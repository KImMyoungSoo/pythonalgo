#https://programmers.co.kr/learn/courses/30/lessons/42577
def solution(phone_book):
    answer = True
    phone_book.sort()
    compare = phone_book[0]
    for phone in phone_book[1:]:
        if compare == phone[:len(compare)]:
            answer = False
            break
    return answer
