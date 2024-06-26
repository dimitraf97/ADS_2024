"""
Write a program which asks for two integer numbers.
The program should then print out whichever is greater.
If the numbers are equal, the program should print a different message.
Examples:
    Please type in the first number: >> 5
    Please type in another number: >> 3
    The greater number was: 5

    Please type in the first number: >> 5
    Please type in another number: >> 8
    The greater number was: 8

    Please type in the first number: >> 5
    Please type in another number: >> 5
    The numbers are equal!

"""
# Write your solution here
n1=int(input("Please type in the first number: "))
n2=int(input("Please type in the second number: "))

if n1 < n2:
    print(f"The greater number was: {n2}")
elif n1 > n2:
    print(f"The greater number was: {n1}")
elif n1 == n2:
    print(f"The numbers are equal!")
"""
Python comparison operators can also be used on strings. 
String a is smaller than string b if it comes alphabetically before b. Notice however that the comparison is only reliable if
- the characters compared are of the same case, i.e. both UPPERCASE or both lowercase
- only the standard English alphabet of a to z, or A to Z, is used.

Write a program which asks the user for two words. The program should then print out whichever of the two comes alphabetically last.

You can assume all words will be typed in lowercase entirely.

Examples:
Please type in the 1st word: >> car
Please type in the 2nd word: >> scooter
scooter comes alphabetically last.

Please type in the 1st word: >> zorro
Please type in the 2nd word: >> batman
zorro comes alphabetically last.

Please type in the 1st word: >> python
Please type in the 2nd word: >> python
You gave the same word twice.

"""
# Write your solution here
w1=str(input("Please type in the first word: "))
w2=str(input("Please type in the second word: "))
if w1 < w2:
    print(f"{w1} comes alphabetically first.")
elif w1 > w2:
    print(f"{w2} comes alphabetically first.")
elif w1==w2:
    print(f"You gave the same word twice.")
"""
Write a program which asks for the user's name. 
If the name is Huey, Dewey or Louie, the program should recognise the user as one of Donald Duck's nephews.
In a similar fashion, if the name is Morty or Ferdie, the program should recognise the user as one of Mickey Mouse's nephews.

Examples:
    Please type in your name: >> Morty
    I think you might be one of Mickey Mouse's nephews.
    
    Please type in your name: >> Huey
    I think you might be one of Donald Duck's nephews.
    
    Please type in your name: >> Ken
    You're not a nephew of any character I know of.
"""
# Write your solution here
username=str(input("Please type in your user's name: "))
if username == "Huey" or username == "Dewey" or username == "Louie":
    print(f"I think you might be one of Donald Duck's nephews.")
elif username == "Morty" or username == "Ferdie":
    print(f"I think you might be one of Mickey Mouse's nephews.")
else:
    print(f"You're not a nephew of any character I know of.")
"""
FizzBuzz
Write a program which asks the user for an integer number. 
If the number is divisible by three, the program should print out Fizz. 
If the number is divisible by five, the program should print out Buzz. 
If the number is divisible by both three and five, the program should print out FizzBuzz.

Examples:
    Number: >> 9
    Fizz
    
    Number: >> 7
    
    Number: >> 20
    Buzz
    
    Number: >> 45
    FizzBuzz
"""
# Write your solution here
num=int(input("Please type in an integer number: "))
if num%3==0 and num%5==0:
    print(f"Fizzbuzz.")
elif num%5==0:
    print(f"Buzz.")
elif num%3==0:
    print(f"Fizz.")
else:
    print("This integer number is neither divisible by three nor five.")
"""
LeapYear
Generally, any year that is divisible by four is a leap year. 
However, if the year is additionally divisible by 100, it is a leap year only if it also divisible by 400.

Write a program which asks the user for a year, and then prints out whether that year is a leap year or not.

Examples:
    Please type in a year: >> 2011
    That year is not a leap year.
    
    Please type in a year: >> 2020
    That year is a leap year.
    
    Please type in a year: >> 1800
    That year is not a leap year.
"""
# Write your solution here
year=int(input("Please type in a year: "))

