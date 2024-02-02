import psycopg2
import psycopg2.extras

class DBConfig:
    username = 'admin'
    password = 'Cooper'
    host = '24.199.125.51'
    database = 'agrisync'
    schema = 'public'
    port = '5432'
    connection = None
    cursor = None

    def init(self):
        connection = psycopg2.connect(
            database=self.database, user=self.username,password=self.password, host=self.host, port=self.port
        )

        self.cursor = connection.cursor(cursor_factory = psycopg2.extras.RealDictCursor)
        self.connection = connection

    def commit(self):
        self.connection.commit()
        self.cursor.close()
        self.connection.close()