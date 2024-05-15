import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *
import os
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

# Uncomment the following line to connect to a running instance of Tecplot 360:
tp.session.connect()

tp.macro.execute_command("""$!ReadDataSet  '\"C:\\Users\\fujiwara\\Downloads\\sigmoid_ver2.plt\" '
  ReadDataOption = New
  ResetStyle = No
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '\"X\" \"Y\" \"Z\" \"rho\" \"u\" \"v\" \"w\" \"p\" \"q_criterion\" \"domainid\"'""")
tp.active_frame().plot().rgb_coloring.red_variable_index=3
tp.active_frame().plot().rgb_coloring.green_variable_index=3
tp.active_frame().plot().rgb_coloring.blue_variable_index=3
tp.active_frame().plot().contour(0).variable_index=3
tp.active_frame().plot().contour(1).variable_index=7
tp.active_frame().plot().contour(2).variable_index=8
tp.active_frame().plot().contour(3).variable_index=9
tp.active_frame().plot().contour(4).variable_index=3
tp.active_frame().plot().contour(5).variable_index=3
tp.active_frame().plot().contour(6).variable_index=3
tp.active_frame().plot().contour(7).variable_index=3
tp.active_frame().plot(PlotType.Cartesian3D).show_slices=True
tp.active_frame().plot().show_contour=True
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().slice(0).orientation=SliceSurface.ZPlanes
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(-1.13687e-13,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    0,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    2144.64)
tp.active_frame().plot().view.psi=0
tp.active_frame().plot().view.theta=0
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(-1.13687e-13,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    0,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    2144.64)
tp.active_frame().plot().view.width=141.225
tp.active_frame().plot().view.position=(-1.13687e-13,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    0,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    2144.64)
tp.active_frame().plot().view.width=51.2246
tp.active_frame().plot().view.position=(-1.13687e-13,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    0,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    2144.64)
tp.active_frame().plot().view.width=26.5717
tp.active_frame().plot().view.position=(-1.13687e-13,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    0,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    2144.64)
tp.active_frame().plot().view.width=14.8914
tp.active_frame().plot().slice(0).origin.z=-0.5
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(-1.13687e-13,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    0,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    2144.64)
tp.active_frame().plot().view.width=25.4377
tp.active_frame().plot().view.position=(-1.13687e-13,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    0,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    2144.64)
tp.active_frame().plot().view.width=19.906
tp.active_frame().plot().view.position=(2.22059,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.290792,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    2144.64)
tp.active_frame().plot().view.width=19.906
tp.active_frame().plot().view.position=(2.22059,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -0.290792,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    2144.64)
tp.active_frame().plot().view.width=10.9631
tp.active_frame().plot().view.position=(2.17691,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    0.131424,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    2144.64)
tp.active_frame().plot().view.width=10.9631
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 9.10358565737
  Y = 4.05876494024
  ConsiderStyle = Yes''')
tp.active_frame().plot().contour(0).variable_index=7
tp.macro.execute_command('$!RedrawAll')
tp.export.save_png('./test2.png',
    width=753,
    region=ExportRegion.AllFrames,
    supersample=1,
    convert_to_256_colors=False)
# End Macro.

