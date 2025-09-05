# bot/main.py
from __future__ import annotations
import asyncio
import logging
from typing import List

import discord
from discord.ext import commands
from discord import app_commands

from .config import settings
from .cogs import moderation, points, config_cog, modlog_cog
from .errors import setup_error_handlers

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("modbot")

intents = discord.Intents.default()
intents.members = True  # helpful; not required for timeouts but useful

bot = commands.Bot(command_prefix="!", intents=intents, application_id=None)  # app commands used
tree = bot.tree


@bot.event
async def on_ready():
    logger.info("Bot ready. Logged in as %s", bot.user)
    # optionally sync to default guild for dev
    if settings.DEFAULT_GUILD:
        try:
            gid = settings.DEFAULT_GUILD
            await tree.sync(guild=discord.Object(id=gid))
            logger.info("Synced commands to guild %s", gid)
        except Exception as exc:
            logger.exception("Failed fast sync: %s", exc)


def main() -> None:
    # cogs
    bot.add_cog(moderation.ModerationCog(bot))
    bot.add_cog(points.PointsCog(bot))
    bot.add_cog(config_cog.ConfigCog(bot))
    bot.add_cog(modlog_cog.ModlogCog(bot))
    setup_error_handlers(bot)
    bot.run(settings.TOKEN)


if __name__ == "__main__":
    main()
