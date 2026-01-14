# Write a program to perform linear search on a list of 8 numbers entered by the user.
# If the number is found, display its index position; otherwise, display “Element not found”.

numbers = []

# Taking 8 numbers from the user
for i in range(8):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Number to search
search = int(input("Enter the number to search: "))

found = False

# Linear search
for i in range(len(numbers)):
    if numbers[i] == search:
        print("Element found at index:", i)
        found = True
        break

if not found:
    print("Element not found")

# Create a tuple of 5 subjects and print:
# •	The first subject
# •	The last subject

# Create a tuple of 5 subjects
subjects = ("Math", "English", "Physics", "Chemistry", "Biology")

# Print the first subject
print("First subject:", subjects[0])

# Print the last subject
print("Last subject:", subjects[-1])

# Create a dictionary to store product details:
# •	Product ID
# •	Product Name
# •	Product Price
# Update the price of the product and display the updated dictionary.

# Create a dictionary to store product details
product = {
    "Product ID": 101,
    "Product Name": "Laptop",
    "Product Price": 50000
}

# # Display original dictionary
print("Original product details:", product)

# Update the price
product["Product Price"] = 55000

# Display updated dictionary
print("Updated product details:", product)

# Create a tuple that stores:
# •	Student Name
# •	Roll Number
# •	Program
# Unpack the tuple and print each value on a separate line.

# Create a tuple with student details
student = ("Ali Khan", 23, "Pre-Medical")

# Unpack the tuple
name, roll, program = student

# Print each value on a separate line
print("Student Name:", name)
print("Roll Number:", roll)
print("Program:", program)

# Create a dictionary for an employee with:
# •	Name
# •	Department
# •	Salary
# Increase the salary by 10% and display the updated employee record.

# Create a dictionary for an employee
employee = {
    "Name": "Sara Ahmed",
    "Department": "HR",
    "Salary": 50000
}

# Display original employee record
print("Original Employee Record:", employee)

# Increase salary by 10%
employee["Salary"] = employee["Salary"] + (employee["Salary"] * 10 / 100)

# Display updated employee record
print("Updated Employee Record:", employee)
