def getfile(words compilation):
    with open (words compilation,encoding ="utf-8") as f:
        mots=text.split()
        syntax=.!?;:""-
        text= f.read()
        for count, mots in enumerate(mots):
            mots[count]=word.strip(syntax)
        return mots
def main()
    dict={}
    f=input('saisir le nom" ')
    if f == " "
       print)("desole")
    else:
        mots=words compilation(f)
        print(cherch(mots,dict))
        omni = input("puis-je saisir un mot avec la omni prefixe: ")
        if omni =" ":
            print('Probablement, vous s "etes trompes un petit peu")
        else:
            print(cherch numero 2(omni,dict))
        print(
                
def cherch (omni, vocab):
    if omni in dict:
        parole = dict[omni]
    else:
        dict= "Malheureusement, ce mot n'existe pas:("
    return parole

def cherch numero 2(mots,dict):
    count = 0
    for mot in dict:
        if mot[4:] == "omni":
            if mot in dict:
                dict[mot] +=1
            else:
                dict[mot] =1
            
    return dict

            

    
    

            


    
        
        
       
        
