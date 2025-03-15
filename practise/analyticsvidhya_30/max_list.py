def max_list():
    list1=[1,2,6,4,5]
    max_no=list1[0]
    for num in list1:
        if num>max_no:
            max_no=num
    print(max(list1))
    return max_no
maximum_no=max_list()
print(maximum_no)