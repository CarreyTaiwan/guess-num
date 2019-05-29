# 產生一個隨機整數1~100 (不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出 "終於猜對了!"
# 猜錯的話 要告註他 比答案大/小

import random
start = input('請輸入隨機數字範圍開始值')
start = int(start)
end = input('請輸入隨機數字範圍結束值')
end = int(end)
r = random.randint(start, end)
count = 0
while True:
	num = input('請猜一數字: ')
	count += 1
	num = int(num)
	if  r == num:
		print('終於猜對了!')
		print('總共猜了', count ,'次')
		break
	elif num > r:
		print('比答案大')
	else:
		print('比答案小')
	print('總共猜了', count ,'次')