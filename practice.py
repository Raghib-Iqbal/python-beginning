
# indoor.py    0 0 
# x=input('').strip().lower()
#print(x);


#plaback.py 0 1


# print(x.replace(' ','...'))

# making faces 0 2
# x= x.replace(':)',' 😐')


# einstien 0 3
# x= int((input('m: ')))
# print(f'E: {x*pow(3*10**8,2)}')

# tip calculate 0 4 
# def main():
#     dollars = dollars_to_float(input("How much was the meal? "))
#     percent = percent_to_float(input("What percentage would you like to tip? "))
#     tip = dollars * percent
#     print(f"Leave ${tip:.2f}")


# def dollars_to_float(d):
#     return float(d.replace('$',''))



# def percent_to_float(p):
#     return float(p.replace('%',''))/100

# main()


# Deep Thought 1 0

# x= input('What is the Answer to the Great Question of Life, the Universe, and Everything?')


# if x=='42' or x=='forty-two' or x=='forty two':
#     print('Yes')
# else :
#     print('No')


# Home Federal Savings Bank 1 1

# x= input('Greeting :').strip().capitalize()

# if x.find('hello')!=-1:

#     print('$ 0')
# elif x[0]=='h' or x[0]=='H':
#     print('$ 20')
# else:
#     print('$ 100')

                                                                # name= 'hellow raghib' reverser something
                                                                # print(name[::-1])

# File Extensions 1 2


# x=input('File name: ')
# y= x[(x.find('.')+1):]
# print(f'Image/{y}')

# Math Interpreter 1 3
################### method 1
# ex=input('Expression: ')
# print(eval(ex))
  
################## method 2
# ex = input('Expression: ') 
# num1, y, num2 = float(ex[0]), ex[1], float(ex[2]) 
# if y == '+':
#     result = num1 + num2
# elif y == '-':
#     result = num1 - num2
# elif y == '*':
#     result = num1 * num2
# elif y == '/':
#     result = num1 / num2
# else:
#     result = "Invalid operator"
# print(result)



# Meal Time 1 3      
# def main():
#     time =input('what\'s time it is ?')
#     print(convert(time))



# def convert(time):
#     hour,minite=time.split(':')
#     hour=float(hour)
#     minite=float(minite)
#     hM= hour+minite/60
#                      # the am pm part is in the parity file
#     if 7<=hM<=8:
#         return 'breakfast time'
#     elif 12<=hM<=13:
#         return "lunch time"
#     elif 18<=hM<=19:
#         return 'dinner time'

# if __name__ == "__main__":
#     main()



# camelCase 2 0 camel.py
# name=input('camelCase :')

# result=''
# for s in name:
#     if s.isupper():
#         s='_'+s.lower()
#     result+=s


# print(f"snack_case :{result}")


# Coke Machine 2 1 coke.py

# print('Amount Due :50')
# price=50
# while True:
#     amount=int(input('Insert Coin :'))
#     if amount==5 or amount==10 or amount==25:
#         price -= amount
#     if price<=0:
#         print(f'Change Owned: {price*-1}')
#         break
#     print(f'Amount Due :{price}')
     
#Just setting up my twttr 2 2 twttr
# string=input('Input :')

# result=''

# for s in string:
#     if s=='a' or s=='e' or s=='i' or s=='o' or s=='u':
#         result+=''
#     else:
#         result+=s
 

# print(f'Output : {result}')

# Vanity Plates 2 3 plates.py
# import string
# def main():
#     plate = input("Plate: ")
#     if is_valid(plate):
#         print("Valid")
#     else:
#         print("Invalid")

# def is_valid(s):
#     Ftwo=s[0:2]
#     # 1. Check for any punctuation
#     has_punct = any(char in string.punctuation for char in s)

#     # 2. Check for spaces
#     has_space = ' ' in s
#      # 3. Check for numbers
#     has_number = any(char.isdigit() for char in s)

#     if 2<=len(s)<=6 and has_punct==False and has_space==False:

#         if(Ftwo.isdigit()==False):
#             if(has_number and s[-1].isdigit()==False):
#                 return False
#             else:
#                 return True

#         else:
#             return False

#     else:
#         return False

# main()

# Nutrition Facts 2 4 nutrition.py

items=[
      {'name':'Apple','calories':130},
        {'name':'Banana','calories':110},
      {'name':'Avocado','calories':50},
     {'name':'Cantaloupe','calories':50},
]
x= input('Item :').strip().title()

for item in items:
    if item['name']== x:
        print(f'Calories :{item["calories"]}')

