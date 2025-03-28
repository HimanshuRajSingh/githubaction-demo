# app.py (This will generate the static HTML)

import os

def generate_homepage():
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>My Simple Python Home Page</title>
    </head>
    <body>
        <h1>Welcome to My GitHub Pages Site!</h1>
        <p>This page was generated by a Python script By Himanshu.</p>
    </body>
    </html>
    """

    # Create the 'public' directory if it doesn't exist
    os.makedirs('public', exist_ok=True)

    with open('public/index.html', 'w') as f:
        f.write(html_content)

if __name__ == "__main__":
    generate_homepage()
    print("Homepage generated in 'public/index.html'")
