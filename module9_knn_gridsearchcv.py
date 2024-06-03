import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

# Ask the user for input N (positive integer)
N = int(input("Enter the number of training points (N): "))

# Initialize arrays to store the training data
train_X = np.zeros(N)
train_y = np.zeros(N, dtype=int)

# Ask the user to provide N (x, y) pairs for the training set
for i in range(N):
    x = float(input(f"Enter the x value for training point {i+1}: "))
    y = int(input(f"Enter the y value (class label) for training point {i+1}: "))
    train_X[i] = x
    train_y[i] = y

# Ask the user for input M (positive integer)
M = int(input("Enter the number of test points (M): "))

# Initialize arrays to store the test data
test_X = np.zeros(M)
test_y = np.zeros(M, dtype=int)

# Ask the user to provide M (x, y) pairs for the test set
for i in range(M):
    x = float(input(f"Enter the x value for test point {i+1}: "))
    y = int(input(f"Enter the y value (class label) for test point {i+1}: "))
    test_X[i] = x
    test_y[i] = y

# Reshape the input data for compatibility with Scikit-learn
train_X = train_X.reshape(-1, 1)
test_X = test_X.reshape(-1, 1)

# Perform hyperparameter search for k (1 <= k <= 10)
best_k = None
best_accuracy = 0

for k in range(1, 11):
    # Create a kNN Classifier with the current k value
    knn = KNeighborsClassifier(n_neighbors=k)
    
    # Train the kNN Classifier on the training data
    knn.fit(train_X, train_y)
    
    # Make predictions on the test data
    predictions = knn.predict(test_X)
    
    # Calculate the accuracy of the predictions
    accuracy = accuracy_score(test_y, predictions)
    
    # Update the best k and accuracy if the current accuracy is higher
    if accuracy > best_accuracy:
        best_k = k
        best_accuracy = accuracy

# Print the best k and corresponding test accuracy
print("Best k:", best_k)
print("Test Accuracy:", best_accuracy)
