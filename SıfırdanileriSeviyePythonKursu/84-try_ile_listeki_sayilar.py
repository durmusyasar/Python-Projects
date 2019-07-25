liste = ["345","sadas","324a","14","kemal"]

for eleman in liste:
    
    try: 
        eleman = int(eleman) # Eğer hata ile karşılaşırsak burası hata verecek ve print çalışmayacak.
        print(eleman)
    except:
        pass # pass deyimi bir blokun hiçbir şey yapmadığı anlamına geliyor. Python'ın hata vermemesi için kullanabilirsiniz.