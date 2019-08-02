import json
import random
import os
import string

char = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = os.urandom(1024)

names = json.loads(open('names.json').read())

for name in names:
    extra_name = ''.join(random.choice(string.digits))
    userName = name.lower() + extra_name + "@yahoo.com"
    password = ''.join(random.choice(char) for i in range(8))
    print("trying " + userName + "    " + password)
