def encryptUsername(username):
    encryptedUsernameUnjoined=[]

    q=0
    for i in range(len(username)):
        convertLetter=ord(username[q])
        
        unicodeChange=convertLetter+1
        UnicodeChangedLetter=chr(unicodeChange)
        
        encryptedUsernameUnjoined.append(UnicodeChangedLetter)
        q+=1

    usernameEncrypted=''.join(encryptedUsernameUnjoined)
    
    outFile=open('passwordData.txt', 'a')
    outFile.write(usernameEncrypted+'\n')
    outFile.close()



def encryptPassword(password):
    encryptedPasswordUnjoined=[]

    q=0
    for i in range(len(password)):
        convertLetter=ord(password[q])
        
        unicodeChange=convertLetter+1
        UnicodeChangedLetter=chr(unicodeChange)
        
        encryptedPasswordUnjoined.append(UnicodeChangedLetter)
        q+=1

    passwordEncrypted=''.join(encryptedPasswordUnjoined)
    

    outFile=open('passwordData.txt', 'a')
    outFile.write(passwordEncrypted)
    outFile.close()
