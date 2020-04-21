import re
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pdb
import pandas as pd
import os
import pickle
import numpy as np
from selenium.webdriver.chrome.options import Options
from tqdm import tqdm
import time
import pickle


def get_progestin_name(text):
	text = text.lower()
	progestins = ["levonorgestrel","desogestrel", "norethindrone", 
	"drospirenone", "medroxy progesterone", "medroxyprogesterone", "norethindrone acetate", 
	"norgestrel", "dienogest", "etonogestrel", "norgestimate", "ethynodiol diacetate"]
	for progestin in progestins:
		if progestin in text:
			return progestin
	return 'none'

def get_progestin_generation(progestin_name):
	progestin_name = progestin_name.lower()
	progestin_generation_map = {"levonorgestrel": 2,"desogestrel": 3, "norethindrone": 1, "drospirenone": 4, 
							   "medroxy progesterone": 1, "medroxyprogesterone": 1, "norethindrone acetate": 1, 
							   "norgestrel": 2, "dienogest": 4, "etonogestrel": 3, "norgestimate": 3, "ethynodiol diacetate": 1}
	return progestin_generation_map[progestin_name]


def get_name(driver):
	name = driver.find_elements_by_class_name("pronounce-title")
	if len(name):
		name = name[0].text
	else:
		content_box = driver.find_elements_by_class_name("content-box")
		if len(content_box) == 0:
			content_box = driver.find_elements_by_class_name("contentBox")
		name = content_box[0].find_elements_by_tag_name('h1')[0].text
	return name

def get_generic_name(driver):
	# handle when there is no drug-subtitle class 
	generic_elements = driver.find_elements_by_class_name('drug-subtitle')
	if len(generic_elements):
		generic_elements = generic_elements[0].find_elements_by_tag_name('a')
		if len(generic_elements):
			generic_name = generic_elements[0].text
		else:
			generic_name = driver.find_elements_by_class_name('drug-subtitle')[0].text[14:]
			generic_name = generic_name.split(' ')[0]
		return generic_name
	else:
		generic_elements = driver.find_elements_by_class_name('contentBox')[0]
		generic_name = generic_elements.find_elements_by_tag_name('p')[0].text
		return generic_name


def get_alternate_names(driver):
	alternate_names = ""
	alternate_elements = driver.find_elements_by_class_name('drug-subtitle')
	if len(alternate_elements):
		alternate_names = alternate_elements[0].find_elements_by_tag_name('i')
		if len(alternate_names):
			alternate_names = alternate_names[0].text
	return alternate_names

# get generic name from drug subtitle
# get other brand names from drug subtitle
driver_path ='/Users/divyas/Documents/real_docs/G2/chromedriver_80'
driver = webdriver.Chrome(driver_path)

collect_links = True
if os.path.exists('drug_links.npy'):
	all_links = np.load('drug_links.npy')
	collect_links = False

if collect_links == True:
	base_url = "https://www.drugs.com/condition/contraception.html?page_number="
	n_pages = 11
	all_links = []
	for i in range(1, n_pages+1):
		driver.get(base_url + str(i))
		elements = driver.find_elements_by_class_name("condition-table__drug-name__link")
		links = [x.get_attribute('href') for x in elements]
		all_links.extend(links)
	np.save('drug_links.npy', all_links)

print("[X] Collected drug names")

name_progestin_map = {}
name_generic_name_map = {}
name_alternates_map = {}
if os.path.exists('progestin.pickle'):
	with open('progestin.pickle', 'rb') as handle:
		name_progestin_map = pickle.load(handle)

	with open('generics.pickle', 'rb') as handle:
		name_generic_name_map = pickle.load(handle)

	with open('alternates.pickle', 'rb') as handle:
		name_alternates_map = pickle.load(handle)

for i, link in enumerate(all_links):
	if i < 236: 
		continue
	print(link)
	driver.get(link)
	name = get_name(driver)
	name = name.lower()

	if name in name_progestin_map or name == "Copper":
		print("Done with: ", name)
		continue


	generic_name = get_generic_name(driver)
	alternate_names = get_alternate_names(driver)
	progestin_name = get_progestin_name(generic_name)

	name_progestin_map[name] = progestin_name
	name_generic_name_map[name] = generic_name
	name_alternates_map[name] = alternate_names

	with open('progestin.pickle', 'wb') as handle:
		pickle.dump(name_progestin_map, handle, protocol=pickle.HIGHEST_PROTOCOL)

	with open('generics.pickle', 'wb') as handle:
		pickle.dump(name_generic_name_map, handle, protocol=pickle.HIGHEST_PROTOCOL)

	with open('alternates.pickle', 'wb') as handle:
		pickle.dump(name_alternates_map, handle, protocol=pickle.HIGHEST_PROTOCOL)


print("[X] Scraped drug info")

pdb.set_trace()