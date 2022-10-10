import re

with open(r"C:\WORK\PROJECTS\Opensanctuary.org\canada_city_province_negative_list.txt", 'r') as f:
	city_list = list(f)
	city_list = [re.sub('\n','',city) for city in city_list]
	city_list = ['\"' + city + '\"' if len(city.split()) > 1 else city for city in city_list]

with open(r"C:\WORK\PROJECTS\Opensanctuary.org\us_canada_city_state_province_negative_list_output.txt", 'w') as f:
	for city in city_list:
		f.write("%s\n" % city)

print(city_list)