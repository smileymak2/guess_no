import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1
	num = input('請輸入數字: ')
	num = int(num)
	if num == r:
		print('猜對了!!!')
		print('你猜了第', count, '次')
		break
	elif num > r:
		print('太大了')
	elif num < r:
		print('太細了')
	print('你猜了第', count, '次')

