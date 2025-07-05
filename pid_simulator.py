import matplotlib.pyplot as plt
import numpy as np

# PID parameters
Kp = 1.2
Ki = 0.1
Kd = 0.05

target = 10  # desired position
position = 0
velocity = 0
integral = 0
prev_error = 0

dt = 0.1
time_steps = 100

positions = []
times = []

for t in range(time_steps):
    error = target - position
    integral += error * dt
    derivative = (error - prev_error) / dt

    output = Kp * error + Ki * integral + Kd * derivative
    velocity = output
    position += velocity * dt

    prev_error = error

    positions.append(position)
    times.append(t * dt)

# Plot the result
plt.plot(times, positions)
plt.axhline(y=target, color='r', linestyle='--', label="Target")
plt.xlabel("Time (s)")
plt.ylabel("Position")
plt.title("PID Position Control Simulation")
plt.legend()
plt.grid(True)
plt.show()

