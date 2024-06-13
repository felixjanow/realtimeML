import numpy as np
import functions

class neuron():
    def __init__(self):
        self.matrix = np.zeros((3,3))
        #zero is neutral, 1 is output, -1 is input
        self.path_state = np.zeros((3,3))
        self.activated = False
    def return_matrix(self):
        return self.matrix
    def populate_index(self,i,j,value):
        self.matrix[i+1,j+1] = value

class network():
    def import_network(self, filename):
        values = []
        i = 0
        j = 0
        f = open(filename,"r")
        for line in f:
            end_index = 0
            row_array = []
            j = 0
            while line[end_index] != "\n":
                single_value = ""
                while line[end_index] != "\t":
                    single_value = single_value + line[end_index]
                    end_index = end_index+1
                end_index = end_index + 1
                row_array.append(float(single_value))
                j = j + 1
            values.append(row_array)
            i = i + 1
        self.activations = np.zeros((i,j))
        f.close()
        result = np.array(values)
        self.matrix = result
        self.states = np.zeros((i,j))
    def output_network(self,filename):
        f = open(filename, "w")
        shape = self.matrix.shape
        n_i = shape[0]
        n_j = shape[1]
        for i in range(0,n_i):
            line_string = ""
            for j in range(0,n_j):
                line_string = line_string + str(self.matrix[i,j]) + "\t"
            f.write(line_string + "\n")
        f.close()
    def return_shape(self):
        return self.matrix.shape

    def import_initial_values(self, filename):
        values = []
        f = open(filename,"r")
        row_count = 0
        for line in f:
            end_index = 0
            row_array = []
            column_count = 0
            while line[end_index] != "\n":
                single_value = ""
                while line[end_index] != "\t":
                    single_value = single_value + line[end_index]
                    end_index = end_index + 1
                end_index = end_index + 1
                value = float(single_value)
                if value != 0:
                    self.activations[(row_count,column_count)] = 1
                row_array.append(value)
                column_count = column_count + 1
            values.append(row_array)
            row_count = row_count + 1
        f.close()
        result = np.array(values)
        self.values = result
        print(self.activations)

    def step_forward(self):
        n_neurons_i = int( (self.matrix.shape[0] - 1)/2 )
        n_neurons_j = int( (self.matrix.shape[1] - 1)/2 )

        #determine the state of each neuron
        for i in range(0,n_neurons_i):
            for j in range(0,n_neurons_j):
                neuron_i = 2*i + 1
                neuron_j = 2*j + 1
                output_sum = 0

                if self.states[(neuron_i,neuron_j)] == 0:
                    for k in range(0,8):
                        path_index_i = functions.path_order_render(k)[0] + neuron_i
                        path_index_j = functions.path_order_render(k)[1] + neuron_j
                        path_state = self.activations[path_index_i,path_index_j]
                        if (path_state == 1):
                            self.states[(neuron_i,neuron_j)] = 1

        #calculate nueron behavior based on its state
        for i in range(0,n_neurons_i):
            for j in range(0,n_neurons_j):
                neuron_i = 2*i + 1
                neuron_j = 2*j + 1
                #input state
                if self.states[(neuron_i,neuron_j)] == 1:

                    # input contribution of each input connection
                    sum = 0
                    for k in range(0,8):
                        path_index_i = functions.path_order_render(k)[0] + neuron_i
                        path_index_j = functions.path_order_render(k)[1] + neuron_j
                        path_state = self.activations[path_index_i,path_index_j]
                        if (path_state == 1):
                            sum = sum + self.values[path_index_i,path_index_j]*self.matrix[path_index_i,path_index_j]
                            self.values[path_index_i,path_index_j] = 0

                    #output of the neuron
                    self.values[neuron_i,neuron_j] = functions.softmax(sum)*self.matrix[neuron_i,neuron_j]

                    #output values of the output connections
                    for k in range(0,8):
                        path_index_i = functions.path_order_render(k)[0] + neuron_i
                        path_index_j = functions.path_order_render(k)[1] + neuron_j
                        path_state = self.activations[path_index_i,path_index_j]
                        if (path_state == 0):
                            self.values[path_index_i,path_index_j] = self.values[neuron_i,neuron_j]*self.matrix[path_index_i,path_index_j]

                    #flip the states of each connection
                    for k in range(0,8):
                        path_index_i = functions.path_order_render(k)[0] + neuron_i
                        path_index_j = functions.path_order_render(k)[1] + neuron_j
                        path_state = self.activations[path_index_i,path_index_j]
                        if (path_state == 0):
                            self.activations[path_index_i,path_index_j] = 1
                        else:
                            self.activations[path_index_i,path_index_j] = 0

                    self.states[(neuron_i,neuron_j)] = -1

                elif self.states[(neuron_i,neuron_j)] == -1:
                    self.states[(neuron_i,neuron_j)] = 0
                    for k in range(0,8):
                        path_index_i = functions.path_order_render(k)[0] + neuron_i
                        path_index_j = functions.path_order_render(k)[1] + neuron_j
                        self.activations[path_index_i,path_index_j] = 0
                        self.values[(path_index_i,path_index_j)] = 0
                    self.values[(neuron_i,neuron_j)] = 0
