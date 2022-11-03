from helpers import Channel_Data_Class
import json
import discord

file = open("setup.json")
setup_params = json.load(file)


# Set up Parameters import
TOKEN = setup_params["TOKEN"]
help_channels_names = setup_params["Help channels"]
available_help_channels_category_name = setup_params["Available Help Channel Category Name"]
occupied_help_channels_category_name = setup_params["Occupied Help Channels Category Name"]


# creating channel objects for better management
help_channels_dict = dict()

for index, item in enumerate(help_channels_names):
    help_channels_dict[item] = Channel_Data_Class(item)


message_channel_available = """ Send your question here to claim the channel.
**Remember:**

• Ask your question in a clear, concise manner.
• Show your code, and if possible, explain where you are stuck
• Include any errors you might be getting
• After 15 minutes, feel free to ping @Helpers.
• Type the command !close to free the channel when you're done.
"""

