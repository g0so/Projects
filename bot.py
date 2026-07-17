# bot.py
# Main bot file: connects to Discord, posts the daily LeetCode problem,
# and pings a role, on a repeating daily schedule.

import os
import discord
from discord.ext import tasks
from datetime import datetime, time, timezone
from dotenv import load_dotenv

from leetcode_api import get_daily_problem
import config

# Load the secret token from the .env file into environment variables.
load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# "Intents" tell Discord which kinds of events/data our bot needs access to.
# We only need the defaults (enough to send messages), so we keep it simple.
intents = discord.Intents.default()
client = discord.Client(intents=intents)

# The exact time of day we want to post, built from our config.py values.
POST_TIME = time(hour=config.POST_HOUR_UTC, minute=config.POST_MINUTE_UTC, tzinfo=timezone.utc)


async def post_daily_problem():
    """
    Fetches today's problem and posts it to the configured Discord channel,
    pinging the configured role.
    """
    problem = get_daily_problem()

    if problem is None:
        # If fetching failed, we skip posting instead of crashing or
        # posting broken data.
        print("[bot] Skipping post - could not fetch today's problem.")
        return

    channel = client.get_channel(config.CHANNEL_ID)
    if channel is None:
        print("[bot] Could not find the configured channel. Check CHANNEL_ID in config.py.")
        return

    # Pick an embed color based on difficulty, just a nice visual touch.
    difficulty_colors = {
        "Easy": discord.Color.green(),
        "Medium": discord.Color.orange(),
        "Hard": discord.Color.red(),
    }
    color = difficulty_colors.get(problem["difficulty"], discord.Color.blue())

    # Build the embed: a structured, nicely formatted message box.
    embed = discord.Embed(
        title=problem["title"],
        url=problem["link"],
        description=problem["description"],
        color=color,
    )
    embed.add_field(name="Difficulty", value=problem["difficulty"], inline=True)
    embed.set_footer(text="LeetCode Daily Challenge")

    # The role mention format Discord understands is <@&ROLE_ID>.
    role_mention = f"<@&{config.ROLE_ID}>"

    # content=role_mention actually pings the role; the embed carries the details.
    await channel.send(content=f"{role_mention} Today's LeetCode challenge is here!", embed=embed)
    print(f"[bot] Posted: {problem['title']}")


@tasks.loop(time=POST_TIME)
async def daily_post_task():
    """
    This function automatically runs once every day at POST_TIME (UTC),
    thanks to the @tasks.loop(time=...) decorator above.
    """
    await post_daily_problem()


@client.event
async def on_ready():
    """
    This runs once, automatically, the moment the bot successfully
    connects to Discord.
    """
    print(f"[bot] Logged in as {client.user}")
    if not daily_post_task.is_running():
        daily_post_task.start()


# Starts the bot, using our secret token to log in.
client.run(DISCORD_TOKEN)