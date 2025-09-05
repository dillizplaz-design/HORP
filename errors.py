# bot/errors.py
from __future__ import annotations
import logging
import discord
from discord.ext import commands
from discord import app_commands
from .utils.embeds import error_embed

logger = logging.getLogger("modbot.errors")


def setup_error_handlers(bot: commands.Bot):
    @bot.tree.error
    async def on_app_command_error(interaction: discord.Interaction, error: Exception):
        # central app_command error wrapper
        if isinstance(error, app_commands.MissingPermissions):
            await interaction.response.send_message(embed=error_embed("Missing permissions."), ephemeral=True)
            return
        if isinstance(error, app_commands.CommandInvokeError):
            # unwrap
            orig = error.original
            logger.exception("Command invoke error: %s", orig)
            await interaction.response.send_message(embed=error_embed("Internal error."), ephemeral=True)
            return
        if isinstance(error, app_commands.CommandOnCooldown):
            await interaction.response.send_message(embed=error_embed(str(error)), ephemeral=True)
            return
        # default
        logger.exception("Unhandled app command error", exc_info=error)
        try:
            await interaction.response.send_message(embed=error_embed("Unknown error."), ephemeral=True)
        except Exception:
            pass
