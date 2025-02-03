import psycopg2


class PostgreSQLConnection:
    def __init__(self):
        self.dbname = ''
        self.user = ''
        self.password = ''
        self.host = ""
        self.port = ""
        self.conn = None
        self.cursor = None

    def connect(self):
        if self.conn is None or self.conn.closed:
            try:
                self.conn = psycopg2.connect(
                    dbname=self.dbname,
                    user=self.user,
                    password=self.password,
                    host=self.host,
                    port=self.port
                )
                self.cursor = self.conn.cursor()
            except Exception as e:
                self.conn = None

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            self.conn = None

    def execute_query(self, query, params=None, fetch=False):
        try:
            if self.conn is None:
                self.connect()
            self.cursor.execute(query, params)
            if fetch:
                result = self.cursor.fetchall()
                return result
            self.conn.commit()
        except Exception as e:
            if self.conn:
                self.conn.rollback()
        finally:
            self.close()
