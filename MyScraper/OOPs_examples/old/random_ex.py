import random
import string

get_letters = string.ascii_lowercase
get_numbers = string.digits
random_str = ''
for _ in range(3):
    random_str = random_str + str(random.choice(get_letters+get_numbers))

# print(str2)
# print(str3)
# print(str1)
