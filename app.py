from flask import Flask, render_template, jsonify # type: ignore
from database import load_jobs_from_db, load_job_by_id

app = Flask(__name__)

@app.route('/')
def home():
    jobs=load_jobs_from_db()
    return render_template('index.html', jobs=jobs)

@app.route("/api/jobs")
def list_jobs(): 
    jobs = load_jobs_from_db()
    return jsonify(jobs)

@app.route("/job/<id>")
def show_job(id):
    job = load_job_by_id(id) 
    
    if not job:
        return "Not Found", 404
    
    return render_template('job_page.html', job=job)


if __name__ == '__main__':
    app.run(debug=True)
    