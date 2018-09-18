#9/18 notes
#strings vs. lists
#strings: basically one long sentence, create a variable name and then put something in the parenthesis (Ex: wizard_list = x,y,z print (wizard_list))
#lists: a list, but the syntax is different, made up of a bunch of strings (EX: wizard_list = )
wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']
print (wizard_list)
print (wizard_list[2])
#^prints third item bc computers think of numbers on a scale of 0-9

#lists:
#can be more useful than strings
#a combination of intergers and strings

school_supplies = [1, 'notebooks', 2, 'pencils', 3, 'highlighters' ]
print (school_supplies)

#append: built in python function to add items to a list
school_supplies.append (4)
print (school_supplies)

#deleting: takes an item away

del school_supplies[2]
print(school_supplies)

#adding and multiplying

mylist1 = (1,2,3,4)
mylist2 = (5,6,7,8)

mylistadd = mylist1 + mylist2
print(mylistadd)

mylistmult = mylist1 * 4
print(mylistmult)
