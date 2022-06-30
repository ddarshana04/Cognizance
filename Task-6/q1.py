data = open("onelinefile.txt","r")
word = str(data.read())
file = len(word)
temp = ""
c=0
for i in range(file):
    if word[i].isalpha()==True:
        temp += word[i]
        if i+1 < file:
            if word[i+1].isalpha()!= True:
                if c!= 3:
                    temp +=  ","
                c += 1

    elif word[i].isdigit()==True:
        temp += word[i]
        if word[i+1] == ".":
            temp += "."
        elif word[i+1].isdigit()!= True and word[i+1]!= ".":
            if c!= 3:
                temp += ","
            c += 1
    if c%4 == 0:
        temp += "\n"
        c = 0
data.close()

u_data = open("Filename2.csv","w")
u_data.writelines(temp)
u_data.close()

print("\nModified file contents: \n")
print(temp)
