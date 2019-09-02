#https://programmers.co.kr/learn/courses/30/lessons/12899
num_list = [4,1,2]
def solution(n):
	total = 0
	digit = 0
	while (n>total):
		digit += 1
		total = total+pow(3,digit)
	quotient = n//3
	remain = n%3
	answer = ''
	if digit > 1:
		answer = str(num_list[remain]) + answer
		i=1
		while 1:
			if remain == 0 and quotient != 0:
				quotient -= 1
			if quotient >= 3:
				remain = quotient%3
				quotient //= 3
				if i < digit-1:
					answer = str(num_list[remain]) + answer
			else:
				break
			i+=1

		answer = str(num_list[quotient]) + answer
	else:
		answer = str(num_list[remain])
	return answer
