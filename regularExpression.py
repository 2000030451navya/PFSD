import re
str1 = " I'm Navya, studying in Kl University"\
       "My goal is to study MS in UK "\
       "I'm an Army,borahae."
matches1 = re.findall("in ", str1)
print(matches1)
matches2 = re.search("MS", str1)
print(matches2)
matches3= re.split(str1,"studying")
print(matches3)
matches4 = re.match(str1 ,"to ")
print(matches4)
