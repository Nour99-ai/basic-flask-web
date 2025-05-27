# basic-flask-web
from flask import Flask , render_template , request 

app = Flask(__name__)

@app.route('/' , methods=['GET' , 'POST'])

def home():
    
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name  = request.form['lastname']
        message = request.form['message']
        Email  =  request.form['email']
        with open('messages.txt' , 'a' , encoding='utf-8') as f :
            f.write(f"{first_name} {last_name}: {message} and the email is : {Email} \n")
        return f"We have received your message: {message}! Thank you {first_name} {last_name}"
    
    if request.method == 'GET':
        return render_template('index.html')

@app.route("/fff", methods=['GET'])
def page():
    return render_template('page.html')


if __name__ == '__main__':
    app.run()
