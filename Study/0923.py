# A = int(input("输入:"))
# 输入数字还是字符都将被作为字符串读取，想要接收数值，需进行转换
for i in range(1, 10):
    for j in range(1,i + 1):
        print(str(i) + "*" + str(j) + "=" + str(i * j)+"  ",end="")
    #     使用  end=""  输出同一行
    print("\t")
