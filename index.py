import sys

# the raise keyword


# def main():
#     pace = get_pace(mile=26.7, minutes=180)
#     print(f'you need to run each mile in {round(pace,2)} minites')


# def get_pace(mile, minutes):
#     if not minutes > 0:
#         raise ValueError('minutes must be greater than 0')

#     return minutes/mile

# main()

# tuples


def tuples():
    cordinates = (45.1245, 65.3256)
    cordinates_arr=[45.1245,65.3256]
    print(f"{sys.getsizeof(cordinates_arr)}")
    # print(cordinates[0],cordinates[1],sep=' &&& ')

tuples()
