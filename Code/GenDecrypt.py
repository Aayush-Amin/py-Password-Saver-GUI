mainFile=open('Code\passwordData.txt','r')
mainFileLines=mainFile.readlines()
mainFile.close()

def genDecrypt(Lines):
    decryptedGeneralUnjoined=[]
    q=0
    
    for i in range(len(Lines)):
        convertLetter=ord(Lines[q])
        
        unicodeChange=convertLetter-1
        UnicodeChangedLetter=chr(unicodeChange)
        
        decryptedGeneralUnjoined.append(UnicodeChangedLetter)
        q+=1

    DecryptedGeneral=''.join(decryptedGeneralUnjoined)
    return DecryptedGeneral


