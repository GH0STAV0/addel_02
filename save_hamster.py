import mysql.connector
import time ,os
from datetime import datetime


host="remotemysql.com"
user="f6V3kVwxvH"
passwd="sOVnW1130i"
database="f6V3kVwxvH"





#######################################################################################


def insert_to_db(cnf_name):
	mydb = mysql.connector.connect(host="remotemysql.com",user="f6V3kVwxvH",passwd="sOVnW1130i",database="f6V3kVwxvH")
	mycursor = mydb.cursor()
	sql = "INSERT INTO live_x (u_name, u_pass,status_actv) VALUES (%s, %s, %s)"
	val = (cnf_name, "baba123A*","NA")
	mycursor.execute(sql, val)
	time.sleep(2)
	print("saved to database")

	mydb.commit()

##############################################################################################




###############################
# host_sql="db4free.net"
# user="test_db4freex01"
# passwd="SkPsU4PrbQEH!DJ"
# database="test_db4freex01"
############################

# insert_to_db("wendy12i5griffin@green-vovo.nl.eu.org")