# Knapsack
Items = {
    1 : [3,10],
    2 : [5,4],
    3 : [6,9],
    4 : [2,11]
} # item : [weight,value]
W = 7
def Knapsack(Items,W):
    num_items = len(Items)
    matrix = [[0]*(W+1)] 
    for i in range(1,num_items+1):
        row = [0]
        for w in range(1,W+1):
            if Items[i][0] > w:
                row += [matrix[i-1][w]] 
            else:
                row += [max( matrix[i-1][w], Items[i][1] + matrix[i-1][w-Items[i][0]] )]
        matrix.append(row)
    for row in matrix:
        for element in row:
                print('{0:<3}'.format(element), end='')
        print()
    return matrix[num_items][W]
def find_sol(i = len(Items),k = W):
    while i != 0 or k != 0:
        if matrix[i][k] >= matrix[i-1][k]:
            
max_val = Knapsack(Items,W)
print ("Max capacity is : ",max_val)
