# matplotlib_settings.py

# use: 
# 
# import plot_settings
# from plot_settings import colors 

# ax.plot(
#     .,
#     .,
#     c=colors["blue"]
# )

import matplotlib.pyplot as plt

plt.rcParams.update({
    'figure.figsize': (10, 6),
    'axes.titlesize': 16,
    'axes.labelsize': 14,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'legend.fontsize': 10
})

colors = {
    "blue": "cornflowerblue",
    "orange": "darkorange",
    "red": "firebrick"
}