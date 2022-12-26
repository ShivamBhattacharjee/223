import time
import zipfile

folderpath = input("enter file path:")
myfolderPath = folderpath.strip()

zipfolder = zipfile.ZipFile(myfolderPath)
print(zipfolder)

if not zipfolder:
    print("the zipped folder is not protected")
else:
    startTime = time.time()
    result = 0
    combination = 0
    characters = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'l', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                  'K', 'L', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<', '}', '{', '^', '[', ']', ' ', '+', '-', '_', '&', ';', '"', '?', '`', "'", '\\']

    if result==0:
        print("checking for 4 characters password")
        print("Brute force Attack")
        for i in characters:
            for j in characters:
                for k in characters:
                    for l in characters:
                        guess=str(i)+str(j)+str(k)+str(l)
                        password=guess.encode("utf-8").strip()
                        combination=combination+1
                        print(combination)
                        try:
                            with zipfile.ZipFile(myfolderPath,'r') as f:
                                zipfolder.extractall(pwd=password)
                                print("success! the password is"+guess)
                                endtime=time.time()
                                result+=1
                                break

                        except:
                            pass
                    if result==1:
                        break
                if result==1:
                    break
            if result==1:
                break
        if result==0:
            duration=endtime-startTime
            print("sorry the password is not found")
        else:
            duration=endtime-startTime
            print("congrats!password found after trying"+str(combination)+"combination in"+str(duration))