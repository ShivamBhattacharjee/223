from pypdf import PdfReader
import PyPDF2 as pd
filename = input('Path to the file: ')
filename=filename.strip()
file = open(filename,'rb')
pdfReader =PdfReader(file,strict=False)

tried = 0

if not pdfReader.isEncrypted:
    print('The file is not password protected! You can successfully open it!')
else:
    wordFile=open("wordlist.txt","r",errors="ignore")
    body=wordFile.read().lower()
    words=body.split("/n")
    for i in range(len(words)):
        mywords=words[i]
        result=pdfReader.decrypt(mywords)
        if result==1:
            print("success,the password is"+mywords)
        elif result==0:
            tried+=1
            print("password tired"+str(tried))
            continue

            


