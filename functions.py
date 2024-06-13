import math
import numpy as np

def d2r(degrees):
    return (math.pi/180)*degrees

def path_order_render(n: int) -> tuple[int, int]:
    return (
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1)
    )[n]

def import_network(filename):
    values =[]
    f = open(filename,"r")
    for line in f:
        end_index = 0
        row_array = []
        while line[end_index] != "\n":
            single_value = ""
            while line[end_index] != "\t":
                single_value = single_value + line[end_index]
                end_index = end_index+1
            end_index = end_index + 1
            row_array.append(float(single_value))
        values.append(row_array)
    f.close()
    return np.array(values)

def output_network(filename,np_array):
    f = open(filename, "w")
    shape = np_array.shape
    n_i = shape[0]
    n_j = shape[1]
    for i in range(0,n_i):
        line_string = ""
        for j in range(0,n_j):
            line_string = line_string + str(np_array[i,j]) + "\t"
        f.write(line_string + "\n")
    f.close()

def softmax(x):
    return 1/(1+math.exp(-x))
