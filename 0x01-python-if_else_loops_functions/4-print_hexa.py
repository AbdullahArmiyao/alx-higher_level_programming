#!/usr/bin/python3

def print_deci_hexa() -> None:
    """
    Prints all decimals and their hexadecimal equivalent
    """
    for deci in range(0, 99):
        print("{:d} = 0x{:x}".format(deci, deci))


if __name__ == "__main__":
    print_deci_hexa()
