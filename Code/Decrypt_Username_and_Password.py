def mainDecrypteFun():
    decryptedUsername=None
    decryptedPassword=None
    
    lines=runFile()
    
    decryptedUsername=decryptUsernameFun(lines)
    decryptedPassword=decryptPasswordFun(lines)
    return decryptedUsername,decryptedPassword


def runFile():
    outFile=open('Code\passwordData.txt','r')
    Lines=outFile.readlines()
    outFile.close()
    return Lines
    

def decryptUsernameFun(Lines):
    text=Lines[0]
    decryptedUsernameUnjoined=[]
    q=0
    
    for i in range(len(text)):
        convertLetter=ord(text[q])
        
        unicodeChange=convertLetter-1
        UnicodeChangedLetter=chr(unicodeChange)
        
        decryptedUsernameUnjoined.append(UnicodeChangedLetter)
        q+=1

    DecryptedUsername=''.join(decryptedUsernameUnjoined)
    return DecryptedUsername
    

def decryptPasswordFun(lines):
    text=lines[1]
    decryptedPasswordUnjoined=[]
    q=0
    
    for i in range(len(text)):
        convertLetter=ord(text[q])
        
        unicodeChange=convertLetter-1
        UnicodeChangedLetter=chr(unicodeChange)
        
        decryptedPasswordUnjoined.append(UnicodeChangedLetter)
        q+=1

    DecryptedPassword=''.join(decryptedPasswordUnjoined)
    return DecryptedPassword

