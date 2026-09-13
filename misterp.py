# misterp.py

import time
import system
import configuration


def ask_integer(message, minimum, maximum):
    while True:
        value = system.prompt(message)

        try:
            number = int(value)

            if minimum <= number <= maximum:
                return number

            print(
                f"\nValue must be between {minimum} and {maximum}."
            )

        except ValueError:
            print("\nPlease enter a valid number.")


def get_target():
    target = system.prompt(
        "Select target site [Enter = 127.0.0.1:8080]:"
    ).strip()

    if not target:
        return configuration.DEFAULT_TARGET

    return target


def select_speed():
    print("\nSelect speed:")
    print("1) Low (slow)")
    print("2) Medium (normal)")
    print("3) High (fast)")

    while True:
        choice = system.prompt("Speed:")

        try:
            choice = int(choice)

            if choice in configuration.SPEED_PROFILES:
                return choice

            print("\nPlease select 1, 2 or 3.")

        except ValueError:
            print("\nPlease enter a number.")


def run_test():
    system.show_banner()

    print("\nMister P DDoS - Laboratory Stress Test\n")

    target = get_target()

    bots = ask_integer(
        "Number of bots:",
        configuration.MIN_BOTS,
        configuration.MAX_BOTS,
    )

    duration = ask_integer(
        "Duration in seconds [1-60]:",
        configuration.MIN_DURATION,
        configuration.MAX_DURATION,
    )

    speed = select_speed()
    speed_data = configuration.SPEED_PROFILES[speed]

    system.clear()
    system.show_banner()

    print("\nTest configuration")
    print("------------------")
    print(f"Target:   {target}")
    print(f"Bots:     {bots}")
    print(f"Duration: {duration}s")
    print(
        f"Speed:    "
        f"{speed_data['name']} ({speed_data['description']})"
    )

    print("\nStarting laboratory test...")
    time.sleep(1)

    start = time.monotonic()

    while True:
        elapsed = time.monotonic() - start

        if elapsed >= duration:
            break

        current = min(elapsed, duration)

        print(
            f"\r{system.progress_bar(current, duration)} "
            f"Elapsed: {int(current)}s",
            end="",
            flush=True,
        )

        time.sleep(0.1)

    print(
        f"\r{system.progress_bar(duration, duration)} "
        f"Elapsed: {duration}s"
    )

    print("\n\nTest completed.")
    system.prompt("Press Enter to return to menu...")


def main():
    while True:
        system.show_banner()

        print("1) Mister P DDoS")
        print("0) Exit")

        choice = system.prompt().strip()

        if choice == "1":
            run_test()

        elif choice == "0":
            system.clear()
            print("Goodbye.")
            break

        else:
            print("\nInvalid option.")
            time.sleep(1)


if __name__ == "__main__":
    main()
