import discord
import responses
from global_variables import help_channels_dict, TOKEN, available_help_channels_category_name, \
    occupied_help_channels_category_name, message_channel_available
from helpers import send_message_to_newly_claimed_channel, send_message_to_user_for_newly_claimed_channel, send_message_to_just_closed_channel


# Send messages
async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        username, user_message, channel = str(message.author), str(message.content), str(message.channel)
        print(f'{username} said: "{user_message}" ({channel})')

        if channel in help_channels_dict:
            if not help_channels_dict[channel].occupied:
                # moving channel so that its now occupied
                category_channel = discord.utils.get(message.guild.channels, name=occupied_help_channels_category_name)
                await message.channel.edit(category=category_channel)

                # updating class properties
                help_channels_dict[channel].occupied = True
                help_channels_dict[channel].question_asker = username
                help_channels_dict[channel].question_pin = message

                # Sending message to user
                await send_message_to_user_for_newly_claimed_channel(message)

                # sending message to channel
                await send_message_to_newly_claimed_channel(message)

                # Pinning user question
                await message.pin()

                # TODO: Assign Role to person asking question

            # only allow the person who asked the channel to close it
            elif user_message == "!close" and help_channels_dict[channel].question_asker == username:
                # update class properties
                help_channels_dict[channel].question_asker = None
                help_channels_dict[channel].occupied = False

                # moving channel back to available category
                category_channel = discord.utils.get(message.guild.channels, name=available_help_channels_category_name)
                await message.channel.edit(category=category_channel)

                # sending relevant message in channel
                await send_message_to_just_closed_channel(message, message_channel_available)

                # unpin the message after the help channel has been freed
                await help_channels_dict[channel].question_pin.unpin()

                # TODO: remove role from person asking question


    client.run(TOKEN)
