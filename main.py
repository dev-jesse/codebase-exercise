import utils
import data
import processing
import output
import validation
import config


def main():
    print("Starting the program...")
    numbers = data.get_numbers()
    print("Numbers retrieved from data module.")

    print("Validating numbers...")
    valid_numbers = validation.validate_numbers(numbers)
    print("Numbers validated.")

    print("Processing numbers...")
    processed_numbers = processing.process_numbers(valid_numbers, config.MULTIPLIER)
    print("Numbers processed.")

    print("Calculating sum...")
    result = utils.calculate_sum(processed_numbers)
    print("Sum calculated.")

    print("Printing result...")
    output.print_result(result)
    print("Result printed.")

    print("Program finished.")


if __name__ == "__main__":
    main()
