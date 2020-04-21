# -*- coding: utf-8 -*-
import pickle
import pdb

import os
import pathlib
absolute_path = str(pathlib.Path().absolute())

def find_closest_name(submitted):
	with open(absolute_path + '/data/progestin.pickle', 'rb') as handle:
		name_progestin_map = pickle.load(handle)
	names = name_progestin_map.keys()
	names = [x.lower() for x in names]
	submitted = submitted.lower()
	# TODO: add some sort of logic for typos
	for name in names:
		if submitted in name:
			return name 
	return "none"

def get_progestin(name):
	with open(absolute_path + '/data/progestin.pickle', 'rb') as handle:
		name_progestin_map = pickle.load(handle)
	return name_progestin_map[name]

def get_progestin_generation(progestin_name):
	progestin_name = progestin_name.lower()
	progestin_generation_map = {"levonorgestrel": 2,"desogestrel": 3, "norethindrone": 1, "drospirenone": 4, 
							   "medroxy progesterone": 1, "medroxyprogesterone": 1, "norethindrone acetate": 1, 
							   "norgestrel": 2, "dienogest": 4, "etonogestrel": 3, "norgestimate": 3, "ethynodiol diacetate": 1}
	return progestin_generation_map[progestin_name]


def get_generation(submitted):
	# see if name is in the name_progestin map
	# go from progestin map to generation
	name = find_closest_name(submitted)
	g_words = None
	if name != "none":
		progestin = get_progestin(name)
		g = get_progestin_generation(progestin)
		g_num_to_words = {1: "first generation" , 2:"second generation", 3: "third generation", 4: "fourth generation"}
		g_words = g_num_to_words[g]
	return g_words

def get_advantages(progestin):
	advantages = {'norethindrone': 'an improved lipid profile and has been shown to be useful to women who experience depression on other oral contraceptive combinations',
				  'norethindrone acetate': 'potential benefits for women who experience migraines or nausea on other oral contraceptives',
				  'ethynodiol diacetate': 'potential benefits for women with endometriosis',
				  'levonorgestrel': 'having the lowest risk of blood clots compared to all other oral contraceptives',
				  'norgestrel': 'potential benefits in terms of preventing endometriosis',
				  'desogestrel': 'alleviating menstrual cramps, reduced risk of menstrual migrains, positive effects on lipids, and less weight gain than other oral contraceptives',
				  'norgestimate': 'being the only FDA-approved pill to help acne and little effect on lipids',
				  'drosperinone': 'potential reduction in PMS symptoms and acne'}
	return advantages[progestin]

def get_disadvantages(progestin):
	disadvantages = {'norethindrone': 'variable effects on acne',
					 'norethindrone acetate': 'variable effects on acne',
					 'ethynodiol diacetate': 'breakthrough bleeding (spotting)',
					 'levonorgestrel': 'negative effects on lipids and increased incidence of androgenic side effecs, such as acne',
					 'norgestrel': 'acne and weight gain',
					 'desogestrel': 'a higher risk of blood clots',
					 'norgestimate': 'a higher rate of headaches and reduced libido',
					 'drosperinone': 'an increased risk of blood clots and increase serum potassium levels'}
	return disadvantages[progestin]

def get_generation_desc(g, submitted):
	name = find_closest_name(submitted)
	progestin = get_progestin(name) 
	# get testosterone derivation
	fourth_gen_testosterone = {"dienogest": "derived from testosterone",
							 "drospirenone": "the only one that is not derived from testosterone, but rather from a diuretic called spironolactone"}
	testosterone_derived = {"first generation": 'derived from testosterone',
							"second generation": 'derived from testosterone',
							"third generation": 'derived from testosterone'}

	if 'fourth' in g:
		testosterone = fourth_gen_testosterone[progestin]
	else:
		testosterone = testosterone_derived[g]

	# get progestin specific side effects
	advantages, disadvantages = None, None
	advantages = get_advantages(progestin)
	disadvantages = get_disadvantages(progestin)

	# get side effects
	gen_se = None
	fourth_gen_side_effects = {"dienogest": "block testosterone receptors, making it so testosterone can’t be 'read' by the cells \
										in your body. So even though they're made from testosterone, \
										they're anti-androgenic. This means fewer breakouts and less weight gain. This generation \
										of progestin (including drospirenone, another fourth generation progestin) is also really good \
										for people who have problems with bleeding between periods", 
							"drospirenone": 'are derived from a diuretic called spironolactone. This generation of pills has the most potent anti-androgen effects. \
											They often promote clearer skin and can promote initial weight loss because it \
											exerts effects that can decrease water retention caused by estrogen'}
	side_effects = {"first generation": "are highly 'progestational,' \
											  meaning good at preventing the HPG cascade and preventing ovulation.",
						  "second generation": "are known to increase a person’s risk of experiencing testosterone-related \
						  						side effects such as decreasing good cholesterol (HDL), \
						  						increasing weight gain, and causing acne and hair growth in places you don’t want hair. \
						  						These effects are usually offset by the estrogen in these pills, but some women still experience these types of side effects",
						  "third generation": 'have been manipulated in a way \
						  					    that decreases the pesky testosterone-related side effects (weight gain, acne, hairiness). These \
						  					    come with a higher risk of blood clots than second-generation pills do'}

	if 'fourth' in g:	
		gen_se = fourth_gen_descr_map[progestin]				  					    
	else:
		gen_se = side_effects[g]		

	return testosterone, progestin, advantages, disadvantages, gen_se 

def get_side_effects(g):
	return "x"
