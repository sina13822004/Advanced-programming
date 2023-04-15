def test(d: dict):
    max_1 =list(d.items())[0][1] ,min_1 = list(d.items())[0][1]
    for i in range(len(d)):
        if list(d.items())[i][1] < min_1:
            min_2 = list(d.items())[i][0]
        if list(d.items())[i][1] > max_1:
            max_2 = list(d.items())[i][0]
    return (max_2, min_2)



