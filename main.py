
import numpy as np


class DataAnalytics:

    def __init__(self):
        self.__array = None

    # Get the current array
    def get_array(self):
        return self.__array

    # Store an array
    def set_array(self, arr):
        self.__array = arr

    # Display the array
    def display_array(self):
        if self.__array is None:
            print("Please create an array first.")
        else:
            print("\nCurrent Array:")
            print(self.__array)

    # Create 1D, 2D or 3D array
    def create_array(self):
        print("\n1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                values = list(map(int, input(
                    "Enter numbers separated by spaces: "
                ).split()))

                if len(values) == 0:
                    print("Array cannot be empty.")
                    return

                arr = np.array(values)

            elif choice == 2:
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))

                if rows <= 0 or cols <= 0:
                    print("Dimensions must be positive.")
                    return

                values = list(map(int, input(
                    "Enter all elements separated by spaces: "
                ).split()))

                if len(values) != rows * cols:
                    print("Incorrect number of elements.")
                    return

                arr = np.array(values).reshape(rows, cols)

            elif choice == 3:
                layers = int(input("Enter number of layers: "))
                rows = int(input("Enter number of rows: "))
                cols = int(input("Enter number of columns: "))

                if layers <= 0 or rows <= 0 or cols <= 0:
                    print("Dimensions must be positive.")
                    return

                values = list(map(int, input(
                    "Enter all elements separated by spaces: "
                ).split()))

                if len(values) != layers * rows * cols:
                    print("Incorrect number of elements.")
                    return

                arr = np.array(values).reshape(layers, rows, cols)

            else:
                print("Invalid choice.")
                return

            self.set_array(arr)
            print("\nArray created successfully!")
            self.display_array()

        except ValueError:
            print("Please enter valid numbers.")

    # Indexing and slicing
    def indexing_slicing(self):
        if self.__array is None:
            print("Create an array first.")
            return

        print("\n1. Indexing")
        print("2. Slicing")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                index = int(input("Enter index: "))
                flat_array = self.__array.flatten()

                if -len(flat_array) <= index < len(flat_array):
                    print("Element:", flat_array[index])
                else:
                    print("Index is out of range.")

            elif choice == 2:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))

                flat_array = self.__array.flatten()
                print("Sliced Array:", flat_array[start:end])

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")

    # Mathematical operations
    def mathematical_operations(self):
        if self.__array is None:
            print("Create an array first.")
            return

        print("\n1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Dot Product")

        try:
            choice = int(input("Enter your choice: "))

            if choice not in [1, 2, 3, 4, 5]:
                print("Invalid choice.")
                return

            values = list(map(float, input(
                "Enter elements for the second array: "
            ).split()))

            if len(values) != self.__array.size:
                print("Both arrays must have the same number of elements.")
                return

            arr2 = np.array(values).reshape(self.__array.shape)

            print("\nOriginal Array:")
            print(self.__array)

            print("\nSecond Array:")
            print(arr2)

            if choice == 1:
                result = self.__array + arr2
                print("\nResult of Addition:")
                print(result)

            elif choice == 2:
                result = self.__array - arr2
                print("\nResult of Subtraction:")
                print(result)

            elif choice == 3:
                result = self.__array * arr2
                print("\nResult of Multiplication:")
                print(result)

            elif choice == 4:
                if np.any(arr2 == 0):
                    print("Division by zero is not allowed.")
                    return

                result = self.__array / arr2
                print("\nResult of Division:")
                print(result)

            elif choice == 5:
                if self.__array.ndim != 2:
                    print("Dot product requires 2D arrays.")
                    return

                if self.__array.shape[1] != arr2.shape[0]:
                    print("Array dimensions are not compatible.")
                    return

                result = np.dot(self.__array, arr2)
                print("\nDot Product:")
                print(result)

        except ValueError:
            print("Please enter valid numbers.")

    # Combine or split arrays
    def combine_split(self):
        if self.__array is None:
            print("Create an array first.")
            return

        print("\n1. Combine Arrays")
        print("2. Split Array")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                values = list(map(int, input(
                    "Enter elements for another array: "
                ).split()))

                if len(values) == 0:
                    print("Second array cannot be empty.")
                    return

                arr2 = np.array(values)

                print("\n1. Horizontal Combine")
                print("2. Vertical Combine")

                option = int(input("Enter your choice: "))

                if self.__array.ndim != 2:
                    print("Combining requires a 2D original array.")
                    return

                if option == 1:
                    if arr2.size % self.__array.shape[0] != 0:
                        print("Elements cannot form matching rows.")
                        return

                    arr2 = arr2.reshape(self.__array.shape[0], -1)
                    result = np.concatenate(
                        (self.__array, arr2), axis=1
                    )

                    print("\nCombined Array:")
                    print(result)

                elif option == 2:
                    if arr2.size % self.__array.shape[1] != 0:
                        print("Elements cannot form matching columns.")
                        return

                    arr2 = arr2.reshape(-1, self.__array.shape[1])
                    result = np.concatenate(
                        (self.__array, arr2), axis=0
                    )

                    print("\nCombined Array:")
                    print(result)

                else:
                    print("Invalid choice.")

            elif choice == 2:
                parts = int(input("Enter number of parts: "))

                if parts < 1 or parts > self.__array.size:
                    print("Enter a valid number of parts.")
                    return

                result = np.array_split(self.__array, parts)

                print("\nSplit Arrays:")
                for part in result:
                    print(part)

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter valid numbers.")

    # Search, sort and filter
    def search_sort_filter(self):
        if self.__array is None:
            print("Create an array first.")
            return

        print("\n1. Search a value")
        print("2. Sort the array")
        print("3. Filter values")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                value = float(input("Enter value to search: "))
                positions = np.argwhere(self.__array == value)

                if positions.size == 0:
                    print("Value not found.")
                else:
                    print("Positions:")
                    print(positions)

            elif choice == 2:
                result = np.sort(self.__array, axis=None)
                print("\nSorted Array:")
                print(result)

            elif choice == 3:
                value = float(input("Show values greater than: "))
                result = self.__array[self.__array > value]
                print("\nFiltered Values:")
                print(result)

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter a valid number.")

    # Aggregates and statistics
    def statistics(self):
        if self.__array is None:
            print("Create an array first.")
            return

        print("\n1. Sum")
        print("2. Mean")
        print("3. Median")
        print("4. Standard Deviation")
        print("5. Variance")
        print("6. Minimum and Maximum")
        print("7. Percentiles")
        print("8. Correlation Coefficient")

        try:
            choice = int(input("Enter your choice: "))
            arr = self.__array.astype(float)

            if choice == 1:
                print("Sum:", np.sum(arr))

            elif choice == 2:
                print("Mean:", np.mean(arr))

            elif choice == 3:
                print("Median:", np.median(arr))

            elif choice == 4:
                print("Standard Deviation:", np.std(arr))

            elif choice == 5:
                print("Variance:", np.var(arr))

            elif choice == 6:
                print("Minimum:", np.min(arr))
                print("Maximum:", np.max(arr))

            elif choice == 7:
                print("25th Percentile:", np.percentile(arr, 25))
                print("50th Percentile:", np.percentile(arr, 50))
                print("75th Percentile:", np.percentile(arr, 75))

            elif choice == 8:
                values = list(map(float, input(
                    "Enter another array with the same number of elements: "
                ).split()))

                if len(values) != arr.size:
                    print("Both arrays must have the same number of elements.")
                    return

                arr2 = np.array(values).reshape(arr.shape)

                if arr.size < 2:
                    print("At least two elements are required.")
                    return

                if np.std(arr) == 0 or np.std(arr2) == 0:
                    print("Correlation cannot be calculated.")
                    return

                result = np.corrcoef(
                    arr.flatten(), arr2.flatten()
                )[0, 1]

                print("Correlation Coefficient:", result)

            else:
                print("Invalid choice.")

        except ValueError:
            print("Please enter valid numbers.")

    # Class method
    @classmethod
    def project_name(cls):
        print("\nProject: NumPy Analyzer")

    # Static method
    @staticmethod
    def about():
        print("Analyze arrays using NumPy functions.")


# Main program
def main():
    data = DataAnalytics()

    DataAnalytics.project_name()
    DataAnalytics.about()

    while True:
        print("\n========== NUMPY ANALYZER ==========")
        print("1. Create a NumPy Array")
        print("2. Indexing and Slicing")
        print("3. Mathematical Operations")
        print("4. Combine or Split Arrays")
        print("5. Search, Sort or Filter")
        print("6. Compute Aggregates and Statistics")
        print("7. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if choice == 1:
            data.create_array()

        elif choice == 2:
            data.indexing_slicing()

        elif choice == 3:
            data.mathematical_operations()

        elif choice == 4:
            data.combine_split()

        elif choice == 5:
            data.search_sort_filter()

        elif choice == 6:
            data.statistics()

        elif choice == 7:
            print("\nThank you for using NumPy Analyzer!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
