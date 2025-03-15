def reverse_string(s):
    s=s.replace(" ","").lower()
    return s[::-1]
input_string="A man a plan a canal Panama"
reversed_string=reverse_string(input_string)
print(reversed_string)
if reversed_string==input_string:
    print("it is palindrome")
else:
    print("it is not a palindrome")