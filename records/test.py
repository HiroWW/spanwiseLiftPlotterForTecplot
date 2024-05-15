import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *

# Uncomment the following line to connect to a running instance of Tecplot 360:
# tp.session.connect()

tp.active_frame().plot().axes.x_axis(0).min=-0.776589
tp.active_frame().plot().axes.x_axis(0).max=1.50909
tp.active_frame().plot().axes.y_axis(0).min=-1.21249
tp.active_frame().plot().axes.y_axis(0).max=0.897334
tp.active_frame().plot().axes.x_axis(0).min=-1.11094
tp.active_frame().plot().axes.x_axis(0).max=1.84344
tp.active_frame().plot().axes.y_axis(0).min=-1.52112
tp.active_frame().plot().axes.y_axis(0).max=1.20596
tp.export.save_png('//wsl$/Ubuntu/home/hiroaki/spanwiseLiftPlotterForTecplot/records/test.png',
    width=753,
    region=ExportRegion.AllFrames,
    supersample=3,
    convert_to_256_colors=False)
# End Macro.

