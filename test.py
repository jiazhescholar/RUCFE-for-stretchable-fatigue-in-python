import math
import numpy as np
import matplotlib.pyplot as plt

from skimage.draw import (line, polygon)


fig,ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10, 6))


img = np.zeros((500, 500, 3), dtype=np.double)

# draw line
rr, cc = line(120, 123, 20, 400)
img[rr, cc, 0] = 255

# fill polygon
poly = np.array((
    (300, 300),
    (480, 320),
    (380, 430),
    (220, 590),
    (300, 300),
))
rr, cc = polygon(poly[:, 0], poly[:, 1], img.shape)
img[rr, cc, 1] = 1



ax1.imshow(img)
ax1.set_title('No anti-aliasing')
ax1.axis('on')


ax1.set_xlabel('Angles (degrees)')
ax1.set_ylabel('Distance (pixels)')

ax1.invert_yaxis() 

plt.show()