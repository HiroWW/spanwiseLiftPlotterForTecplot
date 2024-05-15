import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *

# Uncomment the following line to connect to a running instance of Tecplot 360:
# tp.session.connect()

tp.macro.execute_command("""$!ReadDataSet  '\"C:\\Users\\fujiwara\\Downloads\\sigmoid_ver2.plt\" '
  ReadDataOption = New
  ResetStyle = Yes
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
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(2144.64,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -2.45008e-13,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    1.31321e-13)
tp.active_frame().plot().view.psi=90
tp.active_frame().plot().view.theta=-90
tp.macro.execute_command('$!RedrawAll')
tp.active_frame().plot().view.position=(2144.64,
    tp.active_frame().plot().view.position[1],
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    -2.45008e-13,
    tp.active_frame().plot().view.position[2])
tp.active_frame().plot().view.position=(tp.active_frame().plot().view.position[0],
    tp.active_frame().plot().view.position[1],
    1.31321e-13)
tp.active_frame().plot().view.width=93.8902
tp.macro.execute_command('''$!Pick AddAtPosition
  X = 8.8764940239
  Y = 3.19820717131
  ConsiderStyle = Yes''')
tp.active_frame().plot().contour(0).variable_index=7
tp.macro.execute_command('$!RedrawAll')
# End Macro.

