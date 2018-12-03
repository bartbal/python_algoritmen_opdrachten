def getFrequentie(fileName):
    dictionary = {}
    f=open(fileName, 'r')
    if f.mode == 'r':
        contents = f.readlines()
        for line in contents:
            word = ''
            for letter in line:
                if letter.isalpha():
                    word += letter
                elif word != '':
                    if word in dictionary:
                        dictionary[word] += 1
                    else:
                        dictionary[word] = 1
                    word = ''
        
        WriteDict(dictionary)   

    else:
        print('can\'t read file', fileName)
        return False

def WriteDict(d):
    file = open('result.txt','w') 
    for key, value in d.items():
        line = str(key) + ':' + str(value) + '\n'
        file.write(line)

getFrequentie('tekst')