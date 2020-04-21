import pdb
import pickle
with open('progestin.pickle', 'rb') as handle:
	name_progestin_map = pickle.load(handle)
	new_map = {}
	for key, item in name_progestin_map.items():
		new_map[key.lower()] = item

progestins = pickle.load(open('progestin.pickle', 'rb'))
alternates = pickle.load(open('alternates.pickle', 'rb'))

pdb.set_trace()
for name in alternates.keys():
	name_lower = name.lower()
	progestin = progestins[name_lower]
	generic_names = alternates[name]
	if len(generic_names):
		generic_names = [x.strip().lower() for x in generic_names.split(',')]
		for generic_name in generic_names:
			progestins[generic_name] = progestin

with open('progestin.pickle', 'wb') as handle:
	pickle.dump(progestins, handle, protocol=pickle.HIGHEST_PROTOCOL)

