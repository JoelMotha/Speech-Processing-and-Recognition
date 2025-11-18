import numpy as np
import matplotlib.pyplot as plt
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean

# Parameters
fs = 1000  # sampling frequency
t = np.linspace(0, 1, fs)
f1 = 5  # frequency 1
f2 = 5  # frequency 2 (can change slightly)

# Original sine waves
y1 = np.sin(2 * np.pi * f1 * t)
y2 = np.sin(2 * np.pi * f2 * t * 1.2)  # stretched in time

# Convert to 2D vectors (required by fastdtw)
y1_list = [[val] for val in y1]
y2_list = [[val] for val in y2]

# DTW
distance, path = fastdtw(y1_list, y2_list, dist=euclidean)
print(f"DTW distance: {distance:.2f}")
print(f"Alignment path length: {len(path)}")

# Plot signals
plt.figure(figsize=(10,4))
plt.plot(t, y1, label='y1 (original)')
plt.plot(np.linspace(0,1,len(y2)), y2, label='y2 (stretched)')
plt.title("Sine Waves")
plt.legend()
plt.show()

# Plot DTW path
plt.figure(figsize=(8,6))
plt.plot([p[0] for p in path], [p[1] for p in path], marker='.', color='r')
plt.title("DTW Alignment Path")
plt.xlabel("y1 index")
plt.ylabel("y2 index")
plt.grid(True)
plt.show()
