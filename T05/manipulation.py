# request sentence 
str_manip = input("enetr a sentence: ")

# Manipulation

## Calculating the length
print(len(str_manip))

## Find the last letter in string and replace every occurrence
replace = str_manip[-1]
print(str_manip.replace(replace,"@"))

## Print last 3 characters backwords
str_manip_len = len(str_manip)                      
last_three_words = str_manip[str_manip_len-3:]
print(last_three_words[-1::-1])

    #the len function returns an int so i figured it can be used as an index position


## Create a 5 letter word consisting of first three characters and the last two
first_three = str_manip[0:4]
last_two = str_manip[str_manip_len-1:]
new_word = first_three + last_two
print(new_word)

    # using the same logic as ealier
    # I used the length varable to determine the index positions of the last two letters

## Displaying each word in new a newline 
str_manip_lst = str_manip.split(" ")
for word in str_manip_lst:
        print(word)


    # I had to re-watch how to break a string into a list
    # I understand how iterables work so I used that to unpack the list and print out a new word on eachline
    # If there was another way to do this more inline to this chapter I would like feedback on how in the review.