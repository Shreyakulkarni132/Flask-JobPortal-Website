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
