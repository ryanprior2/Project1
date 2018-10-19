import os
import filecmp
#from dateutil.relativedelta import *
#from datetime import date


def getData(file):
	file = open(file, 'r')
	lines = file.readlines()
	file.close()
	file_dict_list = []
	for line in lines:
		file_dict = {}
		index = line.split(',')
		file_dict['First'] = index[0]
		file_dict['Last'] = index[1]
		file_dict['Email'] = index[2]
		file_dict['Class'] = index[3]
		file_dict['DOB'] = index[4]
		file_dict_list.append(file_dict)
	return file_dict_list
# get a list of dictionary objects from the file
#Input: file name
#Ouput: return a list of dictionary objects where
#the keys are from the first row in the data. and the values are each of the other rows

def mySort(data,col):
	sorted_list = sorted(data, key = lambda x: x[col])
	return('{} {}'.format(sorted_list[0]['First'],sorted_list[0]['Last']))
# Sort based on key/column
#Input: list of dictionaries and col (key) to sort on
#Output: Return the first item in the sorted list as a string of just: firstName lastName


def classSizes(data):
	senior_size = 0
	junior_size = 0
	sophomore_size = 0
	freshman_size = 0
	for student in data:
		if student['Class'] == 'Senior':
			senior_size += 1
		elif student['Class'] == 'Junior':
			junior_size += 1
		elif student['Class'] == 'Sophomore':
			sophomore_size += 1
		elif student['Class'] == 'Freshman':
			freshman_size += 1
	list_tuples = []
	list_tuples.append(('Senior',senior_size))
	list_tuples.append(('Junior',junior_size))
	list_tuples.append(('Sophomore',sophomore_size))
	list_tuples.append(('Freshman',freshman_size))
	return sorted(list_tuples, key = lambda x: x[1], reverse = True)
# Create a histogram
# Input: list of dictionaries
# Output: Return a list of tuples sorted by the number of students in that class in
# descending order
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]


def findMonth(a):
	month_list = []
	for student in a:
		month_list.append(student['DOB'].split('/')[0])
	month_dict = {}
	for num in month_list:
		if num not in month_dict.keys():
			month_dict[num] = 1
		else:
			month_dict[num] += 1
	final_list = sorted(month_dict.keys(), key = lambda x: month_dict[x], reverse = True)
	return int(final_list[0])
# Find the most common birth month from this data
# Input: list of dictionaries
# Output: Return the month (1-12) that had the most births in the data

def mySortPrint(a,col,fileName):
#Similar to mySort, but instead of returning single
#Student, the sorted data is saved to a csv file.
# as fist,last,email
#Input: list of dictionaries, col (key) to sort by and output file name
#Output: No return value, but the file is written

	pass

def findAge(a):
	current_date = "10/23/2018"
	a.remove(a[0])
	age_list = []
	for student in a:
		age_list.append(int(current_date.split('/')[2]) - int(student['DOB'].split('/')[2]))
	total = 0
	for age in age_list:
		total += age
	return int(total/len(age_list))
# def findAge(a):
# Input: list of dictionaries
# Output: Return the average age of the students and round that age to the nearest
# integer.  You will need to work with the DOB and the current date to find the current
# age in years.


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()