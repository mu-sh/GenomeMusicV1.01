import numpy as np
import matplotlib.pyplot as plt

def dict_to_fft(frequency_dict, time):
    # Generate a signal from the dictionary
    signal = []
    for freq, duration in frequency_dict.items():
        signal += [freq] * int(duration * time)
    signal = np.array(signal)

    # Perform FFT
    signal_fft = np.fft.fft(signal)
    signal_fft = np.abs(signal_fft)

    # Plot the FFT spectrum
    plt.plot(signal_fft)
    plt.xlabel('Frequency')
    plt.ylabel('Amplitude')
    plt.show()
