# url : https://school.programmers.co.kr/learn/courses/30/lessons/120814


'''
문제 : 정수 배열 numbers가 매개변수로 주어집니다.  
      numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

'''

def solution(numbers):
    total = 0
    for i in numbers:
        total += i
    return total / len(numbers)
        