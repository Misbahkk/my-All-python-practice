import os

# fh = open("data.txt","w")
# print("This line for filehandnling file", file=fh)
# fh.close()
# fh=open("data.txt","r")
# print(fh.readable())
# print(fh.writable())
# if fh.readable():
#     print("file is readable")
# fh.close()
# fh=open("data.txt","a")
# print("I am a Girl",file=fh)
# fh.close()
# f = open("data.txt","r")
# if f:
#     print("Opend")
# print(f)
# -----------------------------------------------------------------------------------------
# This program cheacked that file that exit or not
# print("HYee!! How I can Help Yo...")
# fileName=input("write a file name... ")
# if os.path.isfile(fileName):
#     f=open(fileName,"w")
#     print("This line for filehandnling file My name is misbah", file=f)
# else:
#     print("file is not exite")

# ---------------------------------------------------------------------------------------
# fileName=input("write a file name... ")
# x="read"
# y="write"
# z="append"
# def readFile():
#     f=open("data.txt","r")
#     print(f.read())
#     f.close()
# def writeFile():
#     f=open("data.txt","w")
#     data=input("Enter Your file data that you save: ")
#     print(data,file=f)
#     f.close()
# def appendFile():
#     f=open("data.txt","a")
#     print("This is my append function",file=f)
#     f.close()
# if fileName==x:
#     readFile()
# elif fileName == y:
#     writeFile()
# elif fileName == z:
#     appendFile()

# else:
#     print("Enter a file name")

# ------------------------------------------
# 

fh = open('data.txt',"r")
# not_eof = True
# while not_eof:
#         mytxt = fh.readline()
#         if not mytxt:
#             print("eof reached...")
#             not_eof=False
#         elif "Misbah" in mytxt:
#             print("String exit in a file")
#         else:
#             print("file is not exit")
# fh.close()
# string to search in file
word = ""
# with open("data.txt", 'r') as fp:
fp =open("data.txt", 'r')
    # read all lines in a list
lines = fp.readlines()
while(word!="exit"):
    word = input("Enter a Roll Number : ")
    
    for line in lines:
        # check if string present on a current line
        if line.find(word) != -1:
            print("Roll NUmber is present ",word)
            # print('Line Number:', lines.index(line))
            print('Line:', line)
        
        
print("You Exit the program")


    
# def serch_str(file_path,word):
#     with open("data.txt", 'r') as file:
#             # read all content of a file
#             content = file.read()
#             # check if string present in a file
#             if word in content:
#                 print('string exist in a file')
#             else:
#                 print('string does not exist in a file')