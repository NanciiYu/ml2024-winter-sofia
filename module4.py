# Read the value of N from the user
N = int(input("Enter the value of N: "))

# Initialize an empty list to store the numbers
numbers = []

# Read N numbers from the user
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Read the value of X from the user
X = int(input("Enter the value of X: "))

# Check if X exists in the list of numbers
if X in numbers:
    index = numbers.index(X) + 1
    print(index)
else:
    print(-1)
