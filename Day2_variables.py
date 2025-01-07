from datetime import datetime
name = input("what is your name?: ") 
print("Good afternoon " + name)
current_year =datetime.now().year
age =int(input("How old are you?: "))
birth_year = current_year - age
print(f"You were born in the year {birth_year}.")