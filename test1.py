# Example file showing a basic pygame "game loop"
import pygame
import numpy as np
import math
import functions
import classes

# pygame setup
pygame.init()
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
running = True

#sim setup
n_i = 8
n_j = 8
neuron_distance = 60
neuron_offset = 60
neuron_radius = 20


#n1 = classes.neuron()
#n1.populate_index(-1,-1,25)
#print(n1.return_matrix())

# setup the structures of all the neuron_distance
#neuron_array = []
#for i in range(0,n_i):
#    row_array = []
#    for j in range(0,n_j):
#        row_array.append(classes.neuron())
#    neuron_array.append(row_array)

#print(neuron_array[1][1].return_matrix())
#boolean for checking if key is already is_pressed
is_pressed = False

#initial conditions of network
network = classes.network()
network.import_network("network.net")
network.import_initial_values("initial_values.val")
n_r = 0
n_b = 0
n_g = 0

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("blue")

    # RENDER YOUR GAME HERE
    flip_neurons = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and not(is_pressed):
        flip_neurons = True
        is_pressed = True
    if not(keys[pygame.K_RIGHT]):
        is_pressed = False
    # render the neurons
    if flip_neurons:
        network.step_forward()
        print("success")

    n_i = 8
    n_j = 8
    n_paths = 8
    i = 0
    j = 0
    while (i < n_i):
        while (j < n_j):
            neuron_i = 2*i + 1
            neuron_j = 2*j + 1
            light_level = network.values[(neuron_i,neuron_j)]
            n_r = int( light_level*255 )
            n_g = int( light_level*255 )
            n_b = int( light_level*255 )
            pygame.draw.circle(screen,(n_r,n_b,n_g),(neuron_offset + j*neuron_distance, neuron_offset + i*neuron_distance),neuron_radius)

            path_count = 0
            while path_count < n_paths:
                light_level = network.values[(neuron_i+functions.path_order_render(path_count)[0],neuron_j+functions.path_order_render(path_count)[1])]
                n_r = int( light_level*255 )
                n_g = int( light_level*255 )
                n_b = int( light_level*255 )
                pygame.draw.line(screen,(n_r,n_b,n_g),(neuron_offset + j*neuron_distance, neuron_offset + i*neuron_distance),( neuron_offset + (j + functions.path_order_render(path_count)[1])*neuron_distance, neuron_offset + (i + functions.path_order_render(path_count)[0])*neuron_distance ),4)
                path_count = path_count + 1

            j = j + 1
        j = 0
        i = i + 1


    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
