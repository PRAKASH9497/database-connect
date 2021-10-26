import mysql.connector
mydb=mysql.connector.connect(
    host='localhost',
    user='prakash',
    password='anand1',
    port='3306',
    database='usersdb'
)
mycursor = mydb.cursor()
mycursor.execute('select * from user_details')
user_details = mycursor.fetchall()
for user_details in user_details:
    print(mydb)
    print('user id : ' + user_details[1])
    print('first name : ' + user_details[2])
    print('second name  : ' + user_details[3])

