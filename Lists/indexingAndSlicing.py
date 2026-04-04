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


# Slicing Examples
# Syntax: list[start : stop : step]
# start is inclusive, stop is exclusive
print("\n--- Slicing Examples ---")
L2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original List:", L2)
print("Slicing from index 1 to 4 (L2[1:5]):", L2[1:5]) 
print("First 3 elements (L2[:3]):", L2[:3])
print("Elements from index 5 to end (L2[5:]):", L2[5:])
print("Every second element (L2[0:10:2]):", L2[0:10:2])
print("Reversing the list (L2[::-1]):", L2[::-1])


# More Negative Indexing (Slicing with negative indices)
print("\n--- Negative Index Slicing ---")
print("Last 3 elements (L2[-3:]):", L2[-3:])
print("All except last 2 (L2[:-2]):", L2[:-2])
print("Slicing backwards (L2[-2:-6:-1]):", L2[-2:-6:-1])


# Traversal Examples (Looping through a list)
print("\n--- Traversal Examples ---")

print("1. Direct Traversal (using for-in):")
for item in L:
    print(item, end=" ") # end=" " prints on the same line
print()

print("\n2. Using Range and Length (getting indices):")
for i in range(len(L)):
    print(f"Index {i}: {L[i]}")

print("\n3. Using Enumerate (best of both worlds):")
for index, value in enumerate(L):
    print(f"Index {index} has value {value}")

print("\n4. Traversing a 2D List (Nested Loop):")
matrix = [[1, 2], [3, 4], [5, 6]]
for row in matrix:
    for element in row:
        print(element, end=" ")
    print() # New line after each row
