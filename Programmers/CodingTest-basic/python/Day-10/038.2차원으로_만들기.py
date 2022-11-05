# url : https://school.programmers.co.kr/learn/courses/30/lessons/120842


'''
문제 : 정수 배열 num_list와 정수 n이 매개변수로 주어집니다. 
      num_list의 원소들을 앞에서부터 n개씩 나눠 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요. 


'''

def solution(num_list, n):
    answer = []
    for i in range(1, len(num_list), n):
        answer.append(num_list[i -1: i + n -1])
    return answer