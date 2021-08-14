import logging
import torchaudio
from torchaudio import transforms

def load_audio(audio_file):
    """Loads an audio file signal and sampling rate using torchaudio.
    
    
    Parameters
    ----------
    audio_file : str
        String containing the audio file to loaded location
        
    Returns
    -------
    sig : torch.Tensor
        Tensor containing the apmplitude of the signal for the different channels
    sr : int
        Sampling rate of the audio file
    """
    
    logging.info("Loading audio file")
    
    sig, sr = torchaudio.load(audio_file)
    
    return sig, sr


def db_mel_spectrogram(sig, sr, n_fft=1024, hop_length=None, n_mels=64, top_db=80):
    """Convert a loaded audio signal to a decibel mel spectrogram.
    
    Parameters
    ----------
    sig : torch.Tensor
        Tensor containing the amplitude of the signal for the different channels
    sr : int
        Sampling rate of the audio file
    n_fft : int
        Window length for each time section
    hop_length : int
        Number of samples by wich to slide the window at each step
    n_mels : int
        Number of frequency bands
    top_db : int
        Minimum negative cut-off in decibels
        
    Returns
    -------
    db_mel_spectrogram : torch.Tensor
        Tensor containing all the information of the devcibel mel spectrogram
    """
    
    logging.info("Converting signal to db mel spectrogram")

    amplitude_mel_spectrogram = transforms.MelSpectrogram(sr, n_fft=n_fft, hop_length=hop_length, n_mels=n_mels)(sig)
    
    db_mel_spectrogram = transforms.AmplitudeToDB(top_db=top_db)(amplitude_mel_spectrogram)
    
    return db_mel_spectrogram


def standardize_sampling_rate(sig, new_sr):
    """Resamples the audio signal to the new sampling rate.
    
    Parameters
    ----------
    sig : torch.Tensor
        Tensor containing the amplitude of the signal for the different channels
    new_sr : int
        New sampling rate to convert the signal 
        
    Returns
    -------  
    new_sig : torch.Tensor
        New signal with the new sampling rate.
    """
    
    