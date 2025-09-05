# bot/utils/checks.py
from __future__ import annotations
import discord
from discord import app_commands
from typing import Callable

def is_guild_owner() -> Callable[[discord.Interaction], bool]:
    async def predicate(interaction: discord.Interaction) -> bool:
        return interaction.user.id == interaction.guild.owner_id
    return app_commands.check(predicate)

def ensure_can_act(target: discord.Member, actor: discord.Member, bot_member: discord.Member) -> None:
    """
    Raise app_commands.CheckFailure if the actor cannot act on target due to hierarchy or identity.
    """
    from discord import app_commands
    if target == actor:
        raise app_commands.CheckFailure("You cannot perform this action on yourself.")
    if target == bot_member:
        raise app_commands.CheckFailure("I cannot act on myself.")
    # owner protection
    if target.guild.owner_id == target.id:
        raise app_commands.CheckFailure("You cannot act on the guild owner.")
    # role hierarchy
    if actor.top_role <= target.top_role and actor.guild.owner_id != actor.id:
        raise app_commands.CheckFailure("You cannot act on a member with an equal or higher role.")
    if bot_member.top_role <= target.top_role:
        raise app_commands.CheckFailure("I do not have a high enough role to act on this member.")
