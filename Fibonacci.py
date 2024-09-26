# Number of terms to generate
#n_terms = 5

n_terms=int(input("Enter the term "))

# Initialize the first two numbers
a = 0
b = 1

# Print the first two numbers
print(a)
print(b)

# Initialize a counter for the terms
count = 2

# Generate the remaining Fibonacci numbers
while count < n_terms:
    # Calculate the next term
    next_term = a + b
    # Print the next term
    print(next_term)
    # Update a and b for the next iteration
    a = b
    b = next_term
    # Increase the counter
    count += 1
