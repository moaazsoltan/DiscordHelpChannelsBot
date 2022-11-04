import discord


class Channel_Data_Class:
    def __init__(self, name):
        self.name = name
        self.occupied = False
        self.question_asker = ""
        self.question_pin = None


async def send_message_to_newly_claimed_channel(message):
    await message.channel.send(f"This channel is now reserved by {message.author.mention} !")
    embedVar = discord.Embed(title=f"This channel is now reserved!",
                             description=f"Current user: {message.author.mention}", color=0x00ff00)
    embedVar.add_field(name="**Note**", value="Please use ``!close`` once you are done to free the channel.",
                       inline=False)
    await message.channel.send(embed=embedVar)


async def send_message_to_user_for_newly_claimed_channel(message):
    await message.author.send(f"You have reserved this channel channel {message.channel.mention}")
    embedVar = discord.Embed(title="You have just Reserved a channel",
                             description=f"{message.channel.mention}", color=0x00ff00)
    embedVar.add_field(name="Note",
                       value="Please use ``!close`` once you are done to free the channel for others to use.",
                       inline=False)
    await message.author.send(embed=embedVar)


async def send_message_to_just_closed_channel(message, message_channel_available):
    await message.channel.send(f"This channel is now available again for use")
    embedVar = discord.Embed(title="This Channel is now available once again!", description=message_channel_available,
                             color=0x00ff00)
    # embedVar.add_field(name="Field1", value="hi", inline=False)
    await message.channel.send(embed=embedVar)
