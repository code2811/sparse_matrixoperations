# main.py
# Author: Frida Ikirezi Kayiranga
# Student at African Leadership University (ALU)
# Description: Command-line interface to perform operations on sparse matrices

from sparse_matrix import SparseMatrix

def main():
    print("Welcome to Sparse Matrix Operations")
    print("This tool allows you to add, subtract, or multiply two sparse matrices.\n")

    
    file1 = input("Enter path to first matrix file (e.g., sample_inputs/matrix1.txt): ").strip()
    file2 = input("Enter path to second matrix file (e.g., sample_inputs/matrix2.txt): ").strip()

    try:
        # Load matrices
        matrix1 = SparseMatrix.from_file(file1)
        matrix2 = SparseMatrix.from_file(file2)

        # Choose operation
        print("\nSelect operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        choice = input("Enter 1, 2, or 3: ").strip()

        if choice == "1":
            result = matrix1 + matrix2
            print("\nResult of Addition:")
        elif choice == "2":
            result = matrix1 - matrix2
            print("\nResult of Subtraction:")
        elif choice == "3":
            result = matrix1 * matrix2
            print("\nResult of Multiplication:")
        else:
            print("❌ Invalid choice. Exiting.")
            return

        print(result)
        save = input("\nDo you want to save the result to a file? (y/n): ").strip().lower()
        if save == 'y':
            output_file = input("Enter output file name (e.g., result.txt): ").strip()
            result.to_file(output_file)
            print(f"✅ Result saved to {output_file}")
        else:
            print("Result not saved.")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()

