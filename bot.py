import discord
from discord.ext import commands

# Enable intents so the bot can read messages
intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

bot = commands.Bot(command_prefix='!', intents=intents)

# Change these two lines:
KEYWORD = "destroyed"          # ← Change to your specific word
ALERT_CHANNEL_ID = None    # ← Set to a channel ID (optional) or leave None

@bot.event
async def on_ready():
    print(f'✅ Bot is online as {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:  # Ignore bot's own messages
        return

    # Check if the keyword is in the message (case-insensitive)
    if KEYWORD.lower() in message.content.lower():
        # Choose where to send the alert
        channel = bot.get_channel(ALERT_CHANNEL_ID) if ALERT_CHANNEL_ID else message.channel
        
        if channel:
            await channel.send(f"@here Someone is blowing up our shit!\n{message.jump_url}")

    # Important: process commands if you add any later
    await bot.process_commands(message)

# Run the bot with your token
bot.run(os.getenv("DISCORD_TOKEN"))   # ← Replace with your actual token