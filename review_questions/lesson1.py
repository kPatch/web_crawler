# -----------Question 2-----------

# Write Python code that prints out the number of hours in 7 weeks

print 7*7*24

# -----------Question 3-----------
# Which of the following sequences of statements leaves the value
# of variable x the same as it was before the statements.
# Assume that both a and x refer to integer values before this code.

#1)	a = x
#	a = a + 1

#2) x = x + 1
#	x = x

#3) z = x
#	a = z
#	x = a

#4) a = x
#	x = a

#5)	a,x = x,a
#	a,x = x,a

#Answer: 1), 3), 4), 5)

# -----------Question 4-----------
# Write Python code that stores the distance 
# in meters that light travels in one 
# nanosecond in the variable, nanodistance. 

# These variables are defined for you:

speed_of_light = 299800000. # meters per second
nano_per_sec = 1000000000. # 1 billion

# After your code,running
# print nanodistance
# should output 0.2998

# Note that nanodistance must be a decimal number.

# ASSIGN nanodistance BELOW this line

nanodistance = speed_of_light / nano_per_sec

print nanodistance


# -----------Question 5-----------
# Given any string s, which of the following always have the same value
# as s? (Be careful, s could be ''.)

#1) ('a' + s)[1:]
#2) s + ''
#3) s[0] + s[1:]
#4) s[0:]

# ANSWER 1),3),4)
# 2) doesn't work because if s is '' (the empty string) then
# we get an error because if we try s[0], there is no character at
# position 0.

# -----------Question 6-----------
# Given the variables s and t defined as:
s = 'udacity'
t = 'bodacious'
# write Python code that prints out udacious
# without using any quote characters in
# your code.

print s[0] + t[2:]
#OR
print s[:-2] + t[-3:]

# -----------Question 7-----------
# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the first occurrence of 'hoo'
# in the value of text, or -1 if
# it does not occur at all.

text = "first hoo" 

# ENTER CODE BELOW HERE
print text.find('hoo')

# -----------Question 8-----------
# Assume text is a variable that
# holds a string. Write Python code
# that prints out the position
# of the second occurrence of 'zip'
# in text, or -1 if it does not occur
# at least twice.

# For example,
#text = 'all zip files are zipped' 
# >>> 18
# text = 'all zip files are compressed'
# >>> -1

text = "all zip files are zipped" 

#ENTER CODE BELOW HERE

print text.find("zip",text.find("zip")+1)

# OR OR OR OR OR


sstart = text.find("zip");

print text.find("zip", sstart + 1)

# -----------Question 9-----------
# Given a variable, x, that stores the 
# value of any decimal number, write Python 
# code that prints out the nearest whole 
# number to x.
# If x is exactly half way between two 
# whole numbers, round up, so
# 3.5 rounds to 4 and 2.5 rounds to 3.
# You may assume x is not negative.

# Hint: The str function can convert any number into a string.
# eg str(89) converts the number 89 to the string '89'

# Along with the str function, this problem can be solved 
# using just the information introduced in unit 1.

# x = 3.14159 
# >>> 3 (not 3.0)
# x = 27.63 
# >>> 28 (not 28.0)
# x = 3.5 
# >>> 4 (not 4.0)

x = 3.14159

#ENTER CODE BELOW HERE

x = x + 0.5
x = str(x)
pointPos = x.find('.')

print x[:pointPos]


# ############# ADDITIONAL QUESTIONS #############
# Question 1
# Given a string s which of the following expressions will print
# 'Udacity'
s =  "C i d a t y U c i t y  d  a" #no spaces

# 1) s[6] + s[-2:] + s[7:12]
# 2) s[-7] + s[2:4] + s[7:11]
# 3) s[6] + s[-2:] + s[7:11]
# 4) s[6] + s[-2] + s[3] + s[:2] + s[4:6]
# 5) s[6] + s[2:4] + s[7:13]
# 6) s[6] + s[2] + s[3] + s[7:11]

#ANSWER: 2),3),6)

# Question 6

##################################################
#     Exercise by Sam the Great from forums!     #
##################################################
# Oh no! A superhero has just flown by 'Udacity'
# and scattered pieces of it all over the place.
# Luckily, we've recovered 3 fragments of debris
# that we can work with. Help us fix 'Udacity'!

# Write one line of Python code that uses
# only the variables fragA, fragB, and fragC 
# to satisfy the given test cases.
# If you are not sure how multiple assignments and
# string slicing works, check out the links to 
# additional tutorials in Instructor Comments
# under this exercise!

fragA, fragB, fragC = 'supercalifragilisticexpialudacious', \
                      'SUPERMAN', 'ytiroirepus'

### WRITE MULTIPLE ASSIGNMENT HERE ###
### THIS MUST BE ONE LINE ###
part1, part2, part3 = fragB[fragB.find('U')], fragA[fragA.find('da'):fragA.find('i',-5)], (fragC[2]+fragC[1]+fragC[0])


### TEST CASES. PRESS RUN TO TEST ###
deadline = part1 + part2[0:2] + part3[-1]
print "Test case 1 (Uday): ", deadline == 'Uday'
fixed = part1 + part2 + part3
print "Test case 2 (Udacity): ", fixed == 'Udacity'
destination = part1 + part2[-1] + part3
print "Test case 3 (Ucity): ", destination == 'Ucity'



