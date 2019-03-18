def collect_data_psf(folder):
    if (folder == []):
        return []
    import pandas as pd
    import os
    if os.path.exists(os.path.join(folder,"summary_PSF.csv")):
        data = pd.read_csv(os.path.join(folder,"summary_PSF.csv"),skiprows=[1])
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
    else:
        return []
    return data