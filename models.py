from sqlalchemy import Table, Colum, Integer, String, MetData

metdata_obj = MetData()


workers_table = Table(
    "workers",
    metdata_ob,
    Column("id", Integer, primary_key=true),
    Column("username", string),
)