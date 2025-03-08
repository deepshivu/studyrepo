#concatenate example
str1="hello"
str2="world"
print(str1+" "+str2)

#check length of the string
str3="Deepika is amazing"
print("length of " + str3 +str(len(str3)))

#uppercase lowercase
str3_upper=str3.upper()
str3_lower=str3.lower()
print("lowercase :"+str3_lower)
print("uppercase :"+str3_upper)

#replace string
str3_replace=str3.replace("amazing","fantastic")
print("replaced text is"+str3_replace)

#split strings
str3_split=str3.split(" ")
print("split text is"+ str(str3_split))

#strip spaces
str3_strip=str3.strip()
print("strip string is"+str3_strip)

#substring example
substring="is"
if substring in str3:
    print(f"{substring} found in {str3}")