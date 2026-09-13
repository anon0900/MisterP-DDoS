# system.py

import os
import sys
import shutil
import time


# ─────────────────────────────────────────────
# Terminal
# ─────────────────────────────────────────────

def clear():
    """Clear the terminal screen."""
    os.system("cls" if os.name == "nt" else "clear")


def terminal_width():
    """Return the current terminal width."""
    return shutil.get_terminal_size((80, 24)).columns


# ─────────────────────────────────────────────
# Colors
# ─────────────────────────────────────────────

RESET = "\033[0m"
BOLD = "\033[1m"

BLUE = (0, 120, 255)
PURPLE = (170, 0, 255)


def rgb(text, r, g, b):
    """Apply an RGB foreground color."""
    return f"\033[38;2;{r};{g};{b}m{text}{RESET}"


def gradient(text):
    """
    Apply a blue → purple gradient across the text.
    Works line by line and character by character.
    """
    lines = text.splitlines()
    output = []

    for line in lines:
        length = max(len(line), 1)
        colored = []

        for i, char in enumerate(line):
            ratio = i / max(length - 1, 1)

            r = int(BLUE[0] + (PURPLE[0] - BLUE[0]) * ratio)
            g = int(BLUE[1] + (PURPLE[1] - BLUE[1]) * ratio)
            b = int(BLUE[2] + (PURPLE[2] - BLUE[2]) * ratio)

            colored.append(rgb(char, r, g, b))

        output.append("".join(colored))

    return "\n".join(output)


# ─────────────────────────────────────────────
# ASCII
# ─────────────────────────────────────────────

ASCII_ART = r"""
    __  ____      __                   ____
   /  |/  (_)____/ /____  _____       / __ \
  / /|_/ / / ___/ __/ _ \/ ___/      / /_/ /
 / /  / / (__  ) /_/  __/ /         / ____/
/_/  /_/_/____/\__/\___/_/         /_/
"""


def show_banner():
    """Clear the terminal and display the Mister P banner."""
    clear()
    print(gradient(ASCII_ART))


# ─────────────────────────────────────────────
# Input
# ─────────────────────────────────────────────

def prompt(message=""):
    """Display the custom Mister P prompt."""
    return input(f"\n{gradient('╰─➤')} {message}")


# ─────────────────────────────────────────────
# Progress bar
# ─────────────────────────────────────────────

def progress_bar(current, total, width=30):
    """
    Return a terminal progress bar.

    current: current progress
    total: total progress
    """
    if total <= 0:
        total = 1

    current = max(0, min(current, total))
    percentage = current / total
    filled = int(width * percentage)

    bar = "█" * filled + "░" * (width - filled)
    percent = int(percentage * 100)

    return f"[{gradient(bar)}] {percent:3d}%"


# ─────────────────────────────────────────────
# Small utilities
# ─────────────────────────────────────────────

def wait(seconds=1):
    """Pause execution."""
    time.sleep(seconds)


def flush():
    """Immediately flush terminal output."""
    sys.stdout.flush()
