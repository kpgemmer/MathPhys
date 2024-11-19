import matplotlib.pyplot as plt
from IPython.display import HTML
from matplotlib.animation import FuncAnimation

# plt.rcParams["animation.html"] = "jshtml"
# plt.rcParams['figure.dpi'] = 150
# plt.ioff()

def flugbahn_animieren(x,y):
    fig, ax = plt.subplots(figsize=(6, 6))
    ax.set_xlim(1.2 * min(x), 1.2 * max(x))
    ax.set_ylim(1.2 * min(y), 1.2 * max(y))
    ax.set_aspect('equal')
    ax.set_xlabel("x (m)")
    ax.set_ylabel("y (m)")

    # obj, = ax.plot([], [], 'bo', markersize=5)
    # obj, = ax.plot(x, y, 'bo', markersize=5)
    # trajectory, = ax.plot([], [], 'b-', lw=1, alpha=0.6, label="Trajektorie")
    trajectory, = ax.plot(x, y, 'b-', lw=1, alpha=0.6, label="Trajektorie")
    ax.legend()

    def update(frame):
        obj.set_data(x[frame], y[frame])
        trajectory.set_data(x[:frame], y[:frame])
        return obj, trajectory,


    # ani = FuncAnimation(fig, update, frames=len(x), interval=0.5, blit=True)

    # HTML(ani.to_html5_video())

    plt.show()
