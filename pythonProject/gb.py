list = [100, 200, 400, 800, 1000, 1300]
# 최종값을 result에 저장할거야
result = 0

for index in list :
    result = result + index
    print(result)
avg= result/len(list)
print(avg)