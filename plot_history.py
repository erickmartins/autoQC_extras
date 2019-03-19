import pandas as pd
from get_directory import get_directory, get_subdirectories
import os
from append_data import append_data_pow,append_data_psf
from collect_data import collect_data_psf,collect_data_pow, collect_limits
from plot import plot_psf, plot_pow

def plot_history():
    directory = get_directory()
    lateral, axial = collect_limits(directory)
    print(lateral, axial)
    subs = get_subdirectories(directory)
    frame_psf = pd.DataFrame()
    frame_pow = pd.DataFrame()
    for folder in subs:
        data_psf = collect_data_psf(os.path.join(directory,folder))
        data_pow = collect_data_pow(os.path.join(directory,folder))
        if isinstance(data_pow, pd.DataFrame):
            frame_pow = append_data_pow(data_pow, frame_pow, folder)
        if isinstance(data_psf, pd.DataFrame):
            frame_psf = append_data_psf(data_psf, frame_psf, folder)
    
    plot_psf(frame_psf,directory,lateral,axial)
    plot_pow(frame_pow,directory)



    return



if __name__ == "__main__":
    plot_history()