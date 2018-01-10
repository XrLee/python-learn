""" this is a function to generate activation code"""

import random
import string

def activation_code(user_id, length=20):
    """the form of activation code is id + "L" + random code

    Args:
    user_id: string, the id of user
    length: the length of the activation code

    """
    prefix = hex(int(user_id))[2:] + 'L'
    length = length - len(prefix)
    chars = string.ascii_letters + string.digits

    '''
    return prefix + ''.join([random.choice(chars) for i in range(length)])
    '''
    return prefix + ''.join(random.sample(chars, length))

def get_id(code):
    '''hex to demical string'''
    return str(int(code, 16))

if __name__ == '__main__':
    for i in range(1, 100, 10):
        CODE = activation_code(i)
        ID = get_id(CODE.split('L')[0])
        print CODE, ID
