# Exercise 1: Vowel or Consonant
#
# Write a Python function named `check_letter` that determines if a given letter
# is a vowel or a consonant.
#
# Requirements:
# - The function should prompt the user to enter a letter (a-z or A-Z) and determine its type.
# - It should handle both uppercase and lowercase letters.
# - If the letter is a vowel (a, e, i, o, u), print: "The letter x is a vowel."
# - If the letter is a consonant, print: "The letter x is a consonant."
# - Replace 'x' with the actual letter entered by the user.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Utilize the `in` operator to check for vowels.
# - Ensure to provide feedback for non-alphabetical or invalid entries.


'''
def check_letter():
    while True:
        letter = input('Please enter a letter from A-Z:').lower()
        if letter.isalpha():
            vowels = "aeiou"
            consonants = "bcdfghjklmnpqrstvwxyz"
            print(f'The user entered { letter }')

            if letter == "quit":
                break
            elif letter in vowels: 
                print(f"The letter { letter } is a vowel.")
            elif letter in consonants:
                print(f"The letter { letter } is a consonant.")
            else:
                print('Please type a letter in the englinsh alphabet from a-z')

# Call the function

check_letter()
'''

# Exercise 2: Old enough to vote?
#
# Write a Python function named `check_voting_eligibility` that determines if a user is old enough to vote.
# Fill in the logic to perform the eligibility check inside the function.
#
# Function Details:
# - Prompt the user to input their age: "Please enter your age: "
# - Validate the input to ensure the age is a possible value (no negative numbers).
# - Determine if the user is eligible to vote. Set a variable for the voting age.
# - Print a message indicating whether the user is eligible to vote based on the entered age.
#
# Hints:
# - Use the `input()` function to capture the user's age.
# - Use `int()` to convert the input to an integer. Ensure to handle any conversion errors gracefully.
# - Use a conditional statement to check if the age meets the minimum voting age requirement.
'''
def check_voting_eligibility():
    voting_age = 18
    while True:
        try:
            user_age = input('Please enter your age:')
            if user_age == "quit":
                break
            else: 
                if int(user_age) >= voting_age: 
                    print(f"You are old enough to vote")
                else:
                    print('Sorry you are too young to vote.  ')
        except:
            print("Please enter your age as a whole number")

# Call the function
check_voting_eligibility()
'''

# Exercise 3: Calculate Dog Years
#
# Write a Python function named `calculate_dog_years` that calculates a dog's age in dog years.
# Fill in the logic to perform the calculation inside the function.
#
# Function Details:
# - Prompt the user to enter a dog's age: "Input a dog's age: "
# - Calculate the dog's age in dog years:
#      - The first two years of the dog's life count as 10 dog years each.
#      - Each subsequent year counts as 7 dog years.
# - Print the calculated age: "The dog's age in dog years is xx."
# - Replace 'xx' with the calculated dog years.
#
# Hints:
# - Use the `input()` function to capture user input.
# - Convert the string input to an integer using `int()`.
# - Apply conditional logic to perform the correct age calculation based on the dog's age.
'''
def calculate_dog_years():
    
    while True:
        try:
            dog_age = input('Please enter your dogs age:')
            if dog_age == "quit":
                break
            else: 
                if int(dog_age) <= 2: 
                    dog_years = int(dog_age) * 10
                    print(f"The dog's age in dog years is { dog_years}")
                else: 
                    dog_years = (int(dog_age) - 2) * 7 + 20
                    print(f"The dog's age in dog years is { dog_years}")
        except:
            print("Please enter your dogs age as a whole number")

# Call the function
calculate_dog_years()
'''

# Exercise 4: Weather Advice
#
# Write a Python script named `weather_advice` that provides clothing advice based on weather conditions.
#
# Requirements:
# - The script should prompt the user to enter if it is cold (yes/no).
# - Then, ask if it is raining (yes/no).
# - Use logical operators to determine clothing advice:
#   - If it is cold AND raining, print "Wear a waterproof coat."
#   - If it is cold BUT NOT raining, print "Wear a warm coat."
#   - If it is NOT cold but raining, print "Carry an umbrella."
#   - If it is NOT cold AND NOT raining, print "Wear light clothing."
#
# Hints:
# - Use logical operators (`AND`, `OR`, `NOT`) in your if statements to handle multiple conditions.
'''
def weather_advice():
    while True:
        cold = input('Is it cold today? yes or no: ').lower()
        raining = input('Is it raining today? yes or no: ').lower()
        
        if cold == "yes" and raining == "yes":
            print("Wear a waterproof coat.")
            break
        elif cold == "yes" and raining == "no":
            print("Wear a warm coat.")
            break
        elif cold == "no" and raining == "yes":
            print("Carry an umbrella.")
            break
        elif cold == "no" and raining == "no":
            print("Wear light clothing.")
            break
        else:
            print("Response not valid please only answer yes or no ")
'''

# Call the function
# weather_advice()



# Exercise 5: What's the Season?
#
# Write a Python function named `determine_season` that figures out the season based on the entered date.
#
# Requirements:
# - The function should first prompt the user to enter the month (as three characters): "Enter the month of the year (Jan - Dec):"
# - Then, the function should prompt the user to enter the day of the month: "Enter the day of the month:"
# - Determine the current season based on the date:
#      - Dec 21 - Mar 19: Winter
#      - Mar 20 - Jun 20: Spring
#      - Jun 21 - Sep 21: Summer
#      - Sep 22 - Dec 20: Fall
# - Print the season for the entered date in the format: "<Mmm> <dd> is in <season>."
#
# Hints:
# - Use 'in' to check if a string is in a list or tuple.
# - Adjust the season based on the day of the month when needed.
# - Ensure to validate input formats and handle unexpected inputs gracefully.
'''
def determine_season():  
    winter_months = ('Dec', 'Jan', 'Feb', 'Mar')
    spring_months = ('Mar', 'Apr', 'May', 'Jun')
    summer_months = ('Jun', 'Jul', 'Aug', 'Sep')
    autumn_months = ('Sep', 'Oct', 'Nov', 'Dec')

    season_boundaries = {
    'Winter': (('Dec', 21), ('Mar', 19)),
    'Spring': (('Mar', 20), ('Jun', 20)),
    'Summer': (('Jun', 21), ('Sep', 21)),
    'Fall': (('Sep', 22), ('Dec', 20))
    }
    
    month = input("Enter the month of the year using the first three letters of the month (Jan - Dec): ").capitalize()
    day = input("Enter the day of the month: ")
    day = int(day)
    
    if month in winter_months:
        if (month == 'Dec' and day >= 21 ) or (month == 'Jan') or (month == 'Feb') or (month == 'Mar' and day <= 19):
            season = "Winter"
    if month in spring_months:
        if (month == 'Mar' and day >= 20) or (month == 'Apr') or (month == 'May') or (month == 'Jun' and day <= 20):
            season = "Spring"
    if month in summer_months:
        if (month == 'Jun' and day >= 21) or (month == 'Jul') or (month == 'Aug') or (month == 'Sep' and day <= 21):
            season = "Summer"
    if month in autumn_months:
        if (month == 'Sep' and day >= 22) or (month == 'Oct') or (month == 'Nov') or (month == 'Dec' and day <= 20):
            season = "Winter"
    print(f"{month} {day} is in  {season}")
# Call the function
determine_season()
'''

# Exercise 7: Number Guessing Game
#
# Write a Python function named `guess_number` that allows a user to guess a predetermined number within a range.
#
# Requirements:
# - Set a fixed number as the target for guessing (e.g., 42).
# - Prompt the user to guess a number within a range (e.g., 1 to 100).
# - Allow the user to guess up to five times.
# - After each guess, use conditional statements with AND, OR, and NOT to give the user hints like:
#   - "Guess is too low" or "Guess is too high."
#   - "Last chance!" when they are on their fifth guess.
# - Print "Congratulations, you guessed correctly!" if they guess the number.
# - Print "Sorry, you failed to guess the number in five attempts." if they do not succeed.
#
# Hints:
# - Use a for loop with a range to limit guesses to five.
# - Use logical AND, OR, and NOT to check conditions and provide appropriate feedback.

def guess_number():
    target_num = 25
    guess_attempts = 5

    while guess_attempts > 0:
        try:
            user_guess = int(input(f"Guess the secret number (1-100) you have {guess_attempts} guesses left: "))
        except ValueError:
            print("Your please enter your guess as a whole number between 1-100.")
            continue
        if user_guess == target_num:
            print(f"CONGRATULATIONS! You guessed that the magic number was {target_num}")
            break
        elif user_guess < target_num:
            guess_attempts -=1
            print(f"Incorrect guess. The magic number is larger than {user_guess} you have {guess_attempts} guesses left.")
        elif user_guess > target_num:
            guess_attempts -=1
            print(f"Incorrect guess. The magic number is smaller than {user_guess} you have {guess_attempts} guesses left.")
        else:
            print("That was not a valid guess please enter a whole number between 1 and 100")
    if guess_attempts == 0:
        print(f"You have run out of guesses and didn't find the magic number {target_num}. Better luck next time.")
    
    
# Call the function
guess_number()

