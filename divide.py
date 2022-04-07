
# open the original file 
with open('Hello.txt', 'rb') as original_file:
    original = original_file.read()

# count the number of characters 
characters =  len(original)


new_characters= characters

while(new_characters % 3 != 0):
    new_characters= new_characters + 1



count = new_characters - characters

#add spaces 
with open('Hello.txt','a') as new_file:
    while(count !=0):
        new_file.write('')
        count = count-1
new_file.close()


#divide into f1 f2 f3 parts
with open('Hello.txt','r') as new_file1:
    file = new_file1.read()
    new_file1.close()
    a=int(new_characters/3)
    b=int((2*a)+1)
    
    f1 = file[0:a]
    with open("parts/f1.txt",'w') as file1:
        file1.write(f1)
    f2 = file[a:b]
    with open("parts/f2.txt",'w') as file2:
        file2.write(f2)
    f3 = file[b:new_characters]
    with open("parts/f3.txt",'w') as file3:
        file3.write(f3)
    # print(f3)

