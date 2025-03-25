from flask import Flask, render_template, jsonify,request # type: ignore
from database import load_jobs_from_db, load_job_by_id, add_application_to_db

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

@app.route("/job/<id>/apply", methods=["POST"])
def apply_to_job(id):
    data = request.form
    
    job = load_job_by_id(id)
    add_application_to_db(job_id=id, data=data)

    return render_template('application.html', application=data, job=job) 


if __name__ == '__main__':
    app.run(debug=True)
    