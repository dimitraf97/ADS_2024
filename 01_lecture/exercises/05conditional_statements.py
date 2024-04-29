"""
Write a program that asks the user for a number.
The program then determines if the number is even or odd and prints out an appropriate message.

Hint: For checking if the number is even or odd, use the Modulo operator:
remainder = number % 2

Example:

    Enter a number: >> 17
    The number 17 is odd.
"""
# Write your solution here
number=int(input("Please type in a number:"))
even = number % 2 == 0
odd = number % 2 != 0
if number%2 ==0:
    print(f"The number {number} is even.")
else:
    print(f"The number {number} is odd.")

"""
Write a program that asks the user for their exam grade (as a percentage). 
The program then prints out the following message:

* If the grade is below 50%: "Unfortunately, you failed the exam."
* If the grade is 60% or above: "You passed the exam!"
* If the grade is higher or equal to 90: "You are excellent!"

Example:

    Enter your exam grade: >> 63
    You passed the exam!
"""
# Write your solution here
grade=int(input("Please type in your grade as a percentage:"))
if grade >=90:
    print(f"You are excellent!")
elif grade >=60:
    print(f"You passed the exam!")
elif grade <60:
    print(f"Unfortunately, you failed the exam.")

"""
Write a program that simulates a simple lunch ordering system. 

1. Ask the user if they want a sandwich, salad, or wrap.
2. If they want a sandwich, ask what kind (chicken, beef, veggie).
3. If they want a salad, ask what dressing (vinaigrette, ranch, caesar).
4. If they want a wrap, ask if they want it toasted.
5. Print a confirmation of their order choice.

Hint: You don't need to verify the user input. But if you want a challenge, try to repeat reading the user input
in case of invalid input. To do so, you might need to research a little bit about "loops" which will be 
covered later in this course :-)

Example:

    Would you like a sandwich, salad, or wrap? >> salad
    What kind of dressing would you like: vinaigrette, ranch, or caesar? >> ranch
    Your order: Salad with ranch dressing
"""
# Write your solution here
def lunch_ordering_system():
    print("Welcome to the lunch ordering system!")
order=str(input("Would you like a sandwich, salad, or wrap?"))

if order == "sandwich":
    answer=str(input("Would you like it with beef, chicken or veggie?"))
    print(f"Your order: {order} with {answer}")
elif order == "salad":
    answer=str(input("What kind of dressing would you like: vinaigrette, ranch, or caesar?"))
    print(f"Your order: {order} with {answer}")
elif order == "wrap":
    toasted=str(input("Do you want it toasted?"))
    if toasted == "yes":
            print (f"You want your wrap toasted.")
    elif toasted == "no":
            print (f"You don't want your wrap toasted.")
else:
    print("Invalid choice. Please select a sandwich, salad, or wrap.")