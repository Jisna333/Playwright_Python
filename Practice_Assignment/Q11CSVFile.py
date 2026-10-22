# Step 1: Create and write CSV
print("Creating employees.csv...")
file = open("employees.csv", "w")

# Write header
file.write("id,name,salary\n")

# Write employee data
file.write("1,Alice,50000\n")
file.write("2,Bob,60000\n")
file.write("3,Charlie,55000\n")
file.write("4,Diana,65000\n")
file.write("5,Eve,58000\n")

file.close()
print("CSV file created!")

# Step 2: Read and print CSV
print("\nReading employees.csv:")
file = open("employees.csv", "r")
content = file.read()
print(content)
file.close()

