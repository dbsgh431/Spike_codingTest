
def generate_arr_xy():
    """
    x행 y열에 해당 하는 2차원 int형 리스트를 반환
    """
    x, y = map(int, input("행과 열을 입력하세요: ").split())
    arr = []
    for i in range(x):
        print(f'{i+1}행의 {y}개의 수를 입력 :')
        row = input()
        arr.append(list(map(int, row)))
    return arr