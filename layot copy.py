import tkinter as tk
from tkinter import Frame, Label
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import numpy as np
import time

def generate_sensor_data():
    return np.random.randint(40, 60)  # Random values between 40 and 60

def init_graph(ax):
    ax.clear()
    ax.set_ylim(0, 100)
    line, = ax.plot([], [], 'r-', lw=2)  # Initialize the line object
    return line

def update_graph(fig, ax, line, x, y):
    line.set_xdata(x)
    line.set_ydata(y)
    ax.set_xlim(min(x), max(x) + 1)  # Adjust x-axis limits dynamically
    ax.relim()
    ax.autoscale_view()
    fig.canvas.draw()

root = tk.Tk()
root.title("FINAL LAYOUT")

# Frames
left_frame_Upper = Frame(root, width=400, height=300, bg="grey")
left_frame_Upper.grid(row=0, column=0, padx=5, pady=5, sticky="nsew")
left_frame_Lower = Frame(root, width=400, height=300, bg="red")
left_frame_Lower.grid(row=1, column=0, padx=5, sticky="nsew")

center_frame_Upper = Frame(root, width=650, height=300, bg="blue")
center_frame_Upper.grid(row=0, column=1, padx=20, pady=5, columnspan=2, sticky="nsew")
center_frame_Lower = Frame(root, width=650, height=300, bg="light blue")
center_frame_Lower.grid(row=1, column=1, padx=20, pady=5, columnspan=2, sticky="nsew")

right_frame = Frame(root, width=400, height=600, bg="black")
right_frame.grid(row=0, column=3, rowspan=2, padx=20, pady=5, sticky="nsew")
right_frame.grid_propagate(False)

# Label for displaying sensor data
sensor_data_label = Label(left_frame_Upper, text="Sensor Data: --", bg="grey", font=("Helvetica", 16))
sensor_data_label.pack(pady=20)

# Matplotlib figure and canvas
fig = Figure(figsize=(4, 5))
ax = fig.add_subplot(111)
line = init_graph(ax)
canvas = FigureCanvasTkAgg(fig, master=right_frame)
canvas_widget = canvas.get_tk_widget()
canvas_widget.pack(fill=tk.BOTH, expand=True)

sensor_data = []
times = []

def update():
    data = generate_sensor_data()
    times.append(time.time() if times else 0)
    sensor_data.append(data)

    # Update the sensor data label with the latest value
    sensor_data_label.config(text=f"Sensor Data: {data}")

    if len(times) > 100:
        times.pop(0)
        sensor_data.pop(0)

    update_graph(fig, ax, line, times, sensor_data)
    root.after(100, update)  # Schedule next update

root.after(1000, update)  # Start updating after 1000 ms
root.mainloop()
