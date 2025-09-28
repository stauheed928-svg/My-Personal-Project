# Pass Word Generating 
import random
import string

s1 = string.ascii_uppercase
s2 = string.ascii_lowercase
s3 = string.digits
s4 = string.punctuation
s5 = s1+s2+s3+s4

s =[]
s.extend(s5)
generated_password = random.shuffle(s)

print("".join(s[0:8]))

