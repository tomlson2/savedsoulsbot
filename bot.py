import configparser
import discord
from discord.ext import commands

# Create the bot instance
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

config = configparser.ConfigParser()
config.read("config.ini")
BOT_TOKEN = config.get("DEFAULT", "bot_token")

@bot.event
async def on_ready():
    print(f"{bot.user} is now online!")

@bot.command(name="save")
async def generate_link(ctx, *, wallet: str):
    username = ctx.author.display_name
    url = f"https://savedsouls.art/profile/{wallet}"
    await ctx.message.delete()
    await ctx.send(f"**{username}** needs their soul saved! 🛟\n{url}")

# Run the bot
bot.run(BOT_TOKEN)
