#!/usr/bin/env python3
"""
Basic Add Two Numbers Project
A simple program that takes two numbers as input and returns their sum.
"""

def add_two_numbers(num1, num2):
    """
    Add two numbers and return the result.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
    
    Returns:
        float: Sum of the two numbers
    """
    return num1 + num2

def get_number_input(prompt):
    """
    Get a valid number input from the user.
    
    Args:
        prompt (str): Prompt message for the user
    
    Returns:
        float: The number entered by the user
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def main():
    """
    Main function to run the add two numbers program.
    """
    print("=" * 40)
    print("   Welcome to Add Two Numbers Program")
    print("=" * 40)
    
    # Get input from user
    num1 = get_number_input("Enter the first number: ")
    num2 = get_number_input("Enter the second number: ")
    
    # Calculate the sum
    result = add_two_numbers(num1, num2)
    
    # Display the result
    print(f"\nResult: {num1} + {num2} = {result}")
    print("\nThank you for using the Add Two Numbers Program!")

if __name__ == "__main__":
    main()
