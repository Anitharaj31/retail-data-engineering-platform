from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:3105@localhost/retail_db"
)

print(engine)