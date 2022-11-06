# url : https://school.programmers.co.kr/learn/courses/30/lessons/120897


'''
문제 : 정수 n이 매개변수로 주어질 때, n의 약수를 오름차순으로 담은 배열을 return하도록 solution 함수를 완성해주세요.

'''

def solution(n):
    answer = []
    sqrt = n ** (1/2) 
    for i in range(1, int(sqrt) +1):
        if n % i == 0 : answer += [n // i, i]
    return sorted(list(set(answer)))