import random
import string 

def generate_random_string(length):
    pwcharacters = string.ascii_lowercase + string.digits + string.punctuation
    result = ''.join(random.choice(pwcharacters)for i in range(length))
    print("Your password is:", result)

pw_length = input('Please enter desired password length: ')
pw_num = int(pw_length)

while True:
      if pw_num >= 8 and pw_num <= 20:
        generate_random_string(pw_num)
        break
      else:
        if pw_num < 8:
            pw_length = input("Your password is too short, try again: ")
            pw_num = int(pw_length)
            continue
        elif pw_num > 20:
            pw_length = input("Your password is too long, try again: ")
            pw_num = int(pw_length)
            continue


    