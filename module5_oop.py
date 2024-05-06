class DataProcessor:
    def __init__(self):
        self.data = []

    def insert_data(self, value):
        self.data.append(value)

    def search_data(self, target):
        if target in self.data:
            return self.data.index(target) + 1
        else:
            return -1

def main():
    processor = DataProcessor()

    N = int(input("Enter the value of N: "))

    print("Enter the numbers:")
    for _ in range(N):
        num = int(input())
        processor.insert_data(num)

    X = int(input("Enter the value of X: "))

    index = processor.search_data(X)
    print(index)

if __name__ == "__main__":
    main()
# module5_mod.py

class DataProcessor:
    def __init__(self):
        self.data = []

    def insert_data(self, value):
        self.data.append(value)

    def search_data(self, target):
        if target in self.data:
            return self.data.index(target) + 1
        else:
            return -1
# module5_call.py

from module5_mod import DataProcessor

def main():
    processor = DataProcessor()

    N = int(input("Enter the value of N: "))

    print("Enter the numbers:")
    for _ in range(N):
        num = int(input())
        processor.insert_data(num)

    X = int(input("Enter the value of X: "))

    index = processor.search_data(X)
    print(index)

if __name__ == "__main__":
    main()
