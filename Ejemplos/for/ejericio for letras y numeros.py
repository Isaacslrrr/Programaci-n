
# for contador in range (0,10):

# for contador in string:
    
var1="hol3 que t88l"
cont_num=0
cont_letra=0

for contador in range(0,len(var1)):
    if var1[contador].isnumeric():
        cont_num+=1
    if var1[contador].isalpha():
        cont_letra+=1
        
print("El total de letras es", cont_letra)
print("El total de números es", cont_num)     
