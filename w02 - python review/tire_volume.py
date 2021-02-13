
import math

def volume_of_tire(w:float, d:float, a:float):
    part1 = a * math.pi * w * w
    part2 = w * a + 2540 * d
    part3 = 1/10000000
    return part1 * part2 * part3

class RangeError(Exception):
    def __init__(self):
        super().__init__()

def get_measurment(prompt:str, bounds=False):

    minimum = 0, maximum = 0
    if type(bounds) == dict:
        minimum = bounds["minimum"]
        maximum = bounds["maximum"]

    for i in range(10):
        try:
            integer = get_int(prompt)
            if bounds == False: return integer
            if type(bounds) == dict:
                if integer < minimum or integer > maximum:
                    raise RangeError
        except RangeError as msg:
            print(f"Invalid Range Error. Please enter a \
                positive integer between {minimum} and {maximum}")
        else: return integer
    return False

def get_int(prompt: str):
    for i in range(10):
        try:
            integer = input(f"{prompt} ")
            if not integer.isnumeric():
                print(f"'{integer}' is not a positive integer.", end=" ")
            integer = int(integer)
        except ValueError as msg:
            print("Please enter a positive integer.")
        except Exception as msg: print(msg)
        else: return integer
    return False # end the program if too many tries

def prompt():
    width    = get_measurment(
        "\nPlease enter the width of the tire (mm)",
        {"minimum": 180, "maximum": 400})
    if width == False: return width

    ratio    = get_measurment(
        "\nPlease enter the aspect ratio of the tire",
        {"minimum": 45,  "maximum": 70})
    if ratio == False: return ratio

    diameter = get_measurment(
        "\nPlease enter the diameter of the tire (inches)",
        {"minimum": 12,  "maximum": 28})
    if diameter == False: return diameter

    return (width, ratio, diameter)

def main():
    width, ratio, diameter = prompt()
    volume = volume_of_tire(width, ratio, diameter)
    if volume != False:
        print(f"\nThe approximate volume is {volume:.1f} milliliters.\n")

if __name__ == "__main__": main()

