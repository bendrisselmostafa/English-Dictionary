import mysql.connector

con = mysql.connector.connect(user="", password="", host="", database="")

cursor = con.cursor()

word = input("Enter a word : ")

req = cursor.execute("select * from Dictionary where expression = '%s'" % word)

results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("No such word")
