# Readme - Code Overview and Explanation

This document serves as a readme for the provided Python code. The code is a Discord bot written in Python using the Discord.py library. The bot simulates a text-based RPG-style game where users can interact with it using various commands to receive different roles and items. The bot assigns random "haki," "sabre" (sword), and "fruit" roles to users. The type of "fruit" role can be either "logia," "paramecia," or "zoan." The "zoan" type further has subtypes: "naturel," "antique," and "mythologique."

## Prerequisites

- Python 3.x
- Discord.py library
- dotenv library

## Installation

1. Make sure you have Python 3.x installed on your system.
2. Install the required libraries using pip:

```bash
pip install discord.py
pip install python-dotenv
```
##Setting Up
1. Create a new Discord bot and obtain its token from the Discord Developer Portal.
2. Create a **.env** file in the same directory as the Python script.
3. Add your Discord bot token to the **.env** file:
```bash
TOKEN=YOUR_DISCORD_BOT_TOKEN
```

##Usage
1. Run the Python script to start the bot.
2. Invite the bot to your Discord server using the appropriate permissions.
3. Interact with the bot using the predefined commands explained below.

##Commands
**/depart**: Starts a new adventure for the user, granting them random roles (beyond their control) like "boat" or "money."
**/haki**: Assigns the user random haki roles ("haki de l'observation" or "haki de l'armement").
**/sabre**: Gives the user a "sabre" role. The user might receive it or not randomly.
**/fruit**: Grants the user a "fruit" role. The user may or may not receive it randomly.
**/typefruit**: Reveals the type of the user's "fruit" role among "logia," "paramecia," or "zoan." The bot also shares a GIF based on the type.
**/zoan**: If the user has a "zoan" type "fruit," this command reveals the specific subtype (naturel, antique, or mythologique) and shares a GIF related to the subtype.

##Miscellaneous
The bot assigns roles based on random boolean choices to create the illusion of randomness in the user's journey.
The bot also uses GIFs to add a fun and interactive element to the game-like experience.

##Disclaimer

This bot is purely for fun and entertainment purposes. The author does not take responsibility for any unintended consequences or misuse of the bot. Please use the bot responsibly and follow the Discord API Terms of Service.


Please note that this README is meant to provide an overview and explanation of the code. In practice, you might want to modify it based on your specific project requirements and customize the user experience accordingly.
