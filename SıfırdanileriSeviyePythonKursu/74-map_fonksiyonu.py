def double(x):
    return x * 2
# map fonk bize bir obje döndürüyor 
print(list(map(double,[1,2,3,4,5,6,7]))) # liste gönderdik
a  = map(lambda x : x**2,(1,2,3,4,5,6,7)) # demet gönderdik
print(list(a))

liste1 = [1,3,5]
liste2 = [2,4,6]
liste3 = [1,2,3,4,5,6]
b = list(map(lambda x,y : x*y,liste1,liste2))
print(b)

c = list(map(lambda x,y,z : x*y*z,liste1,liste2,liste3))
print(c)