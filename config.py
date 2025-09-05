# bot/config.py
from __future__ import annotations
from dataclasses import dataclass
import os
from typing import List, Optional
from dotenv import load_dotenv

load_dotenv()


def _env_list(key: str) -> List[int]:
    raw = os.getenv(key, "")
    if not raw:
        return []
    return [int(x.strip()) for x in raw.split(",") if x.strip()]


@dataclass
class Settings:
    TOKEN: str = os.getenv("TOKEN", "")
    DEFAULT_GUILD: Optional[int] = int(os.getenv("DEFAULT_GUILD")) if os.getenv("DEFAULT_GUILD") else None
    MODLOG_CHANNEL_ID: Optional[int] = int(os.getenv("MODLOG_CHANNEL_ID")) if os.getenv("MODLOG_CHANNEL_ID") else None
    DB_URL: str = os.getenv("DB_URL", "sqlite+aiosqlite:///./data/modbot.sqlite")
    OWNER_IDS: List[int] = _env_list("OWNER_IDS")


settings = Settings()
