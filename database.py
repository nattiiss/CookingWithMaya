from sqlalchemy import create_engine

db_connection_string = "mysql+pymysql://vlv157z7evtchndtzqyp:pscale_pw_6fdWOjbeoBW8sOzAXVAZKE8tr2erRpgaDIeCdix9DLs@eu-west.connect.psdb.cloud/natiswabesite?charset=utf8mb4"
engine = create_engine(db_connection_string)

with engine.connect() as conn:
  result = conn.execute(text("select * from cakes"))
  print(result.all())
