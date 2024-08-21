import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *
import numpy as np 
import matplotlib.pyplot as plt
import os

# User-defined parameters
start = 0.15  # Range start
end = 1.0     # Range end
n = 15       # Number of divisions
user_path = os.path.dirname(os.path.abspath(__file__)) # Update this path by yourself

# Compute midpoints for each section
r_R = np.linspace(start, end, n+1)
r_R_centers = (r_R[:-1] + r_R[1:]) / 2
span_array = r_R_centers

cl_array = []

for span in span_array:
    print("CURRENT SPAN: ", span)
    
    tp.macro.execute_command(f"""
        $!ReadDataSet  '{user_path}\\surfave.plt'
        ReadDataOption = New
        ResetStyle = Yes
        VarLoadMode = ByName
        AssignStrandIDs = Yes
        VarNameList = '\"X\" \"Y\" \"Z\" \"rho\" \"cp\" \"cf\" \"cfx\" \"cfy\" \"cfz\" \"u\" \"v\" \"w\"'
    """)
    
    tp.active_frame().plot_type = PlotType.Cartesian3D
    tp.active_frame().plot().rgb_coloring.red_variable_index = 3
    tp.active_frame().plot().rgb_coloring.green_variable_index = 3
    tp.active_frame().plot().rgb_coloring.blue_variable_index = 3
    tp.active_frame().plot().slice(0).edge.show = True
    tp.active_frame().plot().slice(0).slice_source = SliceSource.SurfaceZones
    tp.active_frame().plot().contour(0).variable_index = 3
    tp.active_frame().plot().contour(1).variable_index = 4
    tp.active_frame().plot().contour(2).variable_index = 5
    tp.active_frame().plot().contour(3).variable_index = 6
    tp.active_frame().plot().contour(4).variable_index = 7
    tp.active_frame().plot().contour(5).variable_index = 3
    tp.active_frame().plot().contour(6).variable_index = 3
    tp.active_frame().plot().contour(7).variable_index = 3
    tp.active_frame().plot(PlotType.Cartesian3D).show_slices = True
    tp.active_frame().plot().slice(0).orientation=SliceSurface.YPlanes
    tp.active_frame().plot().slice(0).origin.y = span
    tp.active_frame().plot().slices(0).extract(transient_mode=TransientOperationMode.AllSolutionTimes)
    
    output_file = os.path.join(user_path, f'slice-x-is-{span}.dat')
    tp.data.save_tecplot_ascii(output_file,
                               zones=[1],
                               variables=[0, 4],
                               include_text=False,
                               precision=9,
                               include_geom=False,
                               use_point_format=True)
    
    print("END TECPLOT MACRO")
    
    slice_data = np.loadtxt(output_file, skiprows=8)
    x = slice_data[:, 0]
    x = x / (np.max(x) - np.min(x)) 
    x = x - np.min(x)
    y = slice_data[:, 1] 
    
    plt.clf()
    plt.plot(x, y)
    
    area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    print(f"Closed curve area: {area}")
    cl_array.append(area)
    print("END AREA CALCULATION")

# Plot cl - r/R
plt.clf()
plt.plot(r_R_centers, cl_array)
plt.xlabel('r/R')
plt.ylabel('Cl')
# plt.ylim(0, 1.5)
plt.savefig("cl-r_R.png")
plt.show()

# Save cl - r/R to text file
np.savetxt("cl-r_R.txt", np.array([r_R_centers, cl_array]).T, delimiter="\t")
