arr = list(map(int,input().split()))
count = 0

for i in range(len(arr)):
    if arr[i] == 1:
        count += 1

print(count if count < len(arr)/2 else len(arr) - count)
