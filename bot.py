import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

# Add as many keywords/phrases as you want
KEYWORDS = [
    "destroyed",
    "Your tribe killed",
    "destroyed your",
    "Your tribe is now RAID flagged"
]

@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    # Check if ANY of the keywords are in the message
    message_text = message.content.lower()
    triggered = any(keyword.lower() in message_text for keyword in KEYWORDS)

    if triggered:
        await message.channel.send(
            f"@here Someone is blowing up our shit!\n"
            f"**Link:** {message.jump_url}"
        )

    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_TOKEN"))