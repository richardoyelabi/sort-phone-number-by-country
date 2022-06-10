import phonenumbers
import pycountry
from phonenumbers.phonenumberutil import region_code_for_country_code
from phonenumbers.phonenumberutil import region_code_for_number
import re

file_name = input ("File name: ")

file = open (file_name, "r")
read = file.readlines()

dict = {}
count = 0
line_count = False

for line in read:
	if (line_count == True):
		line_count = not line_count
		continue
	if (re.search("^TEL;CELL:\+", line)):
		count += 1
		number = line[9:]
		pn = phonenumbers.parse(number)
		country = pycountry.countries.get(alpha_2=region_code_for_number(pn))
		if not (country.name in dict):
			dict[country.name] = 0
		dict[country.name] = dict[country.name] + 1
		line_count = not line_count
	
me = dict

mlis = list(me.values())
memax = max(mlis)
memin= min(mlis)
ndic = {}
for val in range(memax, memin- 1, -1):
	for item in me.keys():
		if me[item] == val:
			ndic[item] = val

for country, viewers in ndic.items():
		print (country + ": " + str(viewers))

nofc = len(list(ndic.keys()))

print ("")
print ("Total: " + str (count))
print("Number of Countries:" + str(nofc))
		
file.close()