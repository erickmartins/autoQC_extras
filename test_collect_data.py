from collect_data import collect_data_pow, collect_data_psf
import pandas as pd

def test_empty_folder_psf():
    folder = []
    assert collect_data_psf(folder) == []

def test_empty_folder_pow():
    folder = []
    assert collect_data_psf(folder) == []

def test_no_file_psf():
    folder = '.'
    assert collect_data_psf(folder) == []

def test_no_file_pow():
    folder = '.'
    assert collect_data_pow(folder) == []

def test_return_type_psf():
    folder = './test_data'
    assert isinstance(collect_data_psf(folder), pd.DataFrame)

def test_return_type_pow():
    folder = './test_data'
    assert isinstance(collect_data_psf(folder), pd.DataFrame)

def test_return_size_psf():
    folder = './test_data'
    print(collect_data_psf(folder).shape)
    assert collect_data_psf(folder).shape == (9,5)

def test_return_size_pow():
    folder = './test_data'
    assert collect_data_pow(folder).shape == (4,2)
