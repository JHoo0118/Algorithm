# https://programmers.co.kr/learn/courses/30/lessons/42577

phone_book = ["119", "97674223", "1195524421"]

def solution(phone_book):
    phone_book.sort()
    for p1, p2 in zip(phone_book, phone_book[1:]):
        print(p1, p2)
        if p2.startswith(p1):
            return False
    return True

print(solution(phone_book))