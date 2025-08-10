import random

def main():
    
    dic_number = {}
    one= two= three= four= five= six= seven= eight= nine= ten = 0

    for i in range(100):

        number = random.randint(1, 10)
        
        #dic_number[number] = dic_number.get(number, 0)+1

        if number == 1:
            one+=1
            dic_number[1]=one
        elif number == 2:
            two+=1
            dic_number[2]=two
        elif number == 3:
            three+=1
            dic_number[3]=three
        elif number == 4:
            four+=1
            dic_number[4]=four
        elif number == 5:
            five+=1
            dic_number[5]=five
        elif number == 6:
            six+=1
            dic_number[6]=six
        elif number == 7:
            seven+=1
            dic_number[7]=seven
        elif number == 8:
            eight+=1
            dic_number[8]=eight
        elif number == 9:
            nine+=1
            dic_number[9]=nine
        else:
            ten+=1
            dic_number[10]=ten
    print(dic_number)
    
main() 