# url : https://school.programmers.co.kr/learn/courses/30/lessons/120847


'''
문제 : 정수 배열 numbers가 매개변수로 주어집니다. 
      numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

'''

def solution(numbers):
    n1, n2 = 0, 0
    for i in numbers:
        if i > n1 :
            n2 = n1
            n1 = i
        elif i > n2 :
            n2 = i
    return n1 * n2