# 3. Chapter - Visualize Data

- `matplotlib` -> for charts

### Bar Charts

- `pyplot.bar` -> (list_of_positions, list_of_height_of_bar, width)
- `from typing import Counter` -> this allows to get occurencies of each item
- `plt.axis` -> defining it for `y-axis` most of the time is a good way to mislead people

### Line Charts

Those are good for showing trends

- `plt.plot(list_of_positions_to_take, height_during_positions, color_and_line_type, label="label_name")`:
  `color_and_line_type` -> can be `g,r,b,c,y` (and so on) together with line type `- -. : --`

### Scatterplots

Right choice for visualizing the relationship between two paired sets of data
