# Import the Flask class from the flask module
from flask import Flask, render_template_string

# Create an instance of the Flask class
app = Flask(__name__)

# The HTML template as a string
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask App</title>
</head>
<body>
    <h1>Hello World, Surya bhai</h1>
</body>
</html>
"""

# Define the root URL route ('/')
@app.route('/')
def hello_world():
    """
    This function handles requests to the root URL.
    It renders a simple HTML template with the specified text.
    """
    return render_template_string(HTML_TEMPLATE)

# Run the app in debug mode if the script is executed directly
if __name__ == '__main__':
    app.run(debug=False, port=5000, host='0.0.0.0')
