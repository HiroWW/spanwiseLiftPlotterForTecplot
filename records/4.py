import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *

# Uncomment the following line to connect to a running instance of Tecplot 360:
# tp.session.connect()

tp.macro.execute_command("""$!ReadDataSet  '\"C:\\Users\\fujiwara\\Downloads\\sigmoid_ver2.plt\" '
  ReadDataOption = New
  ResetStyle = No
  VarLoadMode = ByName
  AssignStrandIDs = Yes
  VarNameList = '\"X\" \"Y\" \"Z\" \"rho\" \"u\" \"v\" \"w\" \"p\" \"q_criterion\" \"domainid\"'""")
# End Macro.

