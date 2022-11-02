

count=0
somma=0
media=0
numero=0


while True:
    numero=(int(input("inserisci un numero")))
    if numero !=0:
        count += 1
        somma +=numero    

    if count > 0:
        media=somma/count
        print( media )
    if numero == 0:
        break    
        

    



