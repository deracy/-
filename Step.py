N = int(input())
people = list(map(int,input().split()))
ans = 0
MaxNum = 0
for i in range(N):
    MaxNum = max(MaxNum, people[i])
    B = MaxNum
    ans += B-people[i]

print(ans)
