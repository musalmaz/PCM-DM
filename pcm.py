import numpy as np
import matplotlib.pyplot as plt

#m(t) = − 2 cos(200π t) + sin(50π t)
# signal properties
bandwith = 100
nyquist_frequency = 2 * bandwith
signal_duration = 2

L = 128
bits_num = 7 # log2(L)
T_s = signal_duration / nyquist_frequency
time = np.arange(start=1,stop=signal_duration * nyquist_frequency) / nyquist_frequency  # 199 sample
message = -2 * np.cos(200 * np.pi * time) + np.sin(50 * np.pi * time)
#print(time)
#print(len(time)) #199
plt.figure(figsize=(12,8))
plt.plot(time,message,'g')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Message signal')
plt.axis([0, 0.5, -3, 3])
plt.show()

max_amplitude = np.amax(message)
min_amplitude = np.amin(message)

#print(max_amplitude, min_amplitude) # 2.7071067811865683 -3.0
amplitude_diff = np.abs(max_amplitude) + np.abs(min_amplitude)   # 5.707106781186568
delta_l = amplitude_diff / L

levels = []
for i in range(L + 1):
    levels.append(min_amplitude + (i * delta_l))
level_list = []
for sampled_msg in message:
    for index, level in enumerate(levels):
        threshold = delta_l / 2
        if np.abs(sampled_msg - level) <= threshold:
            level_list.append(index)

#print(level_list)
result = []
for i in range(10):
    binary_result = np.binary_repr(int(level_list[i]), bits_num)
    result.append(binary_result)

print(*result, sep="-")



