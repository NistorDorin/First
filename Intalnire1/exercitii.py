

input_string = 'Ana merge la Piata'
output_string =''

for i in range(0, len(input_string)):
    if input_string[i].isupper():
        output_string += input_string[i].lower()
    else:
        output_string += input_string[i].lower()

