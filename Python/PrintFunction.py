def printFunc(n):
    if(n == 0): return
    printFunc(n - 1)
    print(n, end = "")

if __name__ == '__main__':
    n = int(input())
    printFunc(n)