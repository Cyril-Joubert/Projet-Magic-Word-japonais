# -*- coding: utf-8 -*-

import io
# #create array for testing the coding 
# def createArray(size=50, max=2000):
# 	from random import randint
# 	return [randint(0,max) for _ in range(size)]
# #print(createArray())

# file = io.open("C:\\Users\\munau\\OneDrive\\Bureau\\Projet MEcab\\taberuFinal.txt", "r", encoding='cp932', errors='ignore')
# dictionnary = {}
# for line in file:
# 	x = line.split("\t")
# 	a = x[0]
# 	b = x[1]
# 	dictionnary[a] = b

# print(dictionnary)

'''
Fonction Croissante et Décroissante qui trie la sortie de MergeSort croissante ou descroissante, prend en entrée 2 tables left et right
donne en sortie le tableau merged tableau ordoné
'''
def mergeAsc(left, right):
	merged = [] #final output array
	leftIndex, rightIndex = 0, 0 

	# While there are still element in the table = compare the 2 indexes
	while len(left) > leftIndex and len(right) > rightIndex: #puts the smallest of the 2 indexes in until one of the indexes is empty
		if left[leftIndex] < right[rightIndex]:
			merged.append(left[leftIndex]) 
			leftIndex+=1
		else:
			merged.append(right[rightIndex])
			rightIndex+=1

	#if there are still elements in one of the 2 indexes, they get appended to the results (one is longer)
	if leftIndex == len(left):
		merged.extend(right[rightIndex:])
	else:
		merged.extend(left[leftIndex:])
	return merged


# merge descending
def mergeDesc(left, right):
	merged = [] #final output array
	leftIndex, rightIndex = 0, 0 

	# While there are still element in the table = compare the 2 indexes
	while len(left) > leftIndex and len(right) > rightIndex: #puts the biggest of the 2 indexes in until one of the indexes is empty
		if left[leftIndex] > right[rightIndex]:
			merged.append(left[leftIndex]) 
			leftIndex+=1
		else:
			merged.append(right[rightIndex])
			rightIndex+=1

	#if there are still elements in one of the 2 indexes, they get appended to the results (one is longer)
	if leftIndex == len(left):
		merged.extend(right[rightIndex:])
	else:
		merged.extend(left[leftIndex:])
	return merged

# a = [1,3,5]
# b = [2,4,6]
# print(mergeDesc(a,b))


'''
Fonction récursive qui divise la liste en 2 jusqu'à ce qu'il n'y ai plus que 2 items et avec la fonction merge les trie dans l'ordre 
prend en entrée la table à trier et appelle en sortie la fonction merge.
'''

def mergeSortAsc(table): #mergesort ascending

	#if table is a list of zeo or one element is sorted, by definition. So we return the table as is
	if len(table) <= 1:
		return table
	
	#recursive function that splits the list in half and mergeSort on each half
	midpoint = int(len(table)/2)
	left = mergeSortAsc(table[:midpoint])
	right = mergeSortAsc(table[midpoint:])

	#merge the 2 sorted parts
	return mergeAsc(left, right)

def mergeSortDesc(table): #mergesort descending

	#if table is a list of zero or one element is sorted, by definition. So we return the table as is
	if len(table) <= 1:
		return table
	
	#recursive function that splits the list in half and mergeSort on each half
	midpoint = int(len(table)/2)
	left = mergeSortDesc(table[:midpoint])
	right = mergeSortDesc(table[midpoint:])

	#merge the 2 sorted parts
	return mergeDesc(left, right)



# results = mergeSortDesc(dictionnary)
# print(results)

def main():
	array = []
	array = createArray()
	print(array)

	results = mergeSortDesc(array)
	print(results)

if __name__ == "__main__":
	main()



