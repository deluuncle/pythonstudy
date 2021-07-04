#有1 2 3 4 这4个数字，将其排列为互补相同的三位数，一共可以排成多少个
i = 0
for j in [1,2,3,4]:
    for n in [1,2,3,4]:
        for M in [1,2,3,4]:
            if j != n and n !=M:
                print(j,n,M)
                i += 1


print("done")
print("一共有{}个不同的三位数".format(i))

