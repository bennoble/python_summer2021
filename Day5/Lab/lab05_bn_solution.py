import re

# open text file of 2008 NH primary Obama speech
with open("/Users/bennoble/Dropbox/Ben/GitHub/python_summer2021/Day5/Lecture/obama-nh.txt", "r") as f:
	obama = f.readlines()


## TODO: print lines that do not contain 'the' using what we learned
## (although you ~might~ think you could do something like
## [l for l in obama if "the" not in l]

nothe = [] 
for l in obama:
	if len(re.findall(r'\b[Tt]he\b', l)) == 0:
		nothe.append(l)
nothe
len(nothe)
# TODO: print lines that contain a word of any length starting with s and ending with e

se_patt = re.compile(r'\b[Ss][a-z]*e\b')
[l for l in obama if se_patt.findall(l)]

## TODO: Print the date input in the following format
## Month: MM
## Day: DD
## Year: YY
date = 'Please enter a date in the following format: 08.18.21'

date_list = re.split(r': |\.', date)

print(
"""
Month: {}
Day: {}
Year: {}
"""
.format(date_list[1],date_list[2],date_list[3])
)


### or (from Matt Dickenson)

pattern=re.compile(r'(\d*)\.(\d*)\.(\d*)')
x = pattern.search(date)
print("Month: {} \nDay: {} \nYear: {}".format(x.groups(0)[0],x.groups(0)[1],x.groups(0)[2]))

