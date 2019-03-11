def get_directory():
    import easygui

    path = easygui.diropenbox()   

    return path



def get_subdirectories(directory):
    import os

    directories = []
    for root, dirs, files in os.walk(directory):
        directories.append(dir)
    return directories