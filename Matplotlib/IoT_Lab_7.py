import matplotlib.pyplot as plt
import numpy as np

frequency = np.linspace(90, 120, 100)
amplitude = -30 * np.sin(0.3 * frequency) - 20 * np.random.rand(100)

plt.figure(figsize=(10, 6))
plt.plot(frequency, amplitude, label="Amplituda sygnału", color="yellow")
plt.xlabel("Częstotliwość (MHz)")
plt.ylabel("Amplituda (dBm)")
plt.title("Wykres amplitudy sygnału w zależności od częstotliwości")
plt.grid()

highlight_points = [(93, -16), (105, -16), (115, -40)]

for freq, amp in highlight_points:
    plt.annotate(f"({freq} MHz, {amp} dBm)",
                 xy=(freq, amp),
                 xytext=(freq + 2, amp + 10),
                 arrowprops=dict(facecolor='red', arrowstyle="->"))

plt.legend()
plt.show()
