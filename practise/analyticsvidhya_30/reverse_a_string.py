def reverse_string(s):
    reversed_string=""
    for char in s:
        reversed_string=char+reversed_string
    return reversed_string
result=reverse_string("hello world")
print(result)
