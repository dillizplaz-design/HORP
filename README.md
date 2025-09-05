# HORP
# Discord Moderation Bot (Python 3.11+, discord.py 2.3+)

Features:
- Slash commands for moderation: /warn, /timeout, /mute, /kick, /ban, /unban, /points, /case, /config, /purge.
- Points system with auto-ban at >=16 points.
- /timeout uses Discord native communication timeouts (member.edit(timed_out_until=...)).
- SQLite default; Postgres toggleable via DB_URL.

## Quickstart (SQLite default)
1. Clone repo.
2. `python -m venv .venv && source .venv/bin/activate`
3. `pip install -U pip`
4. `pip install -r requirements.txt` (or `poetry install`)
5. `cp .env.example .env` and fill values.
6. Run DB migrations (already included): `python -m bot.db.models --init` (makes `data/` and sqlite file).
7. Run: `python -m bot.main`
8. Use `!sync` owner-only command (or use the sync helper) to register slash commands to `DEFAULT_GUILD` for fast iteration.

## Docker
- Build: `docker build -t modbot .`
- Run via docker-compose: `docker-compose up`

## Important perms & intents
- Privileged intents are NOT required for these features but enable member caching.
- Bot needs:
  - `Moderate Members` (for timeouts)
  - `Manage Roles` (for mute role)
  - `Kick Members`, `Ban Members`, `Manage Messages` where relevant

## Testing
`pytest -q`

## Common pitfalls
- Missing `Moderate Members` → /timeout fails.
- Bot below target member in role hierarchy → actions blocked by Discord.
- For auto-ban to work, bot needs `Ban Members`.

## Design notes
- All mod actions create a case (sequential per guild).
- DB writes and discord API calls are done transactionally where feasible: if the API call fails, DB rollback occurs.
- Default points mapping is configurable per guild.

