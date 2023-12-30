

import matplotlib.pyplot as plt
import numpy as np



plt.axes(projection='polar')

for r in range(200):
	theta = r
	while theta > 2*np.pi:
		theta -= 2*np.pi
	plt.polar(theta, r, 'g.')

plt.show()

