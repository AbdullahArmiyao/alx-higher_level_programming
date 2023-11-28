#!/usr/bin/python3


def print_alphabets() -> None:
    """
    Prints the latin alphabets in lower case

    Notes:
        ASCII lowercase letters are in the range 97 through 122
    """
    for alphabet in range(97, 123):
        print("{:c}".format(alphabet), end="")


if __name__ == "__main__":
    print_alphabets()
