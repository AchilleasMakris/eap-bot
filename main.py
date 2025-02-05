import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get the bot token from the environment variable
bot_token = os.getenv("DISCORD_BOT_TOKEN")

# Ensure the token was loaded correctly
if bot_token is None:
    print("❌ Error: DISCORD_BOT_TOKEN is missing from .env file")
else:
    print("✅ Token loaded successfully")

# Create the bot instance
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print(f"✅ Logged in as {bot.user}")

# Run the bot with the token
bot.run(bot_token)
