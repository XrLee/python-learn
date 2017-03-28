import random
import string

def activation_code(id, length = 20):
	'''id + "L" + random code'''
	prefix = hex(int(id))[2:] + 'L'
	length = length - len(prefix)
	chars = string.ascii_letters + string.digits
	'''
	return prefix + ''.join([random.choice(chars) for i in range(length)])
	'''
	return prefix + ''.join(random.sample(chars,length))

def get_id(code):
	'''hex to demical string'''
	return str(int(code, 16))

if __name__ == '__main__':
	for i in range(1, 100, 10):
		code = activation_code(i)
		id = get_id(code.split('L')[0])
		print code,id
