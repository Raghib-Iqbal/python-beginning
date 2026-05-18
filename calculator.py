def main():
   x= int(input('what x ? '))
   print(f'the square of {x} is {square(x)}')

def square(n):
    return pow(n,2)

main()       
# y= input('what y ? ')
# y = float(y)
# z= x/y # you can use round(x/y,2) for the exact same thing
# print(f'{z:.2f}')
# #   :,     syntax is for comma  <<<<<  z:.2f   to show 2 digit after decimel>>>>>>