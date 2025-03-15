input_string="hEllow world"
input_string_lower=input_string.lower()
vowels="aeiou"
count=0
for char in input_string_lower:
    if char in vowels:
        count+=1
print("count of vowels is"+str(count))

