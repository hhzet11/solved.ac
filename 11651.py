n = int(input())
arr = []
for i in range(n):
    x, y = map(int, input().split())
    arr.append([y, x])
arr = sorted(arr)
for y, x in arr :
    print(x, y)