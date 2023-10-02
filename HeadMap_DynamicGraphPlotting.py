import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import matplotlib.animation as animation
import matplotlib.animation as anim
from collections import deque
import random

# MAX NO. OF POINTS TO STORE
max_points=20

que2 = deque(maxlen = max_points)
que3 = deque(maxlen = max_points)
t = deque(maxlen = max_points)
dt = 0.1  # time interval

que2.append(0)
que3.append(0.)
t.append(0.)

data=[[0., 0., 0., 0., 0., 0., 0., 0.],
      [0., 0., 0., 0., 0., 0., 0., 0.],
      [0., 0., 0., 0., 0., 0., 0., 0.],
      [0., 0., 0., 0., 0., 0., 0., 0.],
      [0., 0., 0., 0., 0., 0., 0., 0.],
      [0., 0., 0., 0., 0., 0., 0., 0.],
      [0., 0., 0., 0., 0., 0., 0., 0.],
      [0., 0., 0., 0., 0., 0., 0., 0.]]

image = np.random.rand(10,10,10)

# setup figure
fig = plt.figure(figsize=(12,4))

ax1=fig.add_subplot(1,3,1)
ax2=fig.add_subplot(1,3,2)
ax3=fig.add_subplot(1,3,3)

def data_arduino():
    # GENERATING THE POINTS - FOR DEMO
    hm_array = np.random.uniform(20, 40, size=(8,8))
    hm_array = np.round(hm_array, 2)
    global data
    data = hm_array

    perc = random.randrange(0, 4)
    global que2
    que2.append(perc)

    perc = random.randrange(80, 100)
    global que3
    que3.append(perc)

    global t
    t.append(np.round(t[-1]+dt,2))


#set up list of images for animation
ims=[]

def animation_frame(x):
    
    data_arduino()
    
    # Mapa de calor
    im = ax1.imshow(data, cmap = "jet", vmin = 20, vmax = 30, animated=True)

    # Agregar la leyenda
    #cbar = ax1.figure.colorbar(im, ax = ax1)
    #cbar.ax.set_ylabel("Heat Map", rotation = -90, va = "bottom")

    ax2.clear()
    ax3.clear()

    im2, = ax2.plot(t, que2, color='green')
    im3, = ax3.plot(t, que3, color='crimson')

    ax1.set_title("Mapa de calor")

    ax2.set_title("Pureza de aire")
    ax2.set_xlabel("Tiempo")
    ax2.set_ylabel("Grados")

    ax3.set_title("Gases inflamables")
    ax3.set_xlabel("Tiempo")
    ax3.set_ylabel("Grados")

    #return data
    ims.append([im, im2, im3])


animation = FuncAnimation(fig, func=animation_frame, frames=10, interval=1000)
plt.show()
