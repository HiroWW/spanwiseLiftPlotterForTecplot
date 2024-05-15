import os
import sys
import logging

logging.basicConfig(stream=sys.stdout, level=logging.INFO)

import tecplot

# Run this script with "-c" to connect to Tecplot 360 on port 7600
# To enable connections in Tecplot 360, click on:
#   "Scripting" -> "PyTecplot Connections..." -> "Accept connections"
import sys
if '-c' in sys.argv:
    tecplot.session.connect()


examples_dir = tecplot.session.tecplot_examples_directory()
datafile = os.path.join(examples_dir, 'OneraM6wing', 'OneraM6_SU2_RANS.plt')
dataset = tecplot.data.load_tecplot(datafile)

frame = tecplot.active_frame()
frame.plot_type = tecplot.constant.PlotType.Cartesian3D
frame.plot().show_contour = True

# ensure consistent output between interactive (connected) and batch
frame.plot().contour(0).levels.reset_to_nice()

# export image of wing
tecplot.export.save_png('wing.png', 600, supersample=3)