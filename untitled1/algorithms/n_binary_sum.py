import  math

dig1 = [1,0,1]
dig2 = [0,0,1]

def sum_binary(arr1, arr2):
    for i in reversed(arr1):
        for j in reversed(arr2):
            k = i + j

