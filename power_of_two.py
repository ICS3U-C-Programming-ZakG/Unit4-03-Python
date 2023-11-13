#!/usr/bin/env python3
# Created by: Zak Goneau
# Created on: Nov. 13, 2023
# This program gets a number from the user and will calculate every numbered square until it reaches the user's number.


def main():
    # introduce program to user
    print(
        "This program gets a number from the user and does every number from zero to the user number squared.\n"
    )

    # declare variables
    counter = 0
    answer_squared = 0

    # get user input
    user_num_str = input("Please enter a positive integer: ")
    print("\n")

    # try converting user input to an integer
    try:
        user_num_int = int(user_num_str)

        # check if user number is negative
        if user_num_int >= 0:

            # for loop while counter less than user number and increment
            for counter in range(user_num_int + 1):

                # square counter and assign answer_squared variable that value
                answer_squared = counter**2

                # print every number squared to user number
                print("{}^2 = {}".format(counter, answer_squared))

        # tell user if they didn't input a positive integer
        else:
            print("{} is not a positive integer.\n".format(user_num_int))

    # catch any invalid inputs from user
    except Exception:
        print("{} is an invalid input.\n".format(user_num_str))

if __name__ == "__main__":
    main()