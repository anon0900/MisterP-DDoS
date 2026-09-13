# configuration.py

# ─────────────────────────────────────────────
# Application
# ─────────────────────────────────────────────

APP_NAME = "Mister P DDoS"
VERSION = "1.0.0"


# ─────────────────────────────────────────────
# Target
# ─────────────────────────────────────────────

DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8080

DEFAULT_TARGET = f"http://{DEFAULT_HOST}:{DEFAULT_PORT}"


# ─────────────────────────────────────────────
# Safety limits
# ─────────────────────────────────────────────

# Maximum test duration: 60 seconds.
MAX_DURATION = 60
MIN_DURATION = 1

# Conservative worker limit for laboratory testing.
MAX_BOTS = 100
MIN_BOTS = 1


# ─────────────────────────────────────────────
# Speed profiles
# ─────────────────────────────────────────────

SPEED_PROFILES = {
    1: {
        "name": "Low",
        "description": "slow",
        "requests_per_second": 5,
    },

    2: {
        "name": "Medium",
        "description": "normal",
        "requests_per_second": 20,
    },

    3: {
        "name": "High",
        "description": "fast",
        "requests_per_second": 50,
    },
}

DEFAULT_SPEED = 2


# ─────────────────────────────────────────────
# Interface
# ─────────────────────────────────────────────

MENU_OPTIONS = {
    1: "Mister P DDoS",
    0: "Exit",
}

PROMPT_SYMBOL = "╰─➤"


# ─────────────────────────────────────────────
# Progress bar
# ─────────────────────────────────────────────

PROGRESS_BAR_WIDTH = 30
