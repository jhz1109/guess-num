import random
r = random.randint(1, 100)
count = 0
while True:
    num = input('請輸入數字:')
    num = int(num)    
    count += 1  #count = count + 1
    if num == r:
	    print("恭喜你猜對了!")
	    print('你已經猜了', count, '次')
	    break
    elif num > r:
	    print('再小一點!')
    elif num < r:
	    print('再大一點!') 
    print('你已經猜了', count, '次')

