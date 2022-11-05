# url : https://school.programmers.co.kr/learn/courses/30/lessons/120846


'''
문제 : 약수의 개수가 세 개 이상인 수를 합성수라고 합니다. 
      자연수 n이 매개변수로 주어질 때 n이하의 합성수의 개수를 return하도록 solution 함수를 완성해주세요.

'''

def solution(n):
    answer = 0
    for i in range(1, n +1):
        for j in range(2, int(i ** (1/2)) +1):
            if i % j == 0:
                answer += 1
                break
    return answer