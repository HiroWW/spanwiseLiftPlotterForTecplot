import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *
import numpy as np 
import matplotlib.pyplot as plt
# Uncomment the following line to connect to a running instance of Tecplot 360:
# tp.session.connect()


# 指定された範囲と分割数
start = 0.15  # 範囲の開始点
end = 1.0    # 範囲の終了点
n = 30       # 分割数

# 各区間の中心点を計算
r_R = np.linspace(start, end, n+1)  # 分割点を計算
r_R_centers = (r_R[:-1] + r_R[1:]) / 2  # 中心点を計算
span_array = r_R_centers * (1/0.202)

cl_array = []
# ループを回す外枠
for span in span_array:
  print ("CURRENT SPAN : " , span * 0.202)
  tp.macro.execute_command("""$!ReadDataSet  '\"C:\\Users\\{user}\\Documents\\m1\\07_spanwise-cl-distribution\\surfave.plt\" '
    ReadDataOption = New
    ResetStyle = Yes
    VarLoadMode = ByName
    AssignStrandIDs = Yes
    VarNameList = '\"X\" \"Y\" \"Z\" \"cp_ave\" \"cp_rms\" \"cfx_ave\" \"cfy_ave\" \"cfz_ave\"'""")
  tp.active_frame().plot_type=PlotType.Cartesian3D
  tp.active_frame().plot().rgb_coloring.red_variable_index=3
  tp.active_frame().plot().rgb_coloring.green_variable_index=3
  tp.active_frame().plot().rgb_coloring.blue_variable_index=3
  tp.active_frame().plot().slice(0).edge.show=True
  tp.active_frame().plot().slice(0).slice_source=SliceSource.SurfaceZones
  tp.active_frame().plot().contour(0).variable_index=3
  tp.active_frame().plot().contour(1).variable_index=4
  tp.active_frame().plot().contour(2).variable_index=5
  tp.active_frame().plot().contour(3).variable_index=6
  tp.active_frame().plot().contour(4).variable_index=7
  tp.active_frame().plot().contour(5).variable_index=3
  tp.active_frame().plot().contour(6).variable_index=3
  tp.active_frame().plot().contour(7).variable_index=3
  tp.active_frame().plot(PlotType.Cartesian3D).show_slices=True
  tp.active_frame().plot().slice(0).origin.x=span
  tp.active_frame().plot().slices(0).extract(transient_mode=TransientOperationMode.AllSolutionTimes)
  tp.data.save_tecplot_ascii(f'C:\\Users\\{user}\\Documents\\m1\\07_spanwise-cl-distribution\\slice-x-is-{span}.dat',
      zones=[1],
      variables=[1,3],
      include_text=False,
      precision=9,
      include_geom=False,
      use_point_format=True)
  # End Macro.
  print("END TECPLOT MACRO")
  slice_data = np.loadtxt(f'slice-x-is-{span}.dat', skiprows=8)
  x = slice_data[:,0]
  x = x / (np.max(x)-np.min(x)) 
  x = x - np.min(x)
  y = slice_data[:,1] * (1.0/(0.03514*span))**2

  plt.clf()
  plt.plot(x, y)
  # plt.show()

  area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
  print(f"閉曲線の面積: {area}")
  cl_array.append(area)
  print("END AREA CALCULATION")

# plot cl - r/R
plt.clf()
plt.plot(r_R_centers, cl_array)
plt.xlabel('r/R')
plt.ylabel('Cl')
plt.ylim(0, 1.5)
plt.show()

# save cl - r/R to txt tab separated
np.savetxt("cl-r_R.txt", np.array([r_R_centers, cl_array]).T, delimiter="\t")