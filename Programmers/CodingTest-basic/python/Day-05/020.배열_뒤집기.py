# url : https://school.programmers.co.kr/learn/courses/30/lessons/120821


'''
문제 : 정수 배열 numbers가 매개변수로 주어집니다.  
      numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

'''

def solution(num_list):
    answer = []
    length = len(num_list)
    for i in range(0, length, 1):
        answer.append(num_list.pop())
    return answer

# def solution(num_list):
#     num_list.reverse()
#     return num_list