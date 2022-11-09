# url : https://school.programmers.co.kr/learn/courses/30/lessons/120864


'''
문제 : 문자열 my_string이 매개변수로 주어집니다. 
      my_string은 소문자, 대문자, 자연수로만 구성되어있습니다. 
      my_string안의 자연수들의 합을 return하도록 solution 함수를 완성해주세요.

'''

def solution(my_string):
    answer = 0
    arr = []
    check = False
    for i in my_string :
        if i.isdigit() and check : 
            arr[-1] += i
        elif i.isdigit() :
            arr.append(i)
            check = True
        else : check = False
    for i in arr : answer += int(i)
    return answer