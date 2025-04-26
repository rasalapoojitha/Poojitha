#define two arrays (lists)
array1=[1,2,3,4,5]
array2=[4,5,6,7,8]

common_values=set(array1).intersection(set(array2))

print("common values between the two arrays:",common_values)
