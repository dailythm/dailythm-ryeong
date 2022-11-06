# url : https://school.programmers.co.kr/learn/courses/30/lessons/120890


'''
문제 : 정수 배열 array와 정수 n이 매개변수로 주어질 때, 
      array에 들어있는 정수 중 n과 가장 가까운 수를 return 하도록 solution 함수를 완성해주세요.

'''

def solution(array, n):
    answer = 0
    maxDiff = 100
    array = sorted(array)
    for i in array:
        diff = int(((n - i) ** 2) ** (1/2))
        if diff < maxDiff: 
            maxDiff = diff
            answer = i
    return answer