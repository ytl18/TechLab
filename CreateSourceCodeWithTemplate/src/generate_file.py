import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the template file
template_path = os.path.join(script_dir, '../templates/tablename.py')

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


from pyspark.sql import SparkSession

# Initialize SparkSession
spark = SparkSession.builder \
    .appName("Table Names Replacement") \
    .getOrCreate()

# Databricks database names
database1_name = '<database1-name>'
database2_name = '<database2-name>'

# Fetch table names from the first database
table_names_1 = spark.sql(f"SHOW TABLES IN {database1_name}").select("tableName").rdd.map(lambda row: row[0]).collect()

# Fetch table names from the second database
table_names_2 = spark.sql(f"SHOW TABLES IN {database2_name}").select("tableName").rdd.map(lambda row: row[0]).collect()

# Find the intersection of table names
table_names_intersection = list(set(table_names_1) & set(table_names_2))

# Read the template file
with open('template.txt', 'r') as f:
    template = f.read()

# Loop through each table name in the intersection
for table_name in table_names_intersection:
    # Replace the placeholder with the current table name
    content = template.format(name=table_name)

    # Write the modified content to a new file
    with open(f'output_{table_name}.txt', 'w') as f:
        f.write(content)

    print(f"File 'output_{table_name}.txt' has been generated successfully.")

# Stop SparkSession
spark.stop()
