"""
distribution.py
Author: Kai Darrow
Credit: http://stackoverflow.com/questions/6797984/how-to-convert-string-to-lowercase-in-python
http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
http://stackoverflow.com/questions/1155617/count-occurrence-of-a-character-in-a-string

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
import string
from collections import Counter

a = input("Please enter a string of text (the bigger the better): ")
aa = a.lower()
counter = Counter(aa)
aaa = str(counter['a']) * 'a' 
print(aaa)