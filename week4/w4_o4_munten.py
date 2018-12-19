def paymentOptions(eurocent):
    m = [1,2,5,10,20,50,100,200,500,1000,2000,5000,10000]
    i = 0
    result = []

    while(True):
        if len(m) > i and m[i] <= eurocent:
            temp = [None]*(eurocent+1)
            result.append(temp)
            for j in range(len(result[i])):
                if i == 0 or j == 0:
                    result[i][j] = 1
                elif j >= m[i]:
                    result[i][j] = result[i-1][j] + result[i][j-m[i]]
                elif j < m[i]:
                    result[i][j] = result[i-1][j]
            i += 1
        else:
            i -= 1
            break
    print(result)
    return result[i][len(result[i])-1]

print(paymentOptions(7))