i=1
result = 0
A= []
while i < 100 :
    i= i+1
    if i % 2 ==1 :
        # print(i)
        A.append(i)
# 저장된 값들의 합을 구함


print(sum(A))

print(A)


# 해답
# 더하는 법 이해불가
for x in A :
    result = result + x
    print(result)
