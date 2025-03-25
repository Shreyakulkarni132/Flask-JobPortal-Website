#used freesqldatabase.com, tutor used plantscale.
import os
from sqlalchemy import create_engine, text

db_connection_str= os.getenv("db_connection_str")
engine = create_engine(db_connection_str,
                       pool_pre_ping=True, pool_recycle=1800)
#if it does not work/ are using other cloud db, try connect_args={"ssl"...}

if not db_connection_str:
    raise ValueError("Database URL is not set.")


def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))
        jobs = []
        for row in result.mappings():
            jobs.append(dict(row))
        return jobs

def load_job_by_id(id):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT * FROM jobs WHERE id = :id"), {"id": id})
        rows = result.fetchone()
        if not rows:
            return None
        else:
            # Convert row to dictionary using ._mapping
            return dict(rows._mapping)
        
def add_application_to_db(job_id, data):
    with engine.connect() as conn:
        query = text("INSERT INTO applications (job_id, full_name, email, linkedin, resume) VALUES (:job_id, :full_name, :email, :linkedin, :resume)")

        conn.execute(query, { 
            "job_id": job_id,  
            "full_name": data.get("full_name", ""),  
            "email": data.get("email", ""),  
            "linkedin": data.get("linkedin", ""),  
            "resume": data.get("resume", "")  
        })
        conn.commit()