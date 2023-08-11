import sys


def generate_N_list():
    """
    # input
    N 입력
    공백없이 N개의 수 입력
    
    # return
    N개의 원소를 가지는 리스트 반환
    """
    N = int(input())
    N_list = list(map(int,sys.stdin.readline().rstrip()))

    return N_list[0:N]


def generate_N_list_with_space():
    """
    # input
    N 입력
    N개의 수를 빈칸을 두고 입력
    
    # return
    N개의 원소를 가지는 리스트 반환
    """
    N = int(input())
    N_list = list(map(int,sys.stdin.readline().split()))

    return N_list[0:N]

