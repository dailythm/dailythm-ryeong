# url : https://school.programmers.co.kr/learn/courses/30/lessons/120899


'''
문제 : 정수 배열 array가 매개변수로 주어질 때, 
      가장 큰 수와 그 수의 인덱스를 담은 배열을 return 하도록 solution 함수를 완성해보세요.

'''

def solution(array):
    big = 0
    for i in array:
        if big < i : big = i
    return [big, array.index(big)]