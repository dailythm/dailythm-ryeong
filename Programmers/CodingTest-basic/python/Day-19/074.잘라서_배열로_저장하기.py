# url : https://school.programmers.co.kr/learn/courses/30/lessons/120913


'''
문제 : 문자열 my_str과 n이 매개변수로 주어질 때, my_str을 길이 n씩 잘라서 저장한 배열을 return하도록 solution 함수를 완성해주세요.

'''

def solution(my_str, n):
    answer = []
    while len(my_str) > n :
        answer.append(my_str[0:n])
        my_str = my_str[n:]
    answer.append(my_str)
    return answer