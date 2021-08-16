import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()
ax.axis([-2,2,-2,2])

arrowprops=dict(arrowstyle='<-', color='blue', linewidth=10, mutation_scale=150)
an = ax.annotate('Blah', xy=(1, 1), xytext=(-1.5, -1.5), xycoords='data', 
                 textcoords='data', arrowprops=arrowprops)

colors=["crimson", "limegreen", "gold", "indigo"]
def update(i):
    c = colors[i%len(colors)]
    an.arrow_patch.set_color(c)

ani = animation.FuncAnimation(fig, update, 10, interval=1000, repeat=True)
plt.show()