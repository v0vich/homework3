def create_table():
    import sqlite3

    connection = sqlite3.connect('phones.db')

    cursor = connection.cursor()

    cursor.execute("DROP TABLE IF EXISTS PHONES")


    table = """ CREATE TABLE PHONES (
                phone_id INTEGER PRIMARY KEY,
                phone_value CHAR(255) NOT NULL,
                contact_name VARCHAR(25)
            ); """

    cursor.execute(table)

    print("Table created")

    connection.close()
