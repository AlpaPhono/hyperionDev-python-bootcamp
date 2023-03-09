#********** OPTIONAL TASK *************
# Write a program that will count
# The number of char words and lines in a file
#**************************************

f = open("input.txt","r")
lines = f.readlines()
no_lines = len(lines)
char = 0
words = 0
vowels = ["a","e","i","o","u"]
v_count = 0

#----------- Calculating no. words and char ------------
for line in lines:                              # looping over lines
    current_line = line.split()
    char += len(line)
    words += len(current_line)
    for word in current_line:                   # each word in line
        char += len(word)
        for letter in word:                     # each letter in word
            if letter in vowels:
                v_count += 1



print(v_count)
print(char)
print(words)
print(no_lines)

'''
no_char = len(char)
print(no_lines)
print(no_char)
'''

f.close()
'''
with open("input.txt", "r") as f:
    passage = f.read()
    lines = f.readlines()
    print(len(lines))
    #print(passage)
    '''
#************************* REFERENCES *****************
# Got help from Christiaan Joubert