from src.DatabaseConnection import DatabaseConnection


def insert(*li):
    sql_statement = "Insert Into Section VALUES (%s)"
    for ele in li:
        values = (ele,)
        DatabaseConnection.cur.execute(sql_statement, values)
    DatabaseConnection.conn.commit()
    print("Detail Saved Sucessfully!!!")


def insert_student(roll, name, mobile):
    query = "INSERT INTO Number VALUES(%s,%s,%s)"
    args = (roll, name, mobile)
    DatabaseConnection.cur.execute(query, args)
    DatabaseConnection.conn.commit()


def view(*li):
    sql_statement = "SELECT name,mob FROM Number where roll = %s"
    for ele in li:
        sa = (ele,)
        DatabaseConnection.cur.execute(sql_statement, sa)
        output = DatabaseConnection.cur.fetchall()
        for x in output:
            print(x)
