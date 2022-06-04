'''

Exercise 4a

For this exercise, reimplement the solution for exercise 4 such that it doesn’t use the int func-
tion at all, but rather uses the built-in ord and chr functions to identify the
character. This implementation should be more robust, ignoring characters
that aren’t legal for the entered number base.

'''
# Function takes hex string and converts to decimal
def hex_output(number):
    hex_string = str(number).lower()[::-1]
    hex = 0
    exponent = 0
    hex_dict = {'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15}
    for x in hex_string:
        if x.isnumeric():
            hex += int(x) * 16**exponent
        elif x in hex_dict: 
            hex += hex_dict[x] * 16**exponent
        exponent += 1
    return hex

print(hex_output(50))
print(hex_output('a23e'))
print(hex_output('4c'))