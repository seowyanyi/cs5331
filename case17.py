# Password lowercase and at most 6 chars. 
# Lets try to brute force.

import sys
import itertools
import hashlib
import string

MAX_ATTEMPTS = 308915776 # 26^6
salt = sys.argv[1]
password = sys.argv[2]


def get_hashed_password(plaintext):
    # Password is hashed twice - once on client and once on server
    return hashlib.sha512(hashlib.sha512(plaintext).hexdigest() + salt).hexdigest()


def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in itertools.chain.from_iterable(itertools.product(charset, repeat=i)
        for i in range(1, maxlength + 1)))

count = 0
for attempt in bruteforce(string.ascii_lowercase, 6):
    count += 1
    percentage_completion = float(count)/MAX_ATTEMPTS*100
    if count % 50000 == 0:
        print 'Brute force progress: {}%'.format(percentage_completion)
    if get_hashed_password(attempt) == password:
        print 'Actual plaintext password is: {}'.format(attempt)
        break    