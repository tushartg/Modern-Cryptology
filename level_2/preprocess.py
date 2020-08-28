f = open("input.txt", "r+")
s = f.read()
f.close()

#First remove all the character other than English Alphabets.
#Also convert the capital letters to small letters.
s = s.replace(" ", "")
s = s.replace(".", "")
s = s.replace(",", "")
s = s.replace("\"", "")
s = s.replace("_", "") 
s = s.lower()

f = open("level_2.txt", "w+")
f.write(s)
f.close()