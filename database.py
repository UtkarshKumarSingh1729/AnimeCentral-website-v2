from sqlalchemy import create_engine, text

db_username = '4ep0e0grb6j05bpskr66'
db_password = 'pscale_pw_czDaZ17Ozq3C4dOLkEfaYKt5jVGqh9FRsKiQddR829S'
db_hostname = 'aws.connect.psdb.cloud'
db_port = '3306'
db_name = 'animecentral'

# Create the connection URL
db_url = f'mysql+pymysql://{db_username}:{db_password}@{db_hostname}:{db_port}/{db_name}'

# Create the SQLAlchemy engine
engine = create_engine(db_url,
                       connect_args={"ssl": {
                         "ssl_ca": "/etc/ssl/cert.pem"
                       }})


def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))
    jobs = result.fetchall()
    print(jobs)
    return jobs


def load_job_from_db(id):
  with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs WHERE id = :val"), val=id)
    rows = result.fetchall()
    if len(rows) == 0:
      return None
    else:
      return dict(rows[0])


def add_application_to_db(job_id, data):
  with engine.connect() as conn:
    query = text(
      "INSERT INTO applications (job_id, full_name, email, linkedin_url, education, work_experience, resume_url) VALUES (:job_id, :full_name, :email, :linkedin_url, :education, :work_experience, :resume_url)"
    )

    conn.execute(query,
                 job_id=job_id,
                 full_name=data['full_name'],
                 email=data['email'],
                 linkedin_url=data['linkedin_url'],
                 education=data['education'],
                 work_experience=data['work_experience'],
                 resume_url=data['resume_url'])
