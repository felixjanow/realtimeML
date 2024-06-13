This is an early prototype of a Machine Learning system that uses a time-stepped approach, meaning the calclations done in the neuron space can occur independantly of each other, potentially leading to more adaptive and life-like behavior than the current linear left-to-right approach used in modern models.
The classes and functions files contain methods for inputting and exporting the state of the network, as well as importing initial conditions. 
In the uploaded example, an 8x8 neuron grid is initialized with activations on the left side (this can be changed by modifying the "initial conditions" file). Pressing the right arrow key will continue the time step, allowing the user to visually analyze the behavior of the 2d network. 
This is a primitive prototype, but here are some developments that will need to happen to continue the project:
  1. Increasing the spatial dimensions of the grid can allow for more complex neuron interactions, as well as more complex input and ouptut behavior (for example, any data type that resembles a 2d surface)
  2. For the network to develop in real time, a reward/punishment feedback system will need to be implemented in order for the network to adapt.
  3. A memory cache will be needed to allow the network to identify which inputs should be associated with desired outputs, so that the network can strengthen the relevant connections within itself.

Dependencies: PyGame and NumPy
