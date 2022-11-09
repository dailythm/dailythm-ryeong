# url : https://school.programmers.co.kr/learn/courses/30/lessons/120866


'''
문제 : 지뢰가 있는 지역과 지뢰에 인접한 위, 아래, 좌, 우 대각선 칸을 모두 위험지역으로 분류합니다.
      지뢰는 2차원 배열 board에 1로 표시되어 있고 board에는 지뢰가 매설 된 지역 1과, 지뢰가 없는 지역 0만 존재합니다.
      지뢰가 매설된 지역의 지도 board가 매개변수로 주어질 때, 안전한 지역의 칸 수를 return하도록 solution 함수를 완성해주세요.

'''

def solution(board):
    answer = 0
    leng = len(board)
    danger = [[0 for i in range(leng+2)] for i in range(leng+2)]
    for i in range(leng):
        for j in range(leng):
            if board[i][j] == 1:
                danger[i][j], danger[i][j+1], danger[i][j+2] = 1, 1, 1
                danger[i+1][j], danger[i+1][j+1], danger[i+1][j+2] = 1, 1, 1
                danger[i+2][j], danger[i+2][j+1], danger[i+2][j+2] = 1, 1, 1
    for i in range(1, leng+1):
        for j in range(1, leng+1):
            if danger[i][j] == 0 : answer += 1
    return answer