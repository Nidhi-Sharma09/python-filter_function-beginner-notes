#it is used to filter any element in the list based on the given condition
def even(x):
    if x%2==0:
        return True
    
#appling filter filter(fintion,variable)
lst=[1,2,3,4,5,6,7,8,9,]
print(list(filter(even,lst)))
#output: [2,4,6,8]


#filter with lambda
num=[1,2,3,4,5,6,7,8,9]
greter=list(filter(lambda x: x>=5, num))
print(greter)
#output: [5, 6, 7, 8, 9]


#filter with lambda and multiple condition
numb=[1,2,3,4,5,6,7,8,9,10,11,12]
even_amd_greater=list(filter(lambda x: x>5 and x%2==0, numb))
print(even_amd_greater)
#output: [6, 8, 10, 12]


