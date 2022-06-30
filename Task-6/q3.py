count = 0;  
word = "";  
maxCount = 0;  
words = [];  
  
file = open("about.txt", "r")  
 
for line in file:  
    string = line.lower().replace(',','').replace('.','').split(" ");
 
    for str in string: 
        if len(str) == 6:
            words.append(str);  
    print("\nSix letter words in the given file are: ")
    print(words)

for i in range(0, len(words)):  
    count = 1;  

    for j in range(i+1, len(words)):  
        if(words[i] == words[j]):  
            count = count + 1;  
              
    if(count > maxCount):  
        maxCount = count;  
        word = words[i];  
          
print("\nMost frequently used 6 letter word is: ");
print(word)  
file.close();  