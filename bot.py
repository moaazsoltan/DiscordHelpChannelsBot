import discord
import responses
from global_variables import help_channels_dict, TOKEN, available_help_channels_category_name, \
    occupied_help_channels_category_name, message_channel_available
from helpers import send_message_to_newly_claimed_channel, send_message_to_user_for_newly_claimed_channel


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


            # only allow the person who asked the channel to close it
            elif user_message == "!close" and help_channels_dict[channel].question_asker == username:
                # update class properties
                help_channels_dict[channel].question_asker = None
                help_channels_dict[channel].occupied = False

                category_channel = discord.utils.get(message.guild.channels, name=available_help_channels_category_name)
                await message.channel.edit(category=category_channel)
                await message.channel.send(f"This channel is now available again for use")
                embedVar = discord.Embed(title="This Channel is now available once again!", description=message_channel_available,
                                         color=0x00ff00)
                # embedVar.add_field(name="Field1", value="hi", inline=False)
                await message.channel.send(embed=embedVar)

                # unpin the message after the help channel has been freed
                await help_channels_dict[channel].question_pin.unpin()




    client.run(TOKEN)
