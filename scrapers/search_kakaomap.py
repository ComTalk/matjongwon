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

def save_wo_kakaomap(save_filename, contents, index):

	naver_score = contents[index]['score']

	#del content['score']
	contents[index]['score'] = {}
	contents[index]['score']['navermap'] = naver_score
	contents[index]['score']['kakaomap'] = ""

	naver_review_link = contents[index]['reviews']

	#del content['reviews']
	contents[index]['reviews'] = {}
	contents[index]['reviews']['navermap'] = naver_review_link
	contents[index]['reviews']['kakaomap'] = ""

	with open(save_filename, 'r', encoding='utf-8') as file:
			file_data = json.load(file)

	file_data.append(contents[index])

	with open(save_filename, 'w', encoding='utf-8') as json_file:
		json.dump(file_data, json_file , ensure_ascii=False)

	# with open(save_filename, 'w', encoding='utf-8') as json_file:
	# 	json.dump(contents, json_file , ensure_ascii=False)

warnings.simplefilter("ignore")

datafile = "data/new_collect/naver_contents.json"
save_filename = "data/new_collect/naver_kakaomap_contents.json"

with open(datafile , encoding='utf-8') as f:
	naver_contents = json.load(f)

try :
	with open(save_filename, 'r', encoding='utf-8') as file:
		file_data = json.load(file)
except:
	with open(save_filename, mode='w', encoding='utf-8') as f:
		json.dump([], f)
		file_data = []

current_restaurant = len(file_data)

print('current length : {}'.format(current_restaurant))

if current_restaurant == 0:
	# initialize the file
	with open(save_filename, mode='w', encoding='utf-8') as f:
		json.dump([], f)


# combine_contents = []

kakaomap_path = "https://map.kakao.com/"

for index in range(current_restaurant, len(naver_contents)):

	content = naver_contents[index]

	print('current_restaurant number : {}'.format(index))

	restaurant_name = content['name']

	driver = webdriver.Edge(EdgeChromiumDriverManager().install())
	search_url = f'{kakaomap_path}?q={restaurant_name}'
	driver.get(search_url)
	driver.implicitly_wait(time_to_wait=3)
	time.sleep(0.5)

	try :
		place_list = driver.find_element(by=By.ID, value="info.search.place.list")
		place_elem = place_list.find_elements(By.TAG_NAME, value="li")[0]
	except:
		print('{} is not avaliable in kakaomap'.format(restaurant_name))
		time.sleep(1)
		driver.close()
		save_wo_kakaomap(save_filename, naver_contents, index)
		continue

	IsMatched = False

	for place_elem in place_list.find_elements(By.TAG_NAME, value="li"):

		try :
			address = place_elem.find_element(
				by=By.CLASS_NAME, value="addr"
			).text.split("\n")[0]
		except:
			print('invalid address')
			# save_wo_kakaomap(save_filename, naver_contents, index)
			continue

		try:

			daum_address = address.split(' ')[1]
			naver_address = content['address'].split(' ')[1]

			if daum_address != naver_address:
				raise Exception('no match region')

		except:
			continue


		try :
			category = [place_elem.find_element(
						by=By.CLASS_NAME, value="subcategory"
					).text]
		except:
			print('no category')
			category = []

		try:
			operation_time = [place_elem.find_element(
					by=By.CLASS_NAME, value="openhour"
				).text.split("\n")[-1]]

		except:

			print('no opening hours')
			operation_time = []

		score = place_elem.find_element(
			by=By.CLASS_NAME, value="rating"
		).text.split()[0]
		review_link = place_elem.find_element(
			by=By.CLASS_NAME, value="numberofscore"
		).get_attribute("href")

		place_elem.find_element(by=By.CLASS_NAME, value="moreview").send_keys(
					Keys.ENTER
				)
		driver.switch_to.window(driver.window_handles[-1])

		menu = ""

		try:
			menu_element = driver.find_element(
				by=By.CLASS_NAME, value="list_menu"
			)
			menu_name_list = menu_element.find_elements(
				by=By.CLASS_NAME, value="loss_word"
			)
			menu_price_list = menu_element.find_elements(
				by=By.CLASS_NAME, value="price_menu"
			)
			for menu_name, menu_price in zip(menu_name_list, menu_price_list):
				menu += "{} : {} | ".format(menu_name.text, menu_price.text)
		except:
			print("no menu provided")
			menu = ""

		driver.close()
		driver.switch_to.window(driver.window_handles[0])

		naver_score = content['score']

		#del content['score']
		content['score'] = {}
		content['score']['navermap'] = naver_score

		if is_number(score):
			content['score']['kakaomap'] = score
		else:
			content['score']['kakaomap'] = ""

		naver_review_link = content['reviews']

		#del content['reviews']
		content['reviews'] = {}
		content['reviews']['navermap'] = naver_review_link
		content['reviews']['kakaomap'] = review_link

		if len(content['category']) == 0:
			content['category'] = category

		if len(content['opening_hours']) == 0:
			content['opening_hours'] = operation_time

		if content['menu'] == "":
			content['menu'] = menu

		# combine_contents.append(content)

		time.sleep(1)

		driver.close()

		# print(content)

		IsMatched = True

		break

	if IsMatched == True:
		# with open(save_filename, 'w', encoding='utf-8') as json_file:
		# 	json.dump(naver_contents, json_file , ensure_ascii=False)

		with open(save_filename, 'r', encoding='utf-8') as file:
			file_data = json.load(file)

		file_data.append(content)

		with open(save_filename, 'w', encoding='utf-8') as json_file:
			json.dump(file_data, json_file , ensure_ascii=False)

	else:
		save_wo_kakaomap(save_filename, naver_contents, index)

	
# with open(save_filename, 'w', encoding='utf-8') as json_file:
# 		json.dump(naver_contents, json_file , ensure_ascii=False)