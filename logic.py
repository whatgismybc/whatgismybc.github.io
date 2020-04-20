import pickle
import pdb

def find_closest_name(submitted):
	with open('data/progestin.pickle', 'rb') as handle:
		name_progestin_map = pickle.load(handle)
	names = name_progestin_map.keys()
	names = [x.lower() for x in names]
	submitted = submitted.lower()
	# TODO: add some sort of logic for typos
	for name in names:
		if submitted in name:
			return name 
	return "none"

def get_progestin_generation(progestin_name):
	progestin_name = progestin_name.lower()
	progestin_generation_map = {"levonorgestrel": 2,"desogestrel": 3, "norethindrone": 1, "drospirenone": 4, 
							   "medroxy progesterone": 1, "medroxyprogesterone": 1, "norethindrone acetate": 1, 
							   "norgestrel": 2, "dienogest": 4, "etonogestrel": 3, "norgestimate": 3, "ethynodiol diacetate": 1}
	return progestin_generation_map[progestin_name]


def get_generation(submitted):
	# see if name is in the name_progestin map
	# go from progestin map to generation
	with open('data/progestin.pickle', 'rb') as handle:
		name_progestin_map = pickle.load(handle)
	name = find_closest_name(submitted)
	if name == "none":
		return False

	progestin = name_progestin_map[name]
	g = get_progestin_generation(progestin)
	g_num_to_words = {1: "first generation" , 2:"second generation", 3: "third generation", 4: "fourth generation"}
	return g_num_to_words[g]

def get_generation_desc(g, submitted):
	name = find_closest_name(submitted) 
	generation_descr_map = {"first generation": 'derived from testosterone. These are highly \'progestational,\' \
											  meaning good at preventing the HPG cascade and preventing ovulation.',
						  "second generation": 'derived from testosterone. They are known to increase a person\’s risk of experiencing testosterone-related \
						  						side effects such as decreasing good cholesterol (HDL), \
						  						increasing weight gain, and causing acne and hair growth in places you don\’t want hair. \
						  						These effects are usually offset by the estrogen in these pills, but some women still experience these types of side effects.',
						  "third generation": 'derived from testosterone. Molecules in this generation of progestins have been manipulated in a way \
						  					    that decreases the pesky testosterone-related side effects (weight gain, acne, hairiness). These \
						  					    come with a higher risk of blood clots than second-generation pills do.'}
	fourth_gen_descr_map = {"dienogest": 'derived from testosterone (T). However, unlike the others, this actually blocks \
										testosterone receptors, making it so testosterone can\’t be \'read\' by the cells \
										in your body. So even though it\’s made from testosterone, \
										it\’s anti-androgenic. This means fewer breakouts and less weight gain. This generation \
										of progestin (including drospirenone, another fourth generation pill) is also really good \
										for people who have problems with bleeding between periods.', 
							"drospirenone": 'derived from a diuretic called spironolactone. Of all the progestins, \
											this one has the most potent anti-androgen effects. \
											It often promotes clearer skin and can promote initial weight loss because it \
											exerts effects that can decrease water retention caused by estrogen.'}

	if 'fourth' in g:	
		descr = fourth_gen_descr_map[submitted]				  					    
	else:
		descr = generation_descr_map[g]		

	return descr 

def get_side_effects(g):
	return "x"