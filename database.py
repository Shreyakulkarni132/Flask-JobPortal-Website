#used freesqldatabase.com, tutor used plantscale.

from sqlalchemy import create_engine, text

#db_connection_str= "mysql+pymysql://sql12769121:6EqJJhuqI8@sql12.freesqldatabase.com/sql12769121?charset=utf8mb4"

engine = create_engine("mysql+pymysql://sql12769121:6EqJJhuqI8@sql12.freesqldatabase.com/sql12769121?charset=utf8mb4",
                       pool_pre_ping=True, pool_recycle=1800)
#if it does not work/ are using other cloud db, try connect_args={"ssl"...}

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
       
        