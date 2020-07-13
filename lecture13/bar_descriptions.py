import pygal
from pygal.style import LightColorizedStyle as LCS
from pygal.style import LightenStyle as LS

my_style = LS('#336633', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['awesome-python', 'system-design-primer', 'public-apis']

plot_dicts = [
    {'value': 66036, 'label': 'Description of awesome-python'},
    {'value': 61680, 'label': 'Description of system-design-primer'},
    {'value': 55876, 'label': 'Description of public-apis'},
    ]

chart.add('', plot_dicts)
chart.render_to_file('bar_description.svg')