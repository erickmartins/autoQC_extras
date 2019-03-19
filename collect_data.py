def collect_data_psf(folder):
    if (folder == []):
        return []
    import pandas as pd
    import os
    if os.path.exists(os.path.join(folder,"summary_PSF.csv")):
        data = pd.read_csv(os.path.join(folder,"summary_PSF.csv"))
        data = data.dropna()

    else:
        return []

    return data

def collect_data_pow(folder):
    import pandas as pd
    import os
    if (folder == []):
        return []

    if os.path.exists(os.path.join(folder,"summary_power.csv")):
        data = pd.read_csv(os.path.join(folder,"summary_power.csv"))
        data = data.dropna()
    else:
        return []
    return data

def collect_limits(folder):
    import pandas as pd
    import os

    if (folder == []):
        return []
    directory = os.path.dirname(folder)
    foldername = folder.split(os.sep)[-1]
    if os.path.exists(os.path.join(directory,"resolution_limits.csv")):
        data = pd.read_csv(os.path.join(directory,"resolution_limits.csv"))
        data = data.dropna()
        lateral = data[data['microscope'] == foldername]['lateral'][0]
        axial = data[data['microscope'] == foldername]['axial'][0]
    else:
        lateral = []
        axial = []
    return lateral,axial