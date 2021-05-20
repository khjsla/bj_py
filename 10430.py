import sys
#python3

A,B,C = map(int, sys.stdin.readline().split())
#첫 줄에, A,B,C 가 순서대로 주어진다.
# ==> map && split 으로 A,B,C 순서대로 입력

print((A+B)%C)
# 첫 줄 위에 출력
# 다음줄 다음에 출력
