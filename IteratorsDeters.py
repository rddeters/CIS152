import array
import random

ARRAY_SIZE = 10  # A constant to set the size of the array
MIN_VALUE = 5  # Minimum random value
MAX_VALUE = 25  # Maximum random value


def fill_array_with_numbers(size, min_val, max_val):
    # Create the array with an integer type
    iterator_array = array.array('i')

    # Add the random values to the array
    for n in range(size):
        iterator_array.append(random.randint(min_val, max_val))

    return iterator_array


def main():
    # Fill the array with random numbers using a separate function
    iterator_array = fill_array_with_numbers(ARRAY_SIZE, MIN_VALUE, MAX_VALUE)
    myit = iter(iterator_array)

    # Iterate through the array and print the numbers
    for item in myit:
        print(item)


if __name__ == "__main__":
    main()
