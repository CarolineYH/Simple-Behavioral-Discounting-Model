
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# Parameters
V0 = 1
k = 1
lambda_fixed = 0.5
compression_factors = np.linspace(1.0, 0.2, 40)  # 时间压缩因子 α 从 1.0 到 0.2
t = np.linspace(0, 20, 500)  # 时间范围

fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 20)
ax.set_ylim(0, 1)
ax.set_title("Effect of Time Compression on Utility Contribution")
ax.set_xlabel("Time (t)")
ax.set_ylabel("Instantaneous Utility")

# Initialization function
def init():
    line.set_data([], [])
    return line,

# Animation for each frame
def animate(i):
    alpha = compression_factors[i]
    V_t = V0 * np.exp(-lambda_fixed * (alpha * t))   # V(t) after time compression
    W_t = 1 / (1 + k * t)                             # Discount function W(t)
    y = V_t * W_t                                     # Utility contribution
    line.set_data(t, y)
    ax.set_title(f"Time Compression: α = {alpha:.2f}")
    return line,

# Create animation object
ani = animation.FuncAnimation(
    fig, animate, frames=len(compression_factors),
    init_func=init, blit=True, interval=100
)

# Save as GIF
ani.save("time_compression_utility.gif", writer=PillowWriter(fps=10))
print("Animation saved as time_compression_utility.gif")