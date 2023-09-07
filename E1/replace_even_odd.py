import re

# Function to replace words on even and odd occurrences
def replace_even_odd(text, target_word, replacement1, replacement2):
    count = 0
    def replace_callback(match):
        nonlocal count
        if count % 2 == 0:
            count += 1
            return replacement1
        else:
            count += 1
            return replacement2

    # Use regular expression to find the target word, including "terrible"
    pattern = re.compile(r'\b(' + re.escape(target_word) + r')\b')
    modified_text = pattern.sub(replace_callback, text)
    return modified_text

# Read the content of the input file
with open('file_to_read.txt', 'r') as file:
    content = file.read()

# Count the total occurrences of "terrible" and "terrible!"
terrible_count = content.lower().count("terrible")

# Replace words on even and odd occurrences, including "terrible"
modified_text = replace_even_odd(content, "terrible", "marvellous", "pathetic")

# Write the modified text to the result file
with open('result.txt', 'w') as result_file:
    result_file.write(modified_text)

# Display the total count of "terrible"
print(f'Total occurrences of "terrible" : {terrible_count}')
