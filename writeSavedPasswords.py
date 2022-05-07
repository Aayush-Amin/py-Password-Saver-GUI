from GenEncrypt import genEncrypt

def writeSavedPasswords(website,name,password):
    enWebsite=genEncrypt(website)
    enName=genEncrypt(name)
    enPassword=genEncrypt(password)
    savePath=open('savedPassword.txt', 'a')
    savePath.write(f'{enWebsite};Vtfsobnf;{enName}!!!!Qbttxpse;{enPassword}'+'\n')
    savePath.close()
