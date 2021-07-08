import seaborn
import matplotlib.pyplot as plt

def plot_spectrogram(spectrogram):
    """Plot the multiple channels of the supplied mel spectrogram
    
    Parameters
    ----------
    mel_spectrogram : torch.Tensor
        Tensor with all the information of the mel spectrogram
    """
    
    number_channels = spectrogram.shape[0]
    
    fig, axes = plt.subplots(number_channels, 1, figsize=(18, 8))
    
    for c in range(number_channels):
        seaborn.heatmap(spectrogram[c], ax=axes[c])
        

def plot_audio(audio_signal):
    """Plots the audio signal amplitude over time 
    
    Parameters
    ----------
    audio_signal : torch.Tensor
        Tensor containing the amplitude of the signal for the different channels
    """
    
    number_channels = audio_signal.shape[0]
    
    fig, axes = plt.subplots(number_channels, 1, figsize=(18, 8))
    
    for c in range(number_channels):
        axes[c].plot(audio_signal[c])
    