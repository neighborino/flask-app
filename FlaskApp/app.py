from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "b'~\xf3\x0c+\xf0\xedv\x1f\xb4^d\x17\x0c//\xdb\xf7\xea\x10\x80\xa3\x8a(l'"

email_addresses = []

@app.route('/')
def hello_world():
    author="Neighborino"
    name="valued customer"
    return render_template("index.html",author=author,name=name)

@app.route('/signup', methods = ['POST'])
def signup():
    email = request.form['email']
    email_addresses.append(email)
    session['email'] = email
    print("The email addresses are '" + str(email_addresses) + "'")
    return redirect('/')

@app.route('/unregister')
def unregister():
    # Make sure they've already registered an email address
    if 'email' not in session:
        return "You haven't submitted an email!"
    email = session['email']
    # Make sure it was already in our address list
    if email not in email_addresses:
        return "That address isn't on our list"
    email_addresses.remove(email)
    del session['email'] # Make sure to remove it from the session
    return 'We have removed ' + email + ' from the list!'

@app.route('/emails.html')
def emails():
    return render_template('emails.html', email_addresses=email_addresses)

if __name__ == "__main__":
    app.run()
