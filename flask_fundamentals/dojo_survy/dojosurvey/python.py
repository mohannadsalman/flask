from flask import Flask, render_template, request, redirect
app = Flask(__name__)  
@app.route('/')
def dojo():
	return render_template('first.html')
@app.route('/result', methods=['post'])
def result():
	print(request.form)
	name=request.form['name']
	name2=request.form['name2']
	comment=request.form['comment']
	check=request.form['check']
	agree=request.form['agree']

	
	return render_template('second.html', name=name, name2=name2, comment=comment, check=check,agree=agree)
app.run(debug=True)