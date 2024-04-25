import tecplot as tp
from tecplot.constant import PlotType, ValueLocation

# Tecplot 360セッションの開始とデータのロード
tp.session.connect()
dataset = tp.data.load_tecplot('test.plt')

# 必要な変数の選択
x = dataset.variable('X')
y = dataset.variable('Y')
cp = dataset.variable('CP')  # 圧力変数

# # 新しい変数 'Cp' を追加
# cp = dataset.add_variable('Cp')

# # Cpの計算式を設定
# cp_formula = '({} - 1 / 1.4) / (0.5 * 1 * 0.2 * 0.2)'.format(p.name)
# cp.equation = cp_formula  # 正しいプロパティへの計算式の設定

# スパン方向の分割設定
spanwise_slices = 10  # スパン方向のスライス数

# スパン方向の全範囲を取得
y_min, y_max = y.values().min(), y.values().max()

# スライス間の距離を計算
slice_width = (y_max - y_min) / spanwise_slices

# 各スライスでのCLの計算
cl_values = []
spanwise_positions = []

for i in range(spanwise_slices):
    y_start = y_min + i * slice_width
    y_end = y_start + slice_width
    spanwise_positions.append((y_start + y_end) / 2)

    # 範囲に基づいてスライスを作成
    with tp.session.suspend():
        slice = dataset.slice((1, y_start, y_end), plot_type=PlotType.XYLine)
    
    # Cpを積分してClを計算
    slice.activate()
    cl = tp.data.query_integral(cp, direction='X', zone=slice)
    cl_values.append(cl)

# 揚力分布のプロット
tp.new_layout()
frame = tp.active_frame()
plot = frame.plot(PlotType.XYLine)
line_map = plot.add_xy_line(y=spanwise_positions, x=cl_values)

# 軸の設定
plot.axes.y_axis.variable = cp
plot.axes.x_axis.variable = dataset.variable('Spanwise Position')

# プロットの保存
plot.save('spanwise_lift_distribution.png')

tp.session.disconnect()
