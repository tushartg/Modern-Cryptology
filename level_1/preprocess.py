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
s = s.replace("\n", "")
s = s.lower()

#Writing the string s in file level_1.txt for further use
f = open("level_1.txt", "w+")
f.write(s)
f.close()