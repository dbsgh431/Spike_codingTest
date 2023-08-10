import sys


def generate_N_list():
    """
    N개의 원소를 가지는 리스트 반환
    """
    N = int(input())
    N_list = list(map(int,sys.stdin.readline().rstrip()))

    return N_list[0:N]
