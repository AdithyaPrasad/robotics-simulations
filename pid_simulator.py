#test
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

Kp, Ki, Kd = 1.2, 0.1, 0.05
target = 10
position = 0
velocity = 0
integral = 0
prev_error = 0
dt = 0.1
time_steps = 100

positions = []
times = []

fig, ax = plt.subplots()
line, = ax.plot([], [], lw=2)
target_line = ax.axhline(y=target, color='r', linestyle='--', label="Target")

ax.set_xlim(0, time_steps*dt)
ax.set_ylim(0, target + 5)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Position')
ax.set_title('PID Position Control Animation')
ax.grid(True)

def init():
    line.set_data([], [])
    return line,

def update(frame):
    global position, velocity, integral, prev_error
    error = target - position
    integral += error * dt
    derivative = (error - prev_error) / dt

    output = Kp * error + Ki * integral + Kd * derivative
    velocity = output
    position += velocity * dt

    prev_error = error

    positions.append(position)
    times.append(frame * dt)

    line.set_data(times, positions)
    return line,

ani = FuncAnimation(fig, update, frames=range(time_steps),
                    init_func=init, blit=True, interval=100)

plt.legend()
plt.show()
