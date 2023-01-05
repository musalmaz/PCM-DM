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
# plot message signal
"""plt.figure(figsize=(12,8))
plt.plot(time,message,'g')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Message signal')
plt.axis([0, 0.5, -3, 3])
plt.show()
"""
max_amplitude = np.amax(message)# 2.7071067811865683
min_amplitude = np.amin(message)# -3.0

amplitude_diff = max_amplitude - min_amplitude  # 5.707106781186568
delta_l = amplitude_diff / L   # difference between quantization levels

levels = []
for i in range(L):
    levels.append(min_amplitude + (i * delta_l))
level_list = []
for sampled_msg in message:
    sampled_msg-= min_amplitude
    sampled = sampled_msg // delta_l
    sampled = -sampled + 127
    level_list.append(sampled)

result = []
for i in range(10):
    binary_result = np.binary_repr(int(level_list[i]), bits_num)
    result.append(binary_result)
print("Resulting PCM output: ")
print(*result, sep="-")  # 0000000-1010011-0000000-1101001-0011111-1111111-0011111-1101001-0000000-1010011

####################################  Second Part Delta Modulation          ####################

# m(t) = − 2 cos(200π t) + sin(50π t)
bandwith = 100
nyquist_rate = 2 * bandwith
sampled_frequency = 4 * nyquist_rate
signal_duration  = 2
time = np.arange(start=0,stop=signal_duration * sampled_frequency) / sampled_frequency 
message = -2 * np.cos(200 * np.pi * time) + np.sin(50 * np.pi * time)
message_derivative = 2 * 200 * np.pi * np.sin(200 * np.pi * time) + 50 * np.pi * np.cos(50 * np.pi * time)
max_message_derivative = np.amax(message_derivative)

step_list = np.zeros_like(message)
step_list[0] = 0
epsilons = np.zeros_like(message)
delta_epsilon = 0.8
step = delta_epsilon

for index in range(len(message)):
    if message[index] > delta_epsilon:
        epsilons[index] = step
        delta_epsilon += step
    else:
        epsilons[index] = - step
        delta_epsilon -= step
    if index != len(message)-  1:
        step_list[index+ 1] = delta_epsilon
modulated_output = np.zeros_like(epsilons)
for i in range(len(epsilons)):  #convert pozitive or negative epsilon values to bits
    if epsilons[i] < 0:
        modulated_output[i] = 0
    else:
        modulated_output[i] = 1

result = []
for i in range(1,21):   # since we take message signal as a base, discard first index sice first sample is taken at Ts
    result.append(int(modulated_output[i]))
print("Output of Delta modulation: ")
print(*result, sep='-')  # print the result    ### 0-1-1-1-1-0-0-0-0-1-1-1-1-0-0-0-0-1-1-1

# Plot message signal and levels  also epsilons
"""plt.figure(figsize=(12,8))
plt.subplot(2, 1, 1)
plt.plot(time,message,'g')
plt.step(time, step_list, 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Message signal')
plt.axis([0, 0.005, -3, 4])

plt.subplot(2,1,2)
plt.scatter(time,epsilons)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Epsilon')
plt.axis([0, 0.005, -1, 1])
plt.show()"""