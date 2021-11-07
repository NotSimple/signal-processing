import numpy as np


def build_space(T, N):
    '''
    Build a linear space centered on the origin

    Parameters
    ----------
    T : int
        Period of linear space
    N : int
        Length of linear space

    Returns
    ----------
    linear_space: ndarray(int)
        linear space of length N
    '''
    space = np.linspace(start=T, stop=N * T, num=N)
    zero_centered_space = space - space[N // 2]
    return zero_centered_space


def sample(f, T, N):
    '''
    Function sampler

    Parameters
    ----------
    f : function
        function to sample
    T : int
        Sampling Period
    N : int
        Number of samples

    Returns
    ----------
    linear_space: ndarray(int)
        linear space of length N
    sampled_f: ndarray(int)
        sampled function of length N
    '''
    x_array = build_space(T, N)
    sampled_f = f(x_array)
    return x_array, sampled_f
