# count.py


# Function definitions
def count(string, chars):
  total = 0
  for letter in string:
    if letter in chars:
      total += 1
  return total


# Input
string = input("Enter a string: ")
chars = input("Enter a set of characters with no spaces: ")
while ' ' in chars:
  chars = input("I said no spaces! ")

# Computation
letters = count(string, chars)

# Output
print("The character(s) of", chars, "occur(s) in", string, letters, "times.")