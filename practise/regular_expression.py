import re
str1="quick brown fox"
pattern=r"brown"
result_search=re.search(pattern,str1)
if result_search:
    print(" search pattern exists in"+str1)
else:
    print("search pattern does not exists in"+str1)
result_match=re.match(pattern,str1)
if result_match:
    print(" match pattern exists in"+str1)
else:
    print("match pattern does not exists in"+str1)
replcament="red"
result_sub=re.sub(pattern,replcament,str1)
print("replaced text is"+result_sub)
