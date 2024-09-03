# file_name=input("Your file name : ")  
f=open("./dic.txt","r")
words=f.readlines()

word = input("Enter a word to search for: ")
word_found=False
for roll in words:

    if roll.find(word) != -1:
      word_found = True
      break
if word_found:
    print(word,"word found in the file.")
    print("Line",roll)
else:
    print("word not found in the file. Please enter a valid word.")

f.close()