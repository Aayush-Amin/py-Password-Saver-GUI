def genEncrypt(general):
    encryptedGeneralUnjoined=[]

    q=0
    for i in range(len(general)):
        convertLetter=ord(general[q])
        
        unicodeChange=convertLetter+1
        UnicodeChangedLetter=chr(unicodeChange)
        
        encryptedGeneralUnjoined.append(UnicodeChangedLetter)
        q+=1

    generalEncrypted=''.join(encryptedGeneralUnjoined)
    return generalEncrypted
