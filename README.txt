This is a (very) small Python program which is used to prevent textual spam in Discord channels. It relies heavily on the Discord.py package (https://github.com/Rapptz/discord.py). Discord.py can be installed using the command 'pip install discord.py'.
The program limits spam by preventing flooding using rate limiting, and by limiting the number of similar messages which can be sent over a period of time by a singular user.
It is intended to be deployed from a webserver, with a Discord account specified using the 'username' and 'password' variables. 

Note: Later versions of Discord.py may break this bot, so you can either use the files inside discord.zip (which work at the time of this commit) or re-write the bot to use the newer library if that becomes a necessity.

It should also be noted that the implementation is rather hacky, and assumes that the bot will be provided with an account with the ability to administer over the relevant channel. It does not have multi channel support, and you may have to do large amounts of debugging yourself if you encounter problems.