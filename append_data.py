def append_data_psf(data, frame, folder):
    if (data.empty):
        return frame
    if (frame.empty):
        data.insert(0,'date', folder)
        return data
    return []

def append_data_pow(data, frame, folder):
    if (data.empty):
        return frame
    if (frame.empty):
        data.insert(0,'date', folder)
        return data
    return []