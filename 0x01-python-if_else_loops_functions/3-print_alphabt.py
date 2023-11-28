#!/usr/bin/python3

def print_alphabets() -> None:
    """
    Prints the latin alphabets in lower case except 'e' and 'q'
    """
    for alphabets in range(97, 123):
        if chr(alphabets) in "eq":
            continue  # skip letters 'e' and 'q'
        print("{:c}".format(alphabets), end="")


if __name__ == "__main__":
    print_alphabets()
