
      #!/usr/bin/env python3

"""
Sparse Matrix Operations - Created by Frida Ikirezi Kayiranga (GitHub: @code2811)
"""

import sys
import os
from sparse_matrix import SparseMatrix


class SparseMatrixApp:
    def __init__(self):
        self.matrix1 = None
        self.matrix2 = None
        self.user_name = "user"

    def display_welcome(self):
        print("Welcome to Sparse Matrix Operations!")
        self.user_name = input("Before we begin, what’s your name? ").strip() or "user"
        print(f"\nHi {self.user_name}, I’m here to help you work with sparse matrices.")
        print("This tool was built by Frida Ikirezi Kayiranga (GitHub: @code2811)")
        print("=" * 60)

    def load_matrix(self, prompt):
        while True:
            try:
                file_path = input(f"{prompt}\n> ").strip()
                if not file_path or not os.path.exists(file_path):
                    print(f"File not found: '{file_path}'. Please check the path and try again.")
                    continue

                matrix = SparseMatrix(file_path=file_path)
                print("Matrix loaded successfully.")
                print(matrix)
                return matrix

            except ValueError as e:
                print(f"Error: {e}")
            except Exception as e:
                print(f"Unexpected error: {e}")

            retry = input("Would you like to try another file? (y/n): ").strip().lower()
            if retry != 'y':
                return None

    def load_matrices(self):
        print(f"\nLet's load your matrices, {self.user_name}.")
        self.matrix1 = self.load_matrix("Enter the path to your first matrix file:")
        if not self.matrix1:
            return False

        self.matrix2 = self.load_matrix("Enter the path to your second matrix file:")
        return bool(self.matrix2)

    def display_menu(self):
        print("\n" + "=" * 40)
        print("Select an operation:")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrices")
        print("4. Show Matrix Info")
        print("5. Load New Matrices")
        print("6. Exit")
        print("=" * 40)

    def perform_operation(self, choice):
        if not self.matrix1 or not self.matrix2:
            print("Please load both matrices before performing operations.")
            return None

        try:
            operations = {
                '1': ('Addition', self.matrix1.add),
                '2': ('Subtraction', self.matrix1.subtract),
                '3': ('Multiplication', self.matrix1.multiply),
            }

            if choice in operations:
                name, func = operations[choice]
                print(f"\nPerforming {name.lower()}...")
                result = func(self.matrix2)
                print(f"{name} completed successfully.")
                return result
            else:
                print("Invalid operation selected.")
        except Exception as e:
            print(f"Operation failed: {e}")
        return None

    def display_matrix_info(self):
        if not self.matrix1 or not self.matrix2:
            print("No matrices are currently loaded.")
            return

        print("\nMatrix Information:")
        print(f"Matrix 1:\n{self.matrix1}")
        print(f"Matrix 2:\n{self.matrix2}")

        m1_dims = self.matrix1.get_dimensions()
        m2_dims = self.matrix2.get_dimensions()

        print(f"\nMatrix 1: {m1_dims[0]}x{m1_dims[1]} with {self.matrix1.get_non_zero_count()} non-zero elements")
        print(f"Matrix 2: {m2_dims[0]}x{m2_dims[1]} with {self.matrix2.get_non_zero_count()} non-zero elements")

        print("\nOperation Compatibility:")
        print(f"Addition/Subtraction: {'Yes' if m1_dims == m2_dims else 'No'}")
        print(f"Matrix 1 × Matrix 2: {'Yes' if m1_dims[1] == m2_dims[0] else 'No'}")
        print(f"Matrix 2 × Matrix 1: {'Yes' if m2_dims[1] == m1_dims[0] else 'No'}")

    def save_result(self, matrix):
        if input("\nWould you like to save the result? (y/n): ").strip().lower() == 'y':
            output = input("Enter output file path: ").strip()
            try:
                matrix.save_to_file(output)
                print(f"Result saved to '{output}'.")
            except Exception as e:
                print(f"Could not save the file: {e}")

    def display_result(self, matrix):
        print("\nResult Matrix:")
        print(matrix)
        dims = matrix.get_dimensions()
        non_zero = matrix.get_non_zero_count()

        print(f"Dimensions: {dims[0]}x{dims[1]}")
        print(f"Non-zero elements: {non_zero}")

        if 0 < non_zero <= 20:
            if input("Would you like to view the matrix data? (y/n): ").strip().lower() == 'y':
                print("\nMatrix Data:")
                print(matrix)

    def run(self):
        self.display_welcome()
        if not self.load_matrices():
            print("Could not load matrices. Exiting.")
            return

        while True:
            self.display_menu()
            try:
                choice = input("Choose an option (1-6): ").strip()

                if choice in ['1', '2', '3']:
                    result = self.perform_operation(choice)
                    if result:
                        self.display_result(result)
                        self.save_result(result)
                elif choice == '4':
                    self.display_matrix_info()
                elif choice == '5':
                    if self.load_matrices():
                        print("Matrices reloaded successfully.")
                    else:
                        print("Failed to reload matrices.")
                elif choice == '6':
                    print(f"Thank you for using Sparse Matrix Operations, {self.user_name}.")
                    print("Created by Frida Ikirezi Kayiranga — GitHub: @code2811")
                    break
                else:
                    print("Invalid input. Please choose a number from 1 to 6.")
            except KeyboardInterrupt:
                print("\nSession interrupted by user.")
                break
            except Exception as e:
                print(f"Unexpected error: {e}")


def main():
    try:
        app = SparseMatrixApp()
        app.run()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
    
      
            

    
        
