from flask import Flask, request, render_template_string
from sparse_matrix import SparseMatrix


app = Flask(__name__)

# ------------------------------------------------------------------------
# Author: Frida Ikirezi Kayiranga
# Institution: African Leadership University (ALU)
# Purpose: Web application to perform sparse matrix operations (add, subtract, multiply)
# ------------------------------------------------------------------------

# HTML Template for upload and operation selection
HTML_FORM = """
<!doctype html>
<html>
<head>
    <title>Sparse Matrix Operations</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; }
        form { margin-bottom: 30px; }
        footer { margin-top: 50px; font-size: 14px; color: gray; }
    </style>
</head>
<body>
    <h2>Sparse Matrix Operations Web Tool</h2>
    <form method="POST" enctype="multipart/form-data">
        <label><strong>Upload Matrix 1 (.txt):</strong></label><br>
        <input type="file" name="matrix1" required><br><br>

        <label><strong>Upload Matrix 2 (.txt):</strong></label><br>
        <input type="file" name="matrix2" required><br><br>

        <label><strong>Select Operation:</strong></label><br>
        <select name="operation" required>
            <option value="add">Add</option>
            <option value="subtract">Subtract</option>
            <option value="multiply">Multiply</option>
        </select><br><br>

        <button type="submit">Compute</button>
    </form>

    {% if result %}
        <h3>Result:</h3>
        <pre>{{ result }}</pre>
    {% endif %}

    <hr>
    <footer>
        <p>Designed and Developed by <strong>Frida Ikirezi Kayiranga</strong><br>
        Student at <strong>African Leadership University (ALU)</strong></p>
    </footer>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        file1 = request.files.get('matrix1')
        file2 = request.files.get('matrix2')
        operation = request.form.get('operation')

        try:
            # Read matrices from file streams (not from file paths)
            matrix1 = SparseMatrix.from_stream(file1.stream)
            matrix2 = SparseMatrix.from_stream(file2.stream)

            # Perform selected operation
            if operation == 'add':
                result_matrix = matrix1 + matrix2
            elif operation == 'subtract':
                result_matrix = matrix1 - matrix2
            elif operation == 'multiply':
                result_matrix = matrix1 * matrix2
            else:
                raise ValueError("Unsupported operation selected.")

            result = str(result_matrix)

        except Exception as e:
            result = f"Error occurred: {str(e)}"

    return render_template_string(HTML_FORM, result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

