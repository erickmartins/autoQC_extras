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

def test_oldframe_empty_psf():
    import pandas as pd
    oldframe = pd.DataFrame()
    newframe = pd.DataFrame(['test'])
    compare = newframe.copy()
    folder = "date"
    assert append_data_psf(newframe,oldframe,folder).equals(compare)

def test_oldframe_empty_pow():
    import pandas as pd
    oldframe = pd.DataFrame()
    newframe = pd.DataFrame(['test'])
    compare = newframe.copy()
    folder = "test"
    assert append_data_pow(newframe,oldframe,folder).equals(compare)


    