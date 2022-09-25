from flask import Flask, render_template, jsonify

app = Flask(__name__)

jobs = [{
    'id': 1,
    'id_string': 'waiter0',
    'title': 'Waiter',
    'salary': '$25,000',
    'requirements': 'None',
    'description': "be polite, service with a smile!, be an empath",
    'num': 5
}, {
    'id': 2,
    'id_string': 'cashier0',
    'title': 'Cashier',
    'salary': '$30,000',
    'requirements': 'None',
    'description':
    "be good at mental arithmetic, also be a sharpshooter, carry a personal firearm, you'll need it in case things go south",
    'num': 2
}, {
    'id': 3,
    'id_string': 'primary_cook0',
    'title': 'Primary Cook',
    'salary': '$50,000',
    'requirements': '5 years experience',
    'description':
    "good balance of creativity and consistency of quality food",
    'num': 3
}, {
    'id': 4,
    'id_string': 'assistant_cook0',
    'title': 'Assistant Cook',
    'salary': '$45,000',
    'requirements': '2 years experience',
    'description': "a good team player, support role",
    'num': 5
}, {
    'id': 5,
    'id_string': 'dancer0',
    'title': 'Dancer',
    'salary': '$30,000',
    'requirements': 'None',
    'description':
    "pretty, athletic, and understand how to manipulate customers into paying us more money, while having a good time of course",
    'num': 5
}]


@app.route('/')
def hello():
    return render_template('home.html', jobs=jobs)


@app.route('/api/jobs/')
def list_jobs():
    return jsonify(jobs)


if __name__ == "__main__":
    app.run('0.0.0.0', debug=True)
