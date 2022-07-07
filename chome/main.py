# from selenium import webdriver
# from selenium_stealth import stealth

import drive_md
import cnf

import emoji
from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options as options
from selenium.webdriver.firefox.options import Options as Firefox_Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random,datetime,string , os ,time ,subprocess , sys , requests ,re
from selenium.webdriver import ActionChains

# url_1="https://bot.sannysoft.com/"
# url_1='https://accounts.google.com/servicelogin'
url_1="https://shell.cloud.google.com/?cloudshell=true&show=terminal"


telrgram_text=[]
# email="waelmaiil9"
email="youcefshalhoub"
# email="abedrahman0x"
# email="alphonsoalpatchino"
# email="boudabkafaycel"
# email="xamiramogdan"
# email="almidaopo"
# email="azfounmondilla"
# email="don0mar0l0k0"
# email="zaafaranmaloman"
# email="islamouissam"
# email="kalawssimatrix"
# email="don0mar0l0k0"
# email="abouichrine"
# email="almidaopo"


# email="don0mar0l0k0"
# email="abouichrine"
# email="almidaopo"
# email="youcefshalhoub"



paxx="g0ping0*"
# paxx="g0ping0**"

jb="clear && docker ps"

#####################################

def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		#
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		# os.system("ps aux | grep -i geckodriver_15 | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i chromedriver | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/*")
		os.system("rm /var/log/openvpn/openvpn.log > /dev/null 2>&1")
		os.system("ps aux | grep -i chrome | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		time.sleep(2)
		print(" OK !!!")
	except:
		print(" NO  some_Error init_fire")
###################################################################################################
###################################################################################################


def stage_1():
	try:
		#print (url_1)
		init_fire()
		os.system("rm -rf /tmp/*") 
		os.system("clear && sleep 1") 
		print ( "-------------------------------------------------------")
		print(emoji.emojize("Website    : "+url_1+' :check_mark_button: :alien:'))
		print("System     : "+cnf.sys_use_agent)
		print ( "-------------------------------------------------------")
	except Exception as error:
		print (str(error))

###########################################################################



###############################  CHECK RECONNECT SHIT ############################################
def check_reconect(driver):
	print("CHECK RECONNECT SHIT ..... ",end='',flush=True)
	try:
		reconnect_button=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//*[@id="cloudshell"]/div/horizontal-split/div[2]/devshell/terminal-container/terminal-status-bar/status-message/mat-toolbar/button[2]')))
		reconnect_button.click()
		print("syeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee!!!!!!")
		driver.close()
		# display.stop()
		starting_tasks()
		
	except Exception as e:
		print("still  not  fucking  reconect!!!!!!")
		open_login_button=WebDriverWait(driver, 58).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xterm-helper-textarea')))
		open_login_button.click()
		open_login_button.send_keys("clear && docker ps",Keys.ENTER)
		time.sleep(300)
		check_reconect(driver)

##########################################################################

def check_remail(driver):
	print("check mail")
	try:
		# //*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[3]/div
		row_recovey_mail=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="view_container"]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div/ul/li[3]/div')))
		print("recovery found")
		row_recovey_mail.click()
		time.sleep(5)
		# //*[@id="knowledge-preregistered-email-response"]
		try:
			input_recovey_mail=WebDriverWait(driver, 58).until(EC.presence_of_element_located((By.XPATH, '//*[@id="knowledge-preregistered-email-response"]')))
			input_recovey_mail.send_keys("cha3b0n@protonmail.com",Keys.ENTER)
			pint("chaaaaaaaaaaaaaaaaaaaaaaaa")
			staage="RECVERY MAIL DONE !!!!!"
			cnf.send_msg_dock(staage)
		except:
			print("oi")
		# input("cli")

	except Exception as e:
		print("no ecovery ")


#################################"MAIN STARTING"##############################
def ads_class(driver):
	try:
		print("OPEN AND VISITE WEB-SITE [ 1 ]...... ",end='',flush=True)
		action = webdriver.ActionChains(driver)
		# print(driver.execute_script("return navigator.userAgent;"))
		driver.get(url_1)
		print(" [ "+url_1+" ]")
		gmail_id_input=WebDriverWait(driver, 65).until(EC.presence_of_element_located((By.XPATH, '//*[@id="identifierId"]')))
		# gmail_id_input.send_keys("xamiramogdan",Keys.ENTER)
		# gmail_id_input.send_keys("quarinamouslou",Keys.ENTER)
		gmail_id_input.send_keys(email,Keys.ENTER)
		#ramitamer613
		time.sleep(12)
		gmail_id_input=WebDriverWait(driver, 65).until(EC.presence_of_element_located((By.XPATH, '//*[@id="password"]/div[1]/div/div[1]/input')))
		# gmail_id_input.send_keys("testpassw0rdDZ*",Keys.ENTER)
		# gmail_id_input.send_keys("agoon007",Keys.ENTER)
		gmail_id_input.send_keys(paxx,Keys.ENTER)
		time.sleep(7)

		# input('password don')
		check_remail(driver)


		time.sleep(3)

		
		driver.get("https://shell.cloud.google.com/?cloudshell=true&show=terminal")
		time.sleep(25)
		# input("")
		# input('google loginAAAAAAAAAAAA')
		print("CHECK XTERMINAL ...... ",end='',flush=True)
		open_login_button=WebDriverWait(driver, 58).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.xterm-helper-textarea')))
		open_login_button.click()
		staage="OK XTEMINAL ACTIVATED [ "+email+" ]"
		print(staage)
		cnf.send_msg_dock(staage)
		open_login_button.send_keys("sudo su",Keys.ENTER)
		time.sleep(10)
		# action.send_keys_to_element(open_login_button, "qwerty").perform()
		open_login_button.send_keys("clear && docker ps",Keys.ENTER)
		time.sleep(3)
		# open_login_button.send_keys("./start.sh",Keys.ENTER)
		# open_login_button.send_keys("reboot -f",Keys.ENTER)
		open_login_button.send_keys("ls",Keys.ENTER)



		time.sleep(25)
		check_reconect(driver)

	except Exception as e:
		print(e)
	# driver.delete_all_cookies()
	
		
# def starting_tasks():
































def starting_tasks():
	# width ,height=cnf_bvb.resolution_func()
	try:

		stage_1()
		width ,height=cnf.resolution_func()
		display = Display(visible=0, size=(width,height)).start()
		driver=drive_md.build_driver()
		# display = Display(visible=visible_v, size=(width,height)).start()
		ads_class(driver)
		# url = "https://bot.sannysoft.com/"
		# driver.get(url)
		# time.sleep(5)
		# input("")
	# driver.quit()
	except:
		print("er")



def main():
	starting_tasks()


if __name__ == '__main__':

	main()





	# input("")
	# url='https://accounts.google.com/servicelogin'