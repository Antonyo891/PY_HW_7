'''Таблица умножения'''
def Print_operation_table(operation, num_rows=6, num_columns=6):
    rows_list1:list=[item for item in range(1,num_rows+1)]
    columns_list2:list=[item for item in range(1,num_columns+1)]
    for i in rows_list1:
        for j in columns_list2:
            if operation(i,j)//10==0:
                print(operation(i,j),end='   ')
            else:
                print(operation(i,j),end='  ')
        print()



Print_operation_table(lambda x,y:x*y)