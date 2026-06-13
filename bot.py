import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

KEYWORD = "destroyed"          # ← You can still change this

@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if KEYWORD.lower() in message.content.lower():
        channel = message.channel
        await channel.send(
            f"@here Someone is blowing up our shit!\n"
            f"**Link:** {message.jump_url}"
        )

    await bot.process_commands(message)

bot.run(os.getenv("DISCORD_TOKEN"))