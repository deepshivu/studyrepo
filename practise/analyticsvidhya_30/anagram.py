def anagram_check():
    string1="silent"
    string2="listena"
    string1_sort=sorted(string1)
    print("string1"+str(string1_sort))
    string2_sort=sorted(string2)
    print("string2"+str(string2_sort))
    if string1_sort==string2_sort:
        print("string 1 and 2 are angrams")
    else:
        print("string 1 and 2 are not angrams")
anagram_check()
