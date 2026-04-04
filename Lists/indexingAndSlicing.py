L = [1,2,3,4,5]
# positive indexing 
print(L[0])
print(L[1])
print(L[2])
print(L[3])
print(L[4])


# how to give specing between these two 
print('\n')

# negitive indexing 
print(L[-1])
print(L[-2])
print(L[-3])
print(L[-4])
print(L[-5])

# adding items to a list 
L.append(6)
print(L)

# removing items from a list 
L.remove(6)
print(L)


# indexing in 2D list
L1 = [1,2,3,[4,5,[6,7]],[8,9]]

print("printing the 2D list")

print(L1[0])
print(L1[1])
print(L1[2])
print(L1[3])
print(L1[4][0])

# how to give spacing between these two 
print('\n')

print("printing the negitive indexing of 2D list")
# negitive indexing 
print(L1[-1])
print(L1[-2])
print(L1[-3])
print(L1[-4])
print(L1[-5])


print("\nremoving the value 9 from the nested list")
# Target the sub-list directly to remove the item inside it
L1[4].remove(9) 
print(L1)
