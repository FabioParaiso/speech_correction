import os

import pickle
import pytest
import torch

from speech import data


@pytest.fixture
def rootdir():
    return os.path.dirname(os.path.abspath(__file__))


def test_load_audio(rootdir):
    
    audio_file = os.path.join(rootdir, 'validation_data/audio.wav')
    result, sr = data.load_audio(audio_file)
    
    expected_pickle_file = os.path.join(rootdir, 'validation_data/signal.pickle')
    expected = pickle.load(open(expected_pickle_file, 'rb'))
    
    assert torch.eq(result, expected).all()
    
    
def test_db_mel_spectrogram(rootdir):
    
    audio_file = os.path.join(rootdir, 'validation_data/audio.wav')
    sig, sr = data.load_audio(audio_file)
    result = data.db_mel_spectrogram(sig, sr)
    
    expected_pickle_file = os.path.join(rootdir, 'validation_data/db_mel_spectrogram.pickle')
    expected = pickle.load(open(expected_pickle_file, 'rb'))
    
    assert torch.eq(result, expected).all()
    

    