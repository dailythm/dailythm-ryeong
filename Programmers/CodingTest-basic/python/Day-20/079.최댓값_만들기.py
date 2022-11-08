# url : https://school.programmers.co.kr/learn/courses/30/lessons/120862


'''
문제 : 정수 배열 numbers가 매개변수로 주어집니다. 
      numbers의 원소 중 두 개를 곱해 만들 수 있는 최댓값을 return하도록 solution 함수를 완성해주세요.

'''

def solution(numbers):
    sort = sorted(numbers)
    if sort[0] * sort[1] > sort[-1] * sort[-2]:
        return sort[0] * sort[1]
    else : return sort[-1] * sort[-2]