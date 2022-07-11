import smtplib
import time
import imaplib
import email
import bs4
import re
from bs4 import BeautifulSoup
from faker import Faker
import datetime
import random
import string
import subprocess as sp
from urllib.parse import quote
imaplib._MAXLINE = 80000

import drive_md



sz="860,860"
driver = drive_md.build_driver(sz)
driver.maximize_window()



def save_it(finall):
	with open('shift_url2','a') as f:
	        f.write(finall+"\n")
	        f.close()

activation=[]
def connection_imap():
	conn = imaplib.IMAP4_SSL("outlook.office365.com", 993)
	gmail_user = 'v0v0-temp@outlook.com'
	gmail_pwd = 'baba123A**'
	# conn.login(gmail_user, gmail_pwd)
	conn.login(gmail_user, gmail_pwd)
	return conn



def gather_acces(emmail,driver):
	print("search for email")
	magic_formul='(SUBJECT "Verify your email address")'
		# magic_formul='(TO "xxxxx" SUBJECT "Verify your email address")'

	magic_formul=magic_formul.replace("xxxxx",emmail)
	magic_formul=magic_formul.encode('utf-8')

	mail=connection_imap()
	mail.select('INBOX')
	status, data = mail.search(None, magic_formul)
	ids = data[0]
	unread_msg_nums = data[0].split()
	print (" [ ",len(unread_msg_nums)," ]",flush=True,end= " ")
	if len(unread_msg_nums) == 0 :
		print("NOTHING FOUND")
		mail.close()
		
		time.sleep(8)
		gather_acces(emmail)


	for emailid in unread_msg_nums:
		# resp3, data3 = mail.uid("fetch", emailid,"(RFC822)" )#mail.uid('search', None, "ALL")
		result, data = mail.fetch(emailid, "(RFC822)")
		print(str(emailid))
		email_body = data[0][1].decode("utf-8")
		za_body_mail = email.message_from_string(email_body)
		iii=za_body_mail.get_content_type()
		ohh=za_body_mail.get_payload()
		#charset = za_body_mail.get_content_charset()
		html0 = za_body_mail.get_payload()#, str(charset), "ignore"#.encode('utf8', 'replace')
		# print(za_body_mail)
		# input("")
		if za_body_mail.is_multipart():
			for part in za_body_mail.get_payload():
				# print(part.get_content_type())
				if part.get_content_type() == 'text/plain' :
					# print(part.get_content_type())
					# html0=part.get_payload()
					payload=part.get_payload(decode=True).decode(part.get_content_charset('utf-8'))
					# print(payload)
		else:
			print(za_body_mail.get_payload())
		# print(za_body_mail.get_payload()[0])
		# print(payload)
		# input("")
		# linkess=re.findall(u'"(https:.*?)"' , payload)
		urls = re.findall(r'http://|https://tr.*', payload)
		urlsw = re.findall(r'http://.*|https://.*', payload)
		if len(urlsw) == 0:
			print('the list is empty')
			activation=urls[2]
		else :
			activation=urlsw[2]
		# print(', '.join(urls))
		# input("")
		l_a = activation.split()
		print(l_a[0])
		driver.get(l_a[0])
		time.sleep(1)
	mail.close()
	return l_a[0]

#gather_acces("alicia20epxlgoodman@biglose3.ml")
#print(link.get('href'))

#read_uniq()
#gather_acces("john21peolg6brown@multi-service-seller.tk")
emmail="rachel40ndchoi@green-vovo.nl.eu.org"
gather_acces(emmail,driver)