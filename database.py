from sqlalchemy import create_engine, text

db_username = 'lj1g6qswjcfawjvvijge'
db_password = 'pscale_pw_dfjQDISggY9zQGM2LQSRRekUKIvNvfY8g8pLao6wRDG'
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
    result = conn.execute(text("select * from jobs"))
    jobs = result.fetchall()
    print(jobs)
    return jobs


load_jobs_from_db()
