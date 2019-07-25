liste = [1,2,3,4,5]

liste2 = [i for i in liste]
print(liste2)


###########################
liste3 = [i * 2 for i in liste]
print(liste3 )

#############################
liste4 = [(1,2),(3,4),(5,6)]

liste5 = [i * j for i,j in liste4]

print(liste5)


###############################

s = "python"

listes = [i * 3 for i in s]
print(listes)