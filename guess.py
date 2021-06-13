import random
r = random.randint(1, 100)
while True:
	num = input('請輸入數字: ')
	num = int(num)
	if num == r:
		print('猜對了!!!')
		break
	elif num > r:
		print('太大了')
	elif num < r:
		print('太細了')

