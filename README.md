### Simple helps Channels Discord Bot
This Bot allows users to use the very recently popular framework of having "help channels"
that can be used on discord servers to ask questions. The layout is quite simplistic and allows for expansion.
This version of the bot does the absolute minimum to ensure smooth service.



## Setting up the Bot
So far the bot hasn't been fully built to be set up through the text channels on discord.
It does take a fair bit of setting up and some basic faimliarity with how discord bots are made using python.

Once you have set it up on your own server it is pretty straight forward. You only need to modifyt he JSON file.


```
JSON setup Layout
{
    "TOKEN" : "",
    "Help channels" : ["help-1", "help-2", "help-3", "help-4", "help-5"],
    "Available Help Channel Category Name" : "Available Help Channels",
    "Occupied Help Channels Category Name" : "Occupied Help Channels",
    "Question Asker Role" : " "
}
```

## Reseting the bot
If the server drops all channels must be reset manually.
