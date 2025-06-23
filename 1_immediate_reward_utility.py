import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# Parameters
V0 = 1
k = 1
lambda_fixed = 0.5
R_values = np.linspace(0, 2, 40)  # Immediate reward magnitude from 0 to 2
t = np.linspace(0, 20, 500)

# Approximate delta as a narrow Gaussian centered at 0
def delta_approx(t, width=0.05):
    return np.exp(- (t / width)**2) / (width * np.sqrt(np.pi))

fig, ax = plt.subplots(figsize=(10,6))
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 5)
ax.set_ylim(0, 3)
ax.set_xlabel("Time (t)")
ax.set_ylabel("Instantaneous Utility")
ax.set_title("Effect of Immediate Reward Injection on Utility")

def init():
    line.set_data([], [])
    return line,

def animate(i):
    R = R_values[i]
    V_t = V0 * np.exp(-lambda_fixed * t) + R * delta_approx(t)
    W_t = 1 / (1 + k * t)
    y = V_t * W_t
    line.set_data(t, y)
    ax.set_title(f"Immediate Reward R = {R:.2f}")
    return line,

ani = animation.FuncAnimation(fig, animate, frames=len(R_values),
                              init_func=init, blit=True, interval=100)

ani.save("immediate_reward_utility.gif", writer=PillowWriter(fps=10))
print("Saved animation as immediate_reward_utility.gif")