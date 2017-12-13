# -*- coding: utf-8 -*-

def two_arrays():

    """
    X-array -- strings
    Y-array -- queries
    for each query in Y-array the program counts queries in X-array

    input from console or from a file ('absolute path')

    """

    a = raw_input("Ввод с клавиатуры (y/n): ")

    if a == 'y':
        lst_1 = [raw_input() for i in range(int(raw_input()))] # X
        lst_2 = [raw_input() for j in range(int(raw_input()))] # Y
        for i in lst_2:
            print lst_1.count(i)
    else:
        lst = [line.strip() for line in open(raw_input("Путь к файлу: "))]
        tmp = int(lst[0])

        lst_strings = lst[1:tmp+1] # X
        lst_queries = lst[tmp+2:]  # Y

        for i in lst_queries:
            print lst_strings.count(i)


two_arrays()
