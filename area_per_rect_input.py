#!/usr/bin/env python3
# Created by: jedidiah
# Created on: Nov. 29, 2021
# This program asks the user for the length and
# width of the rectangle in mm. It then
# calculates and displays the area and
# perimeter.
import math


def main():
    # input
    print("We will calculate the area and")
    print("perimeter of a rectangle")
    length = int(input("Enter the length (mm): "))
    width = int(input("Enter the width (mm): "))

    # process
    area = length * width
    perimeter = 2*(length + width)

    # output
    print("")
    print("Area = {} mm^2". format(area))
    print("Perimeter = {} mm". format(perimeter))


if __name__ == "__main__":
    main()
