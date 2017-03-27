"""
distribution.py
Author: <your name here>
Credit: <list sources used, if any>

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

input = input("Please enter a string of text (the bigger the better): ")

a = input.count("a")
b = input.count("b")
c = input.count("c")
d = input.count("d")
e = input.count("e")
f = input.count("f")
g = input.count("g")
h = input.count("h")
i = input.count("i")
j = input.count("j")
k = input.count("k")
l = input.count("l")
m = input.count("m")
n = input.count("n")
o = input.count("o")
p = input.count("p")
q = input.count("q")
r = input.count("r")
s = input.count("s")
t = input.count("t")
u = input.count("u")
v = input.count("v")
w = input.count("w")
x = input.count("x")
y = input.count("y")
z = input.count("z")
