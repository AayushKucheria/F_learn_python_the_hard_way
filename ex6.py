# a variable storing the number of types of people
types_of_people = 10

# a string
x = f"There are {types_of_people} types of people."

# a string
binary = "binary"

# a string
do_not = "don't"

# y is concatenating the two strings above with another sentence
y = f"Those who know {binary} and those who {do_not}."

#printing both the strings
print(x)
print(y)

# printing x and y again with format for comical purpose
print(f"I said: {x}")
print(f"I also said: '{y}'")

# storing a boolean value false
hilarious = False

# a string with an incomplete format bracket
joke_evaluation = "Isn't that joke so funny?! {}"

# printing @joke_evaluation and adding the previous boolean value to it through format
print(joke_evaluation.format(hilarious))

# initializing two strings, concatenating them, and then printing them.
w = "This is the left side of..."
e = "a string with a right side."

print(w + e)
