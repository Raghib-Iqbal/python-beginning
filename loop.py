students=[
    {'name':'raghib','home': 'kazipara'},
    {'name':'rawnak','home': 'kazipara'},
    {'name':'gufran','home': 'dhaka'}

]
# for student in students:
#     print(student['name'],student['home'],sep=' , ')


# for i in range(3):
  
#     for j in range(3):
#         print('*', end='')
#     print('')
def main():
    print_square(3)
    print_column(3)

def print_square(num):
    for i in range(num):
        print_column(num)
        print()


def print_column(num):
    for i in range(num):
        print('#',end='')


main()