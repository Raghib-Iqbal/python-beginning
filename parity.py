from datetime import datetime
# def main():
#     x= int(input('what is x ?'))
#     if is_even(x):
#         print('Even')
#     else:
#         print('odd')

# # def is_even(n):
# #     if n%2==0:
# #         return True
# #     else:
# #         return False

# def is_even(n):
#     return n%2==0
# main()      

time_str = "7:54 pm"

# Method 1: String manipulation (destructure into parts)
time_part, period = time_str.split()
hour, minute = map(int, time_part.split(':'))
hm= hour+minute/60
if period=="pm":
    hm += 12
print(f"Hour: {hour}, Minute: {minute}, Period: {hm}")
# # Method 2: Convert to a 24-hour datetime object
# time_obj = datetime.strptime(time_str, "%I:%M %p").time()
# print(f"24-Hour Object: {time_obj.strftime('%H:%M:%S')}")

