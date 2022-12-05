import io
# Open the input file and read its contents as a string
with io.open('Y22\\Day5\\input.txt', 'r') as input_file:
    input_string = input_file.read()
columns = input_string.split('\n')

# Create an empty list to store the columns as lists of characters
column_lists = []

# Use a for loop to iterate over the columns
for column in columns:
    # Use the split() method to split each column into individual characters
    characters = column.split()

    # Use a list comprehension to create a list of the characters in the column
    column_list = [character for character in characters if character.isalpha()]

    # Add the column list to the list of columns
    column_lists.append(column_list)

# Print the resulting list of columns
print(column_lists)  # Output: [['Z', 'N'], ['M', 'C', 'D'], ['P']]