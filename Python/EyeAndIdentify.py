import numpy as np

if __name__ == '__main__':
    a, b = (int(x) for x in input().split())
    np.set_printoptions(legacy='1.13')
    print(np.eye(a, b))