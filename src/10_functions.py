# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE
def is_even(number):
    if (number % 2 == 0):
        print(True)
    else:
        print(False)
# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"

# YOUR CODE HERE

def print_out(bannana):
    if bannana % 2 == 0:
        print("even")
    else: 
        print("odd")

print_out(num)
is_even(num)