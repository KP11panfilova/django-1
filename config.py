def DATABASE_URL_asyncpg(self):
        # postgresql+asyncpg://postgres:postgres@localhost:5432/sa
        return mysql+asyncmy://panfilova:Pa$$w0rd@KP11MYSQL-S1.OUIIT.LOCAL/panfilova_db

def DATABASE_URL_psycopg(self):
        # DSN
        # postgresql+psycopg://postgres:postgres@localhost:5432/sa
        return mysql+aiomysql://panfilova:Pa$$w0rd@KP11MYSQL-S1.OUIIT.LOCAL/panfilova_db
