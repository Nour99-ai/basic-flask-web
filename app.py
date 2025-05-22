
from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route('/heram', methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template('index.html')

    # POST method
    firstname = request.form.get('firstname', '').strip()
    lastname = request.form.get('lastname', '').strip()
    email = request.form.get('email', '').strip()
    message = request.form.get('message', '').strip()

    # Basic input validation
    if not firstname  or not lastname or not email or not message:
        return "<h2>All fields are required.</h2>" \
               "              <hr>               " \
               "<h3>    Please try again>   </h3>" , 400

    # Save all fields to file
    with open('messages.txt', 'a', encoding='utf-8') as f:
        f.write(f"{firstname} {lastname} <{email}>: {message}\n")

    return f"We have received your message: {message}! Thank you {firstname} {lastname}!"

@app.route("/fff", methods=['GET'])
def page():
    try:
        return render_template('page.html')
    except Exception:
        # If template not found, show a 404 page
        return (
            '''
            <h1>404 Page not found</h1>
            <p>Sorry, the page you are looking for does not exist.</p>
            <p>Return to <a href="/">home</a></p>
            ''', 404
        )

if __name__ == '__main__':
    app.run(debug=True)

