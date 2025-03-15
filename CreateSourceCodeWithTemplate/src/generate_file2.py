import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the template file
template_path = os.path.join(script_dir, '../templates/tablename2.py')

# Open the template file for reading
with open(template_path, 'r') as f:
    template = f.read()

# Define variables
name = 'John'
age = 30
email = 'john@example.com'

# Replace placeholders in the template
content = template.format(name=name, age=age, email=email)

# Define the output file path
output_path = os.path.join(script_dir, 'output.txt')

# Write the modified content to a new file
with open(output_path, 'w') as f:
    f.write(content)

print("File 'output.txt' has been generated successfully.")

