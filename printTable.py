def printTable(table):
    colWidth = [0] * len(table)
    y = 0
    
    # colWidth记录每个列表中的最大的字符串长度
    for i in range(len(table)):
        for j in range(len(table[i]) - 1):
            big_num = len(table[i][j])
            
            if len(table[i][j]) < len(table[i][j + 1]):
                big_num = len(table[i][j+1])
            if colWidth[i] < big_num:
                colWidth[i] = big_num
    
    # 选出colWidth的最大值
    for x in range(len(colWidth) - 1):
        max_num = colWidth[x]
        
        if colWidth[x] < colWidth[x + 1]:
            max_num = colWidth[x + 1]
        if y < max_num :
            y = max_num
    
    # 对每个列表中的字符串进行右对齐并进行拼接
    for i in range(len(table)):
        for j in range(len(table[i])):
            print(table[i][j].rjust(20),end='')        
        print('')
        
tableData = [
['apples', 'oranges', 'cherries', 'banana'],
['Alice', 'Bob', 'Carol', 'David'],
['dogs', 'cats', 'moose', 'goose']]

printTable(tableData)