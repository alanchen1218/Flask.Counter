from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'ThisIsSecret'
app.count = 0

@app.route('/')
def index():
    # session['count'] += 0  NEED TO INITIALIZE COUNT TO 0 FIRST
    session['count'] += 1
    return render_template('index.html', count=session['count'])

@app.route('/add', methods=['POST'])
def increment_by_two():
    session['count'] += 1
    # incrementing this count by 1 because refreshing the page already +1
    return redirect('/')

@app.route('/clear', methods=['POST'])
def clear():
    session['count'] = 0
    return redirect('/')

app.run(debug=True)
