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
# Filter out negative and zero values for all layers

for layer in layers:
    df = df[df[layer] > 0]

# Specify the layers you want to move and the amounts
move_layers = {'1m':463, '1.47m':462.53, '2.15m':461.85, '3.16m':460.84, '4.64m':459.36,
          '6.81m':457.19, '10m':454, '14.7m':449.3, '31.6m':432.4, '46.4m':417.6, '68.1m':395.9, '100m':364, '147m':317, '215m':249, '316m':148,}

for index, layer in enumerate(layers):
    # Perform the interpolation
    Z = griddata((df['X'], df['Y']), df[layer], (grid_x, grid_y), method='cubic')
    
    # Remove negative and zero values from the interpolated data
    Z[Z <= 15] = np.nan  # Replace with NaN

    # Check if this is one of the layers to move and calculate its new offset
    if layer in move_layers:
        offset_amount = -index * 200 + move_layers[layer]
    else:
        offset_amount = -index * 200

    # Create a flat contour map at a specific height
    contour = ax.contourf(grid_x, grid_y, Z, zdir='z', offset=offset_amount, cmap='jet')

    
    # Check if this is one of the layers to move and calculate its new offset
    if layer in move_layers:
        offset_amount = -index * 200 + move_layers[layer]
    else:
        offset_amount = -index * 200
    # Create a flat contour map at a specific height
    
    contour = ax.contourf(grid_x, grid_y, Z, zdir='z', offset=offset_amount, cmap='jet')
    
ax.set_xlim(min(df['X']), max(df['X']))
ax.set_ylim(min(df['Y']), max(df['Y']))
ax.set_zlim(-len(layers) * 200, 0)

# Set labels
ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Depth')

ax.set_zticklabels([])
ax.grid(False)

# Add a horizontal color bar at the bottom
cbar = fig.colorbar(contour, ax=ax,  orientation='horizontal')
cbar.set_label('Resistivity (Ohm-m)', fontsize=12)
cbar.ax.xaxis.set_ticks_position('bottom')
cbar.ax.xaxis.set_label_position('bottom')

# Show plot
plt.show()

