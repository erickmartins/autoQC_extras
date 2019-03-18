from append_data import append_data_pow, append_data_psf

def test_newframe_empty_psf():
    import pandas as pd
    newframe = pd.DataFrame()
    oldframe = pd.DataFrame(['test'])
    folder = "test"
    assert append_data_psf(newframe,oldframe,folder).equals(oldframe)

def test_newframe_empty_pow():
    import pandas as pd
    newframe = pd.DataFrame()
    oldframe = pd.DataFrame(['test'])
    folder = "test"
    assert append_data_pow(newframe,oldframe,folder).equals(oldframe)

if __name__ == "__main__":
    import pandas as pd
    new = pd.read_csv("test_data/summary_power.csv")
    first = pd.DataFrame()
    old = pd.read_csv("test_data/summary_power.csv")
    print(append_data_pow(old,first, "20180325"))
    
    print(append_data_pow(new,old, "20190315"))
    