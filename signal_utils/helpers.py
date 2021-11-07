import os


def ensure_dir(path):
    '''
    Ensure that directory of path exists. Creates directories if needed.
    '''
    directory = os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
