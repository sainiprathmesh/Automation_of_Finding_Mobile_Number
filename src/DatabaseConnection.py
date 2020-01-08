class DatabaseConnection:
    import mysql.connector as mc
    conn = mc.connect(host="localhost", user="root", passwd="", database="Std")
    cur = conn.cursor()
    if cur:
        print("Connected Sucessfully!")
    else:
        print("Connection Failed!")
