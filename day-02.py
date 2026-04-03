# Using f-strings for string formatting
name = "Ada Lovelace"
language = "Python"

# Create a sentence using an f-string
# The 'f' before the string allows you to embed variables directly.
message = f"Hello, my name is {name} and I am learning {language}."

print(message)

# You can also do expressions inside the curly braces
year = 1815
current_year = 2026
age = current_year - year

print(f"{name} would be {age} years old in {current_year}.")