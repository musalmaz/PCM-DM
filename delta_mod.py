import numpy as np
import matplotlib.pyplot as plt

# m(t) = − 2 cos(200π t) + sin(50π t)
bandwith = 100
nyquist_rate = 2 * bandwith
sampled_frequency = 4 * nyquist_rate
signal_duration  = 2
time = np.arange(start=1,stop=signal_duration * sampled_frequency) / sampled_frequency  # 1599 sample
message = -2 * np.cos(200 * np.pi * time) + np.sin(50 * np.pi * time)
message_derivative = 2 * 200 * np.pi * np.sin(200 * np.pi * time) + 50 * np.pi * np.cos(50 * np.pi * time)
max_message_derivative = np.amax(message_derivative)
#print(message)
#print(max_message_derivative)  # 1401.7597190428908
#delta_epsilon = max_message_derivative / sampled_frequency
#print(delta_epsilon) # 1.7521996488036136
#print(len(time))
step_list = np.zeros_like(message)
step_list[0] = 0
epsilons = np.zeros_like(message)
delta_epsilon = 0.2
const_epsilon = delta_epsilon
for index in range(len(message)):
    if message[index] > delta_epsilon:
        epsilons[index] = const_epsilon
        delta_epsilon += 1
    else:
        epsilons[index] = - const_epsilon
        delta_epsilon -= 1
    if index != len(message)-  1:
        step_list[index+ 1] = delta_epsilon
modulated_output = np.zeros_like(epsilons)
for i in range(len(epsilons)):
    if epsilons[i] < 0:
        modulated_output[i] = 0
    else:
        modulated_output[i] = 1
#print(len(time), len(step_list))
result = []
for i in range(11):
    result.append(modulated_output[i])
print(*result, sep='  ')
plt.figure(figsize=(12,8))
plt.subplot(2, 1, 1)
plt.plot(time,message,'g')
plt.step(time, step_list, 'r')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Message signal')
plt.axis([0, 0.1, -3, 4])

plt.subplot(2,1,2)
plt.scatter(time,epsilons)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Epsilon')
plt.axis([0, 0.1, -0.3, 0.3])
plt.show()
