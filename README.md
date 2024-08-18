# Geoelectricspy
[![CodeFactor](https://www.codefactor.io/repository/github/aradfarahani/geoelectricspy/badge)](https://www.codefactor.io/repository/github/aradfarahani/geoelectricspy)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.10966815.svg)](https://doi.org/10.5281/zenodo.10966815)

![ezgif-1-3c5033177d](https://github.com/aradfarahani/Geoelectricspy/assets/90475349/9932c675-414d-449e-84cf-e7ba028f8d93)



## Overview
This project presents an interactive 3D visualization of subsurface resistivity using geoelectric data. It utilizes Python and its scientific libraries to process and visualize the data across multiple depths, ranging from 1 meter to 464 meters.

## Features
- Data manipulation with `pandas`
- Numerical operations with `numpy`
- 3D plotting with `matplotlib`
- Cubic interpolation with `scipy`
  
## Usage
Load the data from an Excel file and run the script to generate the 3D visualization. The interactive plot allows for rotation and zooming to explore different layers of resistivity.
## Data
The data is stored in ‘processed-data.xlsx’, which contains the X, Y coordinates and resistivity values for various depth
## Visualization
The 3D plot is generated using matplotlib and mpl_toolkits.mplot3d. Each layer’s resistivity is interpolated and visualized with a color map to represent different resistivity levels.
## Contributing
Contributions to improve the visualization or extend the capabilities of this project are welcome. Please fork the repository and submit a pull request.
## License
This project is open-sourced under the MIT License.
## Contact
For any queries or discussions regarding the project, feel free to reach out.

## Installation
To run this project, you will need to install the following Python libraries:
```bash
pip install pandas numpy matplotlib scipy
