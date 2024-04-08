# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 22:45:02 2024

@author: Arad
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from scipy.interpolate import griddata

# Load the data from the Excel file
df = pd.read_excel('processed-data.xlsx')

# Define the grid where the interpolation will be done
grid_x, grid_y = np.mgrid[min(df['X']):max(df['X']):100j, min(df['Y']):max(df['Y']):100j]

# Create a 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Assuming each layer is a column in the DataFrame
layers = ['1m', '1.47m', '2.15m', '3.16m', '4.64m',
          '6.81m', '10m', '14.7m', '31.6m', '46.4m', '68.1m', '100m', '147m', '215m', '316m', '464m']

# Variable to store the last plot_surface object for the color bar
surf = None

for layer in layers:
    # Perform the interpolation
    GE = griddata((df['X'], df['Y']), df[layer], (grid_x, grid_y), method='cubic')
    
    # Make the Z values negative
    GE = -GE *2
    
    # Plot the surface for each layer and store the object in depth
    Depth = ax.plot_surface(grid_x, grid_y, GE, cmap='jet', label=layer)
    
 # Plot the surface
Ngrid_x, Ngrid_y = np.mgrid[min(df['X']):max(df['X']):100j, min(df['Y']):max(df['Y']):100j]
NZ = griddata((df['X'], df['Y']), df['z'], (Ngrid_x, Ngrid_y), method='cubic')
# Shift the 'Surf' surface up by 600 units
NZ_shifted = 100 * NZ - 20000
Surf = ax.plot_surface(Ngrid_x, Ngrid_y, NZ_shifted, color='green')
# Adding color bar to show resistivity scale
fig.colorbar(Depth, ax=ax, shrink=0.5, aspect=5, label='Resistivity (Ohm-m)')

# Set labels
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Z Coordinate')

# Show plot
plt.show()
   