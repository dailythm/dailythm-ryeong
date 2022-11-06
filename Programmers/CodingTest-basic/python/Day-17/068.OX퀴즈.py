# url : https://school.programmers.co.kr/learn/courses/30/lessons/120907


'''
문제 : 덧셈, 뺄셈 수식들이 'X [연산자] Y = Z' 형태로 들어있는 문자열 배열 quiz가 매개변수로 주어집니다. 
      수식이 옳다면 "O"를 틀리다면 "X"를 순서대로 담은 배열을 return하도록 solution 함수를 완성해주세요.

'''

def solution(quiz):
    answer = []
    
    for i in quiz:
        arr = i.split(' ')
        if arr[1] =='-' : curr = int(arr[0]) - int(arr[2])
        else : curr = int(arr[0]) + int(arr[2])

        if str(curr) == arr[4]: answer.append("O")
        else : answer.append("X")

    return answer