# bot/utils/timeparse.py
from __future__ import annotations
import re
from datetime import timedelta
from typing import Optional

_PATTERN = re.compile(r"^\s*(\d+)\s*([smhdw])\s*$", re.I)


def parse_duration_to_seconds(s: str) -> Optional[int]:
    """
    Parse duration strings like 10m, 2h, 3d, 1w -> seconds.
    Return None on parse failure or zero/negative.
    """
    m = _PATTERN.match(s)
    if not m:
        return None
    num = int(m.group(1))
    unit = m.group(2).lower()
    if num <= 0:
        return None
    if unit == "s":
        return num
    if unit == "m":
        return num * 60
    if unit == "h":
        return num * 3600
    if unit == "d":
        return num * 86400
    if unit == "w":
        return num * 86400 * 7
    return None
