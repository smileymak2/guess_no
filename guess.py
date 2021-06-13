import random
start = input('請輸入開始的隨機數: ')
end = input('請輸入結束的隨機數: ')
start = int(start)
end = int(end)

r = random.randint(start, end)
count = 0
guessstart = start
guessend = end
while True:
	print('答案在', guessstart, '至', guessend, '之間')
	num = input('請輸入數字: ')
	num = int(num)
	if num < guessstart or num >guessend:
		print('輸入錯誤, 請重新輸入: ')
	else:
		count += 1
		if num == r:
			print('猜對了!!!')
			print('你猜了第', count, '次')
			break
		elif num > r:
			print('太大了')
			guessend = num
		elif num < r:
			print('太細了')
			guessstart = num
		print('你猜了第', count, '次')

