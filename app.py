from flask import Flask, render_template, jsonify # type: ignore

app = Flask(__name__)

JOBS = [
    {
        'id': 1,
        'title': 'Data Scientist',
        'location': 'Remote',
        'salary': '$120,000'
    },
    {
        'id': 2,
        'title': 'FrontEnd Developer',
        'location': 'Remote',
        'salary': '$220,000'
    },
    {
        'id': 3,
        'title': 'Data Analyst',
        'location': 'Remote',
        'salary': '$90,000'
    },
    {
        'id': 4,
        'title': 'SDE',
        'location': 'Remote',
        'salary': '$110,000'
    }

]

@app.route('/')
def home():
    return render_template('index.html', jobs=JOBS)

@app.route("/api/jobs")
def list_jobs(): 
    return jsonify(JOBS)

if __name__ == '__main__':
    app.run(debug=True)
    