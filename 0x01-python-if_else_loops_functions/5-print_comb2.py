#!/usr/bin/python3

def print_combo() -> None:
    """
    prints numbers from 0 to 99
    """
    for num in range(0, 100):
        # print combinations, separating them with commas and spaces
        print("{:02d}".format(num), end=", " if num < 99 else "\n")


if __name__ == "__main__":
    print_combo()
