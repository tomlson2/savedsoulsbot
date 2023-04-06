# Discord Soul Saver Bot

A simple Discord bot that generates a link to a user's Saved Souls profile and sends it in the chat with a custom message.

## Features

- Takes a user's wallet address as input.
- Deletes the command message to keep the chat clean.
- Generates a custom message with the user's profile link.
- Displays the custom message in the chat with the sender's username in bold.

## Requirements

- Python 3.6 or higher
- `discord.py` library
- A Discord bot token

## Installation

1. Clone this repository or download the code as a ZIP file and extract it.

2. Install the required packages:

   ```
   pip install discord.py
   ```

3. Create a `config.ini` file in the same directory as the bot script, and add the following content:

   ```
   [DEFAULT]
   bot_token = YOUR_BOT_TOKEN
   ```

   Replace `YOUR_BOT_TOKEN` with your actual bot token from the Discord Developer Portal.

4. Run the bot script:

   ```
   python bot.py
   ```

## Usage

1. Invite the bot to your Discord server.

2. Use the `!save` command followed by a wallet address to generate a message with a link to the Saved Souls profile:

   ```
   !save 0x123456789abcdef0123456789abcdef01234567
   ```

   The bot will delete the command message and send the custom message with the link.

## License

This project is released under the MIT License. For more information, please refer to the `LICENSE` file.
