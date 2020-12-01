# The converter should play the sentence "It's really hot" when the user enters more than 38 degrees.

def temp_converter(celsius):
    msg_1 = " degree Celsius are "
    msg_2 = " degree Fahrenheit."
    result = (celsius * 9/5) + 32
    return str(celsius) + msg_1 + str(result) + msg_2

user_input = input("Enter a temperature in degrees Celsius: ")
fahrenheit_result = temp_converter(float(user_input))

print(fahrenheit_result)

if float(user_input) > 38:
    print("It's really hot!")