import sqlite3
from datetime import datetime

conn = sqlite3.connect('data.db')
c = conn.cursor()


def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS RecordONE (Room_No TEXT, Name REAL, Date_Time TEXT, Mode_of_transport Text, Reason Text, Addhar_No TEXT, Rent Text)")


Room_No = int(input("Room_No: "))
Name = str(input("Name: "))
Mode_of_transport = str(input("Mode_of_transport: "))
Reason = str(input("Reason: "))
Addhar_No = int(input("Addhar_No.: "))
Rent = int(input("Rent: "))


def data_entry(Room_No, Name, Mode_of_transport, Reason, Addhar_No, Rent):
    now = datetime.now()  # for adding time automaticaly
    current_time = now.strftime("%D:%H:%M:%S")
    print("Current Time =", current_time)
    Date_Time = current_time

    c.execute("INSERT INTO RecordONE (Room_No, Name, Date_Time, Mode_of_transport, Reason, Addhar_No, Rent) VALUES(?, ?, ?, ?, ?, ?, ?)", (Room_No, Name, Date_Time, Mode_of_transport, Reason, Addhar_No, Rent))


create_table()

data_entry(Room_No, Name, Mode_of_transport, Reason, Addhar_No, Rent)

conn.commit()
c.close()
conn.close()
