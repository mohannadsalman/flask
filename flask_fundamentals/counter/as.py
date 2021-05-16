from flask import Flask, render_template, request, redirect, \
url_for, flash, make_response, session
app=Flask(__name__)
app.secret_key= 'keep it secret, keep it safe'
@app.route('/')
def visits():
    
    if 'counter' in session:
        session['counter'] = session.get('counter') + 1  # reading and updating session data
    else:
        session['counter'] = 1 # setting session data
    return "Total visits: {}".format(session.get('counter'))

@app.route('/delete-visits/')
def delete_visits():
    session.clear()
    return 'Visits deleted'
#...

if __name__ == "__main__":
    app.run(debug=True)
