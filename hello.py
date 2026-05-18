
#strip and title method are used to remove withspace and make the first letter capital 
# here i can use  . capitalize to capital only the first element of a string but title capitalize all the element
#split user name into first and last name 
# first,last = name.split(' ')
def main():
   name = input('what is your name? ').strip().title()
   hello(name)


def hello(to='world'):
    print(f'hellow, {to}')

# main()

students= ['raghib','rawnak','mehwar','gufran']


# for student in students:
#     print(student)
for i in range(len(students)):
    print(i+1, students[i])
