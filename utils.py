from flask import request


def commit_sql(sql: str):
    import sqlite3

    try:
        con = sqlite3.connect('phones.db')
        cur = con.cursor()
        cur.execute(sql)
        con.commit()
    finally:
        con.close()


def phones_create():
    phone_value = request.args.get('phone', '111')

    sql = f"""
    INSERT INTO Phones (phone_value)
    VALUES ({phone_value});
    """
    commit_sql(sql)
    return 'phones_create'


def phones_read():
    import sqlite3
    con = sqlite3.connect('phones.db')
    cur = con.cursor()

    sql = """
    SELECT * FROM Phones;
    """
    cur.execute(sql)

    result = cur.fetchall()
    con.close()

    return result


def phones_update():
    phone_value = request.args['phone']
    phone_id = request.args['id']

    sql = f"""
    UPDATE Phones
    SET phone_value = '{phone_value}'
    WHERE phone_id = {phone_id};
    """
    commit_sql(sql)

    return 'phones_update'


def phones_delete():
    phone_id = request.args['id']

    sql = f"""
    DELETE FROM Phones
    WHERE phone_id = {phone_id};
    """
    commit_sql(sql)

    return 'phones_delete'
