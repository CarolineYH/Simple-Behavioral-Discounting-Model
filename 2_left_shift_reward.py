import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# Parameters
V0 = 1
k = 1
lambda_fixed = 0.5
tau_values = np.linspace(0, 5, 40)  # Shift amount from 0 to 5
t = np.linspace(0, 20, 500)

fig, ax = plt.subplots(figsize=(10,6))
line, = ax.plot([], [], lw=2)
ax.set_xlim(0, 20)
ax.set_ylim(0, 1)
ax.set_xlabel("Time (t)")
ax.set_ylabel("Instantaneous Utility")
ax.set_title("Effect of Left Shift on Utility")

def shifted_V(t, tau):
    # For t < tau, clamp to V(0); else exponential decay from shifted time
    return np.where(t < tau, V0, V0 * np.exp(-lambda_fixed * (t - tau)))

def init():
    line.set_data([], [])
    return line,

def animate(i):
    tau = tau_values[i]
    V_t = shifted_V(t, tau)
    W_t = 1 / (1 + k * t)
    y = V_t * W_t
    line.set_data(t, y)
    ax.set_title(f"Shift τ = {tau:.2f}")
    return line,

ani = animation.FuncAnimation(fig, animate, frames=len(tau_values),
                              init_func=init, blit=True, interval=100)

ani.save("left_shift_utility.gif", writer=PillowWriter(fps=10))
print("Saved animation as left_shift_utility.gif")