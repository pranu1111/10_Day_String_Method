from ntpath import join


a='pranita'
a1=a.capitalize()
# print(a1)...............Upper case the first letter in this sentence

p='python'
p1=p.capitalize()
# print(p1).................Upper case the first letter in this sentence


# casefold()...............Make the string lower case
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
# print(x)..................Make the string lower case



#count.............Returns the number of times a specified value occurs in a string
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
# print(x).........Returns the number of times a specified value occurs in a string

txt = "I love apples, apple are my favorite fruit, I eat apple every day"
x = txt.count("apple")
# print(x)..................Returns the number of times a specified value occurs in a string


# encode()..............Returns an encoded version of the string
txt = "My name is Ståle"
x = txt.encode()
# print(x)..................Returns an encoded version of the string

txt = "My name is Pranita"
x = txt.encode()
# print(x)..........................Returns an encoded version of the string


# endswith()..................Returns true if the string ends with the specified value
txt = "Hello, welcome to my world."
x = txt.endswith(".")
# print(x)................Returns true if the string ends with the specified value

txt = "Hello, welcome to my world, please come!"
x = txt.endswith("!")
# print(x)...................Returns true if the string ends with the specified value


# find()...........Searches the string for a specified value and returns the position of where it was found
txt = "Hello, welcome to my world."
x = txt.find("welcome")
# print(x).......................Searches the string for a specified value and returns the position of where it was found

txt = "python is popular langue"
x = txt.find("popular") 
# print(x)...................Searches the string for a specified value and returns the position of where it was found



# isalnum()..................Returns True if all characters in the string are alphanumeric
txt = "Company12"
x = txt.isalnum()
# print(x)............Returns True if all characters in the string are alphanumeric

a = 'pranita8998.'
a1 = a.isalnum()
# print(a1)...................Returns True if all characters in the string are alphanumeric


# isidentifier().............Returns True if the string is an identifier
txt = "Demo"
x = txt.isidentifier()
# print(x)...................Returns True if the string is an identifier

p_K = 1001
# x = txt.isidentifier()
# print(p.isidentifier()).............Returns True if the string is an identifier


# islower()..............Returns True if all characters in the string are lower case
txt = "hello world!"
x = txt.islower()
# print(x)..................Returns True if all characters in the string are lower case

s = 'sushant'
# print(s.islower())...................Returns True if all characters in the string are lower case


# isspace()...............Check if all the characters in the text are whitespaces.
txt = "   "
x = txt.isspace()
# print(x)..............True

b = '        '
# print(b.isspace())........True


# istitle()......................Check if each word start with an upper case letter.
txt = "Hello, And Welcome To My World!"
x = txt.istitle()
# print(x)................True

B = 'hey.. sweety!'
# print(B.istitle())..............False


# strip()...................Remove spaces at the beginning and at the end of the string.
txt = "     banana     "
x = txt.strip()
# print("of all fruits", x, "is my favorite").......

q1 = '   python is easy    ! '
# print(q1)
q = q1.strip()
# print(q)................Remove spaces at the beginning and at the end of the string


# swapcase()...................Make the lower case letters upper case and the upper case letters lower case
txt = "Hello My Name Is PETER"
x = txt.swapcase()
# print(x).....................hELLO mY nAME iS peter

a = 'pranita is CLEAVER'
# print(a.swapcase()).........PRANITA IS cleaver


# title()..........................Make the first letter in each word upper case
txt = "Welcome to my world"
x = txt.title()
# print(x)...............Welcome To My World

v = 'delhi is capital of india '
# print(v.title()).................Delhi Is Capital Of India 


# zfill()................Fill the string with zeros until it is 10 characters long
txt = "50"
x = txt.zfill(10)
# print(x)............0000000050

txt = "50"
x = txt.zfill(20)
# print(x)..................00000000000000000050

a = 'python'
# print(a.zfill(15))................000000000python


# upper()................Upper case the string
txt = "Hello my friends"
x = txt.upper()
# print(x).............HELLO MY FRIENDS

m = 'hello moto!'
# print(m.upper()).............HELLO MOTO!


# isupper().......................Check if all the characters in the text are in upper case
txt = "THIS IS NOW!"
x = txt.isupper()
# print(x).....................True

o = "lovely!"
# print(o.isupper())............False


# lower()......................Lower case the string
txt = "Hello my FRIENDS"
x = txt.lower()
# print(x)..............hello my friends

d = 'HELLO Guys'
# print(d.lower())........hello guys


# lstrip()..................Remove spaces to the left of the string
txt = "     banana     "
x = txt.lstrip()
# print("of all fruits", x, "is my favorite")........of all fruits banana      is my favorite

ab = '       hello world!    '
# print(ab.lstrip()).............hello world! 


# join().............Join all items in a tuple into a string, using a hash character as separator
myTuple = ("John", "Peter", "Vicky")
x = "#".join(myTuple)
# print(x)...............John#Peter#Vicky

name = ("sweety","preety","mony","sony")
names=",".join(name)
# print(names)...............sweety,preety,mony,sony


# partition().............Returns a tuple where the string is parted into three parts
txt = "I could eat bananas all day"
x = txt.partition("bananas")
# print(x)............('I could eat ', 'bananas', ' all day')

a = 'OPD - Out Patient Department'
opd = a.partition("Patient")
# print(opd)...............('OPD - Out ', 'Patient', ' Department')


# replace().............Returns a string where a specified value is replaced with a specified value
txt = "I like bananas"
x = txt.replace("bananas", "apples")
# print(x).............I like apples

a = 'I lives in Pune'
# print(a.replace("Pune","Hyderabad"))......I lives in Hyderabad


# rfind()...............Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."
x = txt.rfind("casa")
# print(x)...........12


# rindex()...............Searches the string for a specified value and returns the last position of where it was found
txt = "Mi casa, su casa."
x = txt.rindex("casa")
# print(x)..............12


# split()...............Splits the string at the specified separator, and returns a list
txt = "welcome to the jungle"
x = txt.split()
# print(x).............['welcome', 'to', 'the', 'jungle']

p = 'welcome to the hyderabad'
# print(p.split()).....................['welcome', 'to', 'the', 'hyderabad']


# rstrip()..........Returns a right trim version of the string
txt = "     banana     "
x = txt.rstrip()
# print("of all fruits", x, "is my favorite")..........of all fruits      banana is my favorite


# splitlines()...........Splits the string at line breaks and returns a list
txt = "Thank you for the music\nWelcome to the jungle"
x = txt.splitlines()
# print(x).......................['Thank you for the music', 'Welcome to the jungle']


# startswith()............Returns true if the string starts with the specified value
txt = "Hello, welcome to my world."
x = txt.startswith("Hello")
# print(x)............True

a = 'enough yaar'
print(a.startswith('enough'))
