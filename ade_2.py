import cnf_bvb
import mod_vpn2
import mod_driver
import drive_md
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
import json
import t00l
import io
from pydub import AudioSegment
import speech_recognition as sr
import activation_link
import save_hamster


urls_BVB="https://xhamsterlive.com/adel_love"
# urls_BVB="https://xhamsterlive.com/rozana_holmess"


# urls_BVB="https://indab0x.nl.eu.org/"


main_url="https://nordcheckout.com/"

user_agent = cnf_bvb.user_agent


try:
	sys_use_agent=re.findall('\(.*?\)',user_agent)[0]
	
except Exception as e:
	sys_use_agent="eereee"

file_list_1='succes_2'
########################################################################################################################################
def audio_fonction(download_link):
	#data = open('1.mp3', 'rb').read()
	# print("ok download_link")
	request = requests.get(download_link)
	# print("ok request download_link")
	audio_file = io.BytesIO(request.content)
	sound = AudioSegment.from_mp3(audio_file)
	dst = "test1.wav"
	sound.export(dst, format="wav")
	r = sr.Recognizer()
	with sr.WavFile("test1.wav") as source:
		audio = r.record(source)
	
	audio_output=r.recognize_google(audio)
	print("Transcription: " + audio_output)
	return audio_output

# print(file_list_1)
# input("")
def clean_up():
	try:
		os.system("rm -rf /tmp/*")
		os.system("rm -rf rm -rf __pycache__/")
		# os.system("rm geckodriver.log")

	except:
		pass






	#starting_tasks()

##############################################################


def read_current_l0g():
	final_msg=''
	with open(l05_00,'r') as file:
		lines = file.readlines()
		for i in lines:
			final_msg=final_msg + i
	return final_msg
############################################################################



def save_succed(logg):
	with open("Wsucced_nord_xxxx",'a') as fw:
		fw.write(logg[0]+":"+logg[1]+"\n")

def save_succed_final(logg):
	with open("ready_Wsucced_nord_xxxx",'a') as fw:
		fw.write(logg+"\n")

###############################################################################################




###############################################################################################
def lets_play(l0g):
	try:
		width ,height=cnf_bvb.resolution_func()
#		print("OPEN DISPLAY  WEB-SITE ...... ",end='',flush=True)
# size=(width,height)
		# display = Display(visible=1,size=(width,height)).start()
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))

	except Exception as error:
		print(str(error))
		exit(0)
	
	print("OPEN AND VISITE WEB-SITE ...... ",end='',flush=True)
	time.sleep(1)
	try:
		sz=height+","+width
		# print(sz)

		driver = drive_md.build_driver(sz)
		driver.maximize_window()
		# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
		# driver.set_page_load_timeout(79)
		# driver.set_page_load_timeout(79)
		ads_class(driver,l0g)
		# lines=read_current_l0g()
		# cnf_bvb.send_msg(str(lines))
		
	except Exception as error:
		print(str(error))
		# input('')

	# print("CHECK THE getLink_button WEB-SITE ...... ",end='')


	try:
		print("Close Firefox ...... ",end='')
		driver.quit()

		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
		time.sleep(1)
	except:
		pass
	try:
		print("Close Display ...... ",end='')
		display.stop()
		print(emoji.emojize("Ok "' :check_mark_button: :alien:'))
	except:
		pass


#####################################

def init_fire():
	print("############################################################")
	print("INIT TASKS ..... ", end='')
	try:
		os.system("ps aux | grep -i chrome | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#
		os.system("ps aux | grep -i openvpn | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xephyr | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i chromedriver | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("ps aux | grep -i Xvfb | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		os.system("rm -rf /tmp/.*") 
		time.sleep(5)
		print(" OK !!!")
		#os.system("ps aux | grep -i firefox | awk '{print $2}'|xargs kill -9 > /dev/null 2>&1")
		#print("############################################################")
	except:
		print(" NO  some_Error init_fire")
###################################################################################################


def stage_1():
	try:
		#print (urls_BVB)
		os.system("rm -rf /tmp/.*")
		os.system("rm l05_00 ") 
		# os.system("clear && sleep 1") 
		print ( "-------------------------------------------------------")
		print(emoji.emojize("Website    : "+urls_BVB+' :check_mark_button: :alien:'))
		# print(emoji.emojize("Resolution : "+random_display_chose+' :check_mark_button: :alien:'))
		#####TO DO PRINT ONLY THE SYSTEM
		#print(width+"x"+height)
		print("System     : "+sys_use_agent)
		print ( "-------------------------------------------------------")

	except Exception as error:
		print (str(error))

###############################################################################################
l05_00='l05_00'
def append_to_l0g(text_add):
	with open(l05_00,'a') as fw:
		fw.write(text_add+"\n")

	



#################################"MAIN STARTING"##############################
def ads_class(driver,l0g):
	action = ActionChains(driver)
	user_arr_info=t00l.generate_name_add()


	# /html/body/div/div[2]/div
	try:
		driver.get(urls_BVB)
		print("https://xhamsterlive.com/adel_love")
		driver.set_page_load_timeout(30)
		# input("https://xhamsterlive.com/rich_peach")
		# driver.get("https://webglreport.com/")
		# time.sleep(3)
		SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[2]/div[1]/div/div[2]/div[1]/button')))
		action.move_to_element(SUCCESS_MSG_BUTTON)
		action.perform()
		print("peform")
		SUCCESS_MSG_BUTTON.click()
		time.sleep(3)
		print('button click')
		# //*[@id="body"]/div[3]/div[1]/header/div/div/nav[2]/div[2]/a[1]/span[2]
		# //*[@id="body"]/div[3]/div[2]/div[2]
		try:
			SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[3]/div[2]/div[2]')))
			SUCCESS_MSG_BUTTON.click()
			print('Cookies click')
			
		except Exception as e:
			print("no Cookies")

		SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[3]/div[1]/header/div/div/nav[2]/div[2]/a[1]/span[2]')))
		SUCCESS_MSG_BUTTON.click()
		print('button singup')
		time.sleep(3)
		# sign_up_input_login
		SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'sign_up_input_login')))
		SUCCESS_MSG_BUTTON.click()
		SUCCESS_MSG_BUTTON.send_keys(user_arr_info[5],Keys.TAB,user_arr_info[0],Keys.TAB,"baba123A*")
		print('READY TO KILL bCAOTCHA singup')
		time.sleep(3)
		SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'sign_up_input_login')))
		SUCCESS_MSG_BUTTON.click()
		SUCCESS_MSG_BUTTON.clear()
		SUCCESS_MSG_BUTTON.send_keys(user_arr_info[5],Keys.TAB,user_arr_info[0],Keys.TAB,"baba123A*")
		# recaptcha-anchor-label
		SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.ID, 'sign_up_irecaptcha')))
		print('REDY CAPTCHA')


		number_fra=driver.find_elements_by_tag_name("iframe")
		iframes = driver.find_elements_by_xpath("//iframe")
		print(str(len(iframes)))
		print('READY TO KILL bCAOTCHA singup')
		# time.sleep(3)

		try:
			print("cccccc")
			for index , iframe in enumerate(iframes):
				yhio=iframe.get_attribute('title')
				print(str(index)+" -- "+iframe.get_attribute('title'))
				if "reCAPTCHA" in yhio :
					driver.switch_to.frame(index)
					time.sleep(3)
					print("SWITCH TO : "+yhio)
					try:
						
						singup_green_button=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-anchor"]')))
						singup_green_button.click()
						print("CHECK SUCCESS  ")
						driver.switch_to.default_content()
						time.sleep(3)
						iframes = driver.find_elements_by_xpath("//iframe")
						print(str(len(iframes)))
						for index , iframe in enumerate(iframes):
							yhio=iframe.get_attribute('title')
							print(str(index)+" -- "+iframe.get_attribute('title'))
							print("SWITCH TO challenge : "+yhio)
							if "challenge" in yhio :

								driver.switch_to.frame(index)
								time.sleep(3)
								try:
									singup_green_button=WebDriverWait(driver, 18).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-audio-button"]')))
									singup_green_button.click()
									print("audio-source clicked !!!!!!!!")
									time.sleep(3)
									try:
										eto_firstName=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'audio-source')))
										download_link = eto_firstName.get_attribute('src')
										print(download_link)
										audio_output= audio_fonction(download_link)
										text_cap=WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID,'audio-response')))
										text_cap.send_keys(audio_output)
										time.sleep(2)
										text_cap.send_keys(Keys.ENTER)
									except Exception as e:
										print("NO ERROR MESSAGE ")


								except Exception as e:
									print("NO  recaptcha  ",e)
									driver.switch_to.default_content()
									time.sleep(3)
									# input("fix")





						driver.switch_to.default_content()
						time.sleep(5)
						SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[2]/div[1]/div/div[2]/div[1]/div[1]/form/div[5]/button')))
						SUCCESS_MSG_BUTTON.click()

						# singup_green_button=WebDriverWait(driver, 18).until(EC.presence_of_element_located((By.XPATH, '//*[@id="recaptcha-audio-button"]')))
						# singup_green_button.click()
						# //*[@id="body"]/div[2]/div[1]/div/div[2]/div[1]/div[1]/form/div[5]/button
						print("SING-UP FINISHED !!!!!!!!")
						driver.switch_to.default_content()
						# //*[@id="body"]/div[3]/div[1]/div[2]/span/a[2]
						time.sleep(5)
						SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[3]/div[1]/div[2]/span/a[2]')))
						print("LETS ACTIVATED  !!!!!!!!",user_arr_info[0])
						print('hm... hm')
						SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div[1]/div[3]/button')))
						SUCCESS_MSG_BUTTON.click()
						print('hm... FAVORIT')

						driver.get("https://xhamsterlive.com/rozana_holmes")
						SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="body"]/div[3]/div[1]/div[2]/span/a[2]')))
						print("LETS ACTIVATED  !!!!!!!!",user_arr_info[0])
						print('hm... hm')
						SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[2]/div[3]/div/div/div/div[2]/div/div[1]/div/div[3]/div/div[1]/div[3]/button')))
						SUCCESS_MSG_BUTTON.click()

						save_hamster.insert_to_db(user_arr_info[0])


						# 
						time.sleep(5)
						break
						# link_activ=activation_link.gather_acces(user_arr_info[0])
						# # l_a=link_activ.split()
						# print(link_activ)
						# print(str(link_activ))
						# driver.get(link_activ)
						# time.sleep(5)

						# break
					except Exception as e:
						print("NO  0000 recaptcha  ",e)
						# reefree(driver)
		except :
			print("main captcha error")







		# input("oh")
		# try:

		# 	iframes = driver.find_elements_by_xpath("//iframe")
		# 	# print(str(imges_ifam))
		# 	driver.switch_to.frame(0)
		# 	time.sleep(2)

		# 	SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/span')))
		# 	print("peform1 : "+SUCCESS_MSG_BUTTON.text)
		# 	do0n="peform1 : "+SUCCESS_MSG_BUTTON.text+" \n"
		# 	print(do0n)
		# 	# cnf_bvb.alias_send_msg(SUCCESS_MSG_BUTTON.text)
		# 	time.sleep(7)
			
		# except:
		# 	do0n="peform1 : "
		# 	imges_ifam = driver.find_elements_by_xpath("//img")
		# 	# print(str(imges_ifam))
		# 	for i in imges_ifam :
		# 		# print(i.get_attribute("alt"))
		# 		do0n=do0n+ " | "+i.get_attribute("alt")
		# 	print(" "+do0n)
		# 	time.sleep(7)
		# 	pass
		# driver.switch_to.parent_frame()
		# append_to_l0g(do0n)
		# # input('read2')
		# # driver.refresh()
		# driver.get(urls_BVB)
		# time.sleep(2)
		# try:
		# 	iframes = driver.find_elements_by_xpath("//iframe")
		# 	# print(str(imges_ifam))
		# 	driver.switch_to.frame(0)
		# 	time.sleep(2)
		# 	SUCCESS_MSG_BUTTON=WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '/html/body/div/div[2]/div/span')))
		# 	print("peform2 : "+SUCCESS_MSG_BUTTON.text)
		# 	do0n="peform2 : "+SUCCESS_MSG_BUTTON.text
		# 	print(do0n)
		# 	# cnf_bvb.alias_send_msg(SUCCESS_MSG_BUTTON.text)
		# 	time.sleep(7)
				
		# except:
		# 	do0n="peform2 : "
		# 	imges_ifam = driver.find_elements_by_xpath("//img")
		# 	# print(str(imges_ifam))
		# 	for i in imges_ifam :
		# 		# print(i.get_attribute("alt"))
		# 		do0n=do0n+ " | "+i.get_attribute("alt")
		# 	print(" "+do0n)
		# 	time.sleep(7)
		# 	pass
		# driver.switch_to.parent_frame()
		# append_to_l0g(do0n)
		# append_to_l0g("VISITE WEB-SITE [ 2 ] : [ +second_2_visit+]  OK")
		# lines=read_current_l0g()
		# cnf_bvb.send_msg(str(lines))
		# time.sleep(7)
		driver.delete_all_cookies()
		print("Remove Cookies")

	except Exception as error:
		print (str(error))	
def starting_tasks(l0g):
	width ,height=cnf_bvb.resolution_func()
	moz_wid="--width="+str(width)
	moz_hig="--height="+str(height)

######################USER AGENT ###################################################

	try:
		stage_1()### CLEAR
		# print(l0g)
		# os.system("curl -sx socks5://127.0.0.1:9050 ifconfig.co | grep -oP '(?<=Your IP</span>: ).*(?=</span>)'")
		mod_vpn2.fnc_vpn ()
		cnf_bvb.alias_send_msg("starting chom")
		# mod_vpn.renew_connection()
		# serv,ops=mod_driver.build_driver(width ,height)
		lets_play(l0g)
		clean_up()
		

	except Exception as error:
		print (str(error))


def read_current_list_vpn():
	with open(file_list_1,'r') as file:
		lines = file.readlines()
	return lines







def save_successed_bin(card_numer):
	# l_bin=read_the_last_bin()
	print(card_numer)
	# new_bin=int(l_bin)+1
	# binani=str(new_bin)
	#################
	with open("succed_bin","a") as file_bin:
		file_bin.write(card_numer+"\n")
















def main():
	os.system("rm -rf /tmp/.*")
	starting_tasks("l0g:l0g")



if __name__ == '__main__':

	main()


# begaining_loop()