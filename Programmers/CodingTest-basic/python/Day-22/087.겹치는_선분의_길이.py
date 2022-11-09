# url : https://school.programmers.co.kr/learn/courses/30/lessons/120876


'''
문제 : 빨간색, 초록색, 파란색 선분이 x축 위에 있습니다. 
      세 선분의 x좌표 시작과 끝이 [[start, end], [start, end], [start, end]] 형태로 들어있는 2차원 배열 lines가 매개변수로 주어질 때, 
      두 개 이상의 선분이 겹치는 부분의 길이를return 하도록 solution 함수를 완성해보세요.

'''

def solution(lines):
    answer = 0
    pointList = []
    for i in lines:
        for j in range(i[0],i[1]):
            pointList.append(j)
    numList = set(pointList)
    print(numList)
    for i in numList:
        if pointList.count(i) > 1 : answer += 1
    return answer