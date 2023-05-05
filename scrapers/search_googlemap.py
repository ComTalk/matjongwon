import json
import time
import warnings
from collections import defaultdict

import pandas as pd
from tqdm import tqdm
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

seoul_gu_list = [
		"마포구",
		"서대문구",
		"은평구",
		"종로구",
		"중구",
		"용산구",
		"성동구",
		"광진구",
		"동대문구",
		"성북구",
		"강북구",
		"도봉구",
		"노원구",
		"중랑구",
		"강동구",
		"송파구",
		"강남구",
		"서초구",
		"관악구",
		"동작구",
		"영등포구",
		"금천구",
		"구로구",
		"양천구",
		"강서구",
	]

def is_number(n):
    try:
        float(n)   # Type-casting the string to `float`.
                   # If string is not a valid `float`, 
                   # it'll raise `ValueError` exception
    except ValueError:
        return False
    return True

warnings.simplefilter("ignore")

datafile = "data/new_collect/naver_kakaomap_contents.json"

with open(datafile , encoding='utf-8') as f:
	contents = json.load(f)

save_filename = "data/new_collect/final_contents.json"

with open(save_filename, 'r', encoding='utf-8') as file:
	file_data = json.load(file)

# try:
# 	with open(save_filename, 'r', encoding='utf-8') as file:
# 		file_data = json.load(file)

# except:
# 	with open(save_filename, mode='w', encoding='utf-8') as f:
# 		json.dump([], f)
# 		file_data = []


current_restaurant = len(file_data)

print('current length : {}'.format(current_restaurant))

# if current_restaurant == 0:
# 	# initialize the file
# 	with open(save_filename, mode='w', encoding='utf-8') as f:
# 		json.dump([], f)

# combine_contents = []

# googlemap_path = "https://www.google.co.kr/maps"

# for index in range(current_restaurant, len(contents)):

# 	# content = naver_contents[index]

# 	print('current_restaurant number : {}'.format(index))

# 	content = contents[index]

# 	# print(content)

# 	# if index == 2: 
# 	# 	break

# 	restaurant_name = content['name']

# 	# search restaurant

# 	driver = webdriver.Edge(EdgeChromiumDriverManager().install())
# 	search_url = f'{googlemap_path}?q={restaurant_name}'
# 	driver.get(search_url)
# 	driver.implicitly_wait(time_to_wait=3)
# 	time.sleep(0.5)

# 	try:
# 		driver.find_element_by_xpath('//*[@aria-label="Reject all"]').click()
# 		driver.implicitly_wait(time_to_wait=10)
# 	except:
# 		print('no consent')
# 	finally:
# 		time.sleep(3)

# 	# address 
# 	address_list = driver.find_elements_by_xpath(".//div[@class='Io6YTe fontBodyMedium']")
# 	address = ""
# 	latitude = ""
# 	longitude = ""
# 	score = ""
# 	review_link = ""

# 	IsMatched = False

# 	# print('address : {}'.format(address_list))

# 	if len(address_list) != 0:

# 		for item in address_list:

# 			try:
# 				google_address = item.text.split(' ')[1]
# 				naver_address = content['address'].split(' ')[1]

# 				if google_address == naver_address:
# 					address = item.text
# 					IsMatched = True
# 					break

# 			except:
# 				continue

# 		if IsMatched == False:
# 			pass

# 		else:

# 			time.sleep(3)

# 			try:
# 				current_url = driver.current_url
# 				# time.sleep(1)
# 				start_index = current_url.index('@')
# 				tmp_coordinates = current_url[start_index+1:].split(',')
# 				latitude = tmp_coordinates[0]
# 				longitude = tmp_coordinates[1]
# 			except:
# 				print('cannot find coordinates')
# 				# driver.close()
# 				# continue

# 			# review 
# 			try:
# 				# score = driver.find_elements_by_xpath(".//div[@class='fontDisplayLarge']")[0].text
# 				score_element = driver.find_elements_by_xpath(".//span[@class='ceNzKf']")
# 				value = score_element[0].get_attribute("aria-label")
# 				value = value.replace('stars', '')
# 				value = value.replace(' ', '')

# 				if is_number(value):
# 					score = value
# 			except:
# 				print('cannot find score')

# 			#print(score)

# 			# review link
# 			try:
# 				# driver.find_elements_by_xpath(".//button[@class='HHrUdb fontTitleSmall rqjGif']")[0].click()
# 				# time.sleep(2)
# 				# review_link = driver.current_url

# 				review_button = driver.find_element(By.XPATH, "//div[@jsaction='pane.rating.moreReviews']")
# 				review_button.click()

# 				time.sleep(2)
# 				review_link = driver.current_url
					
# 			except:
# 				print('cannot click review')



# 	else:
# 		restaurant_list = driver.find_elements_by_xpath(".//div[@class='Nv2PK THOPZb CpccDe']")
		

# 		for item in restaurant_list:

# 			try:
# 				a_element = item.find_element_by_tag_name("a")
# 				# href = item.get_attribute("href")
# 				href = a_element.get_attribute("href")

# 				# Get the current window handle
# 				current_window_handle = driver.current_window_handle

# 				# Open the link in a new tab
# 				driver.execute_script("window.open('" + href + "', '_blank');")

# 				for handle in driver.window_handles:
# 				    if handle != current_window_handle:
# 				        driver.switch_to.window(handle)
# 				        break
# 			except:
# 				continue

# 			# address 
# 			sub_add_list = driver.find_elements_by_xpath(".//div[@class='Io6YTe fontBodyMedium']")
# 			# address = ''

# 			# print('address : {}'.format(sub_add_list))

# 			for item in sub_add_list:

# 				try:

# 					google_address = item.text.split(' ')[1]
# 					naver_address = content['address'].split(' ')[1]

# 					if google_address == naver_address:
# 						address = item.text
# 						IsMatched = True
# 						break
# 				except:
# 					continue

# 			if IsMatched == False:
# 				driver.close()
# 				driver.switch_to.window(driver.window_handles[0])
# 				continue

# 			else:

# 				# print('before : {}'.format(driver.current_url))

# 				time.sleep(3)

# 				# print('after : {}'.format(driver.current_url))

# 				try:
# 					current_url = driver.current_url
# 					start_index = current_url.index('@')
# 					tmp_coordinates = current_url[start_index+1:].split(',')
# 					latitude = tmp_coordinates[0]
# 					longitude = tmp_coordinates[1]
# 				except:
# 					print('cannot find coordinates')
# 					# driver.close()
# 					# continue

# 				# review 
# 				try:
# 					# score = driver.find_elements_by_xpath(".//div[@class='fontDisplayLarge']")[0].text
# 					score_element = driver.find_elements_by_xpath(".//span[@class='ceNzKf']")
# 					value = score_element[0].get_attribute("aria-label")
# 					value = value.replace('stars', '')
# 					value = value.replace(' ', '')

# 					if is_number(value):
# 						score = value
# 				except:
# 					print('cannot find score')

# 				# review link
# 				try:
# 					# driver.find_elements_by_xpath(".//button[@class='HHrUdb fontTitleSmall rqjGif']")[0].click()
# 					# time.sleep(2)
# 					# review_link = driver.current_url

# 					review_button = driver.find_element(By.XPATH, "//div[@jsaction='pane.rating.moreReviews']")
# 					review_button.click()

# 					time.sleep(2)
# 					review_link = driver.current_url

# 				except:
# 					print('cannot click review')

# 					# driver.find_elements_by_xpath(".//button[@class='HHrUdb fontTitleSmall rqjGif']")[0].click()
# 					# time.sleep(2)
# 					# review_link = driver.current_url

# 				driver.close()
# 				driver.switch_to.window(driver.window_handles[0])
# 				break


# 	driver.close()

# 	content['score']['googlemap'] = score
# 	content['reviews']['googlemap'] = review_link
# 	content['coordinates'] = {"latitude" : latitude, "longitude" : longitude}


# 	with open(save_filename, 'r', encoding='utf-8') as file:
# 		file_data = json.load(file)

# 	file_data.append(content)

# 	with open(save_filename, 'w', encoding='utf-8') as json_file:
# 		json.dump(file_data, json_file , ensure_ascii=False)

# 	print(content)