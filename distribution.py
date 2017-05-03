"""
distribution.py
Author: Kai Darrow
Credit: http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python
http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
http://stackoverflow.com/questions/1155617/count-occurrence-of-a-character-in-a-string
http://stackoverflow.com/questions/20196159/how-to-append-multiple-values-to-a-list-in-python

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
am = input("Please enter a string of text (the bigger the better): ")
aa = am.lower() 
aaa = aa.replace(" ","")
aaaa = (" ".join(aaa))
mfe = aaaa.split()
mfe.sort()
a = mfe.count('a')
b = mfe.count('b')
c = mfe.count('c')
d = mfe.count('d')
e = mfe.count('e')
f = mfe.count('f')
g = mfe.count('g')
h = mfe.count('h')
i = mfe.count('i')
j = mfe.count('j')
k = mfe.count('k')
l = mfe.count('l')
m = mfe.count('m')
n = mfe.count('n')
o = mfe.count('o')
p = mfe.count('p')
q = mfe.count('q')
r = mfe.count('r')
s = mfe.count('s')
t = mfe.count('t')
u = mfe.count('u')
v = mfe.count('v')
w = mfe.count('w')
x = mfe.count('x')
y = mfe.count('y')
z = mfe.count('z')
listnumber = [a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z]
listletter = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
listtogo = zip(listletter, listnumber)
lim = list(listtogo)
"""
"""
def compare(one, two):
    return two > one

def bsort(seq, cmp):
    sorted = False  
    while not sorted:
        sorted = True 
        for index, value in enumerate(seq): 
            if index > 0:                
                if not cmp(seq[index-1], value):  
                    sorted = False        
                    seq[index-1], seq[index] = seq[index], seq[index-1] 

    
listff = lim
bsort(listff, compare)
print(listff)

for memes, elmemes in listff:
    if elmemes > 1:
        memesmemes = elmemes * memes
        print(memesmemes)
for memes, elmemes in listff:
    if elmemes == 1:
        pianobutter = elmemes* memes
        print(pianobutter)
   