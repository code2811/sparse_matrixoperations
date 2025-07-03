# matrix_app.py
"""
Sparse Matrix CLI App
----------------------
Author   : Frida Ikirezi Kayiranga
GitHub   : https://github.com/code2811
Purpose  : Terminal app for working with sparse matrices.
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
        print("=" * 60)
        print("Welcome to Sparse Matrix Operations!")
        self.user_name = input("Before we begin, what’s your name? ").strip() or "user"
        print(f"\nHi {self.user_name}, I’m here to help you work with sparse matrices.")
        print("Built by Frida Ikirezi Kayiranga (GitHub: @code2811)")
        print("=" * 60)

    def load_matrix(self, prompt):
        while True:
            try:
                file_path = input(f"{prompt}\n> ").strip()
                if not file_path or not os.path.exists(file_path):
                    print(f"❌ File not found: '{file_path}'. Try again.")
                    continue

                matrix = SparseMatrix(file_path=file_path)
                print("✅ Matrix loaded successfully.\n")
                print(matrix)
                return matrix

            except ValueError as e:
                print(f"⚠️  Format error: {e}")
            except Exception as e:
                print(f"❌ Unexpected error: {e}")

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
            print("❌ Please load both matrices first.")
            return None

        try:
            operations = {
                '1': ('Addition', self.matrix1.add),
                '2': ('Subtraction', self.matrix1.subtract),
                '3': ('Multiplication', self.matrix1.multiply),
            }

            if choice in operations:
                name, func = operations[choice]
                print(f"\n🔄 Performing {name.lower()}...")
                result = func(self.matrix2)
                print(f"✅ {name} completed.\n")
                return result
            else:
                print("❌ Invalid operation selected.")
        except Exception as e:
            print(f"❌ Operation failed: {e}")
        return None

    def display_matrix_info(self):
        if not self.matrix1 or not self.matrix2:
            print("ℹ️ No matrices are loaded.")
            return

        m1_dims = self.matrix1.get_dimensions()
        m2_dims = self.matrix2.get_dimensions()

        print("\nMatrix Information:")
        print(f"Matrix 1: {m1_dims[0]} x {m1_dims[1]}, {self.matrix1.get_non_zero_count()} non-zero elements")
        print(f"Matrix 2: {m2_dims[0]} x {m2_dims[1]}, {self.matrix2.get_non_zero_count()} non-zero elements")

        print("\nCompatibility:")
        print(f"Add/Subtract: {'Yes' if m1_dims == m2_dims else 'No'}")
        print(f"Matrix1 × Matrix2: {'Yes' if m1_dims[1] == m2_dims[0] else 'No'}")
        print(f"Matrix2 × Matrix1: {'Yes' if m2_dims[1] == m1_dims[0] else 'No'}")

    def save_result(self, matrix):
        if input("\n💾 Save result? (y/n): ").strip().lower() == 'y':
            output = input("Enter output file path: ").strip()
            try:
                matrix.save_to_file(output)
                print(f"✅ Saved to '{output}'.")
            except Exception as e:
                print(f"❌ Save failed: {e}")

    def display_result(self, matrix):
        print("\n📌 Result Matrix:")
        print(matrix)
        dims = matrix.get_dimensions()
        non_zero = matrix.get_non_zero_count()

        print(f"Size: {dims[0]} x {dims[1]}, Non-zero: {non_zero}")
        if 0 < non_zero <= 20:
            if input("👀 View matrix values? (y/n): ").strip().lower() == 'y':
                print(matrix)

    def run(self):
        self.display_welcome()
        if not self.load_matrices():
            print("❌ Failed to load matrices. Exiting.")
            return

        while True:
            self.display_menu()
            choice = input("Choose an option (1–6): ").strip()
            if choice in ['1', '2', '3']:
                result = self.perform_operation(choice)
                if result:
                    self.display_result(result)
                    self.save_result(result)
            elif choice == '4':
                self.display_matrix_info()
            elif choice == '5':
                self.load_matrices()
            elif choice == '6':
                print(f"\n👋 Goodbye {self.user_name}! Thanks for using the tool.")
                print("Created by Frida Ikirezi Kayiranga — GitHub: @code2811")
                break
            else:
                print("❌ Invalid input. Enter a number between 1 and 6.")


def main():
    try:
        SparseMatrixApp().run()
    except Exception as e:
        print(f"💥 Fatal error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
