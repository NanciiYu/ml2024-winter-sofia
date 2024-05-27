import numpy as np
from sklearn.metrics import precision_score, recall_score

# Ask the user for input N (positive integer)
N = int(input("Enter the number of (x, y) points (N): "))

# Initialize arrays to store the ground truth and predicted values
ground_truth = np.zeros(N, dtype=int)
predicted = np.zeros(N, dtype=int)

# Ask the user to provide N (x, y) points and store them in the arrays
for i in range(N):
    x = int(input(f"Enter the ground truth class label (0 or 1) for point {i+1}: "))
    y = int(input(f"Enter the predicted class label (0 or 1) for point {i+1}: "))
    ground_truth[i] = x
    predicted[i] = y

# Calculate Precision and Recall using Scikit-learn
precision = precision_score(ground_truth, predicted)
recall = recall_score(ground_truth, predicted)

# Print the results
print("Precision:", precision)
print("Recall:", recall)
