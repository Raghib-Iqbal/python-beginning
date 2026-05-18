
def main():
    x =get_int('what\'s x? ')
    print(f'x is {x}')



def get_int(promt):
    while True:
        try:
            x= int(input(promt))
            return x
        except ValueError:
            # print('x in not intager') # what is raise keyword here i don't know 
            pass
        
    

main()


