import matplotlib.pyplot as plt

from helpers import ensure_dir


def plot_complex2d(real_x, complex_y,
                   title='', legend=None,
                   xlabel='x', ylabel='amplitude',
                   drawlines=True, drawdots=True):
    '''
    Plot functions with real domain and complex range in a 2d plot
    '''
    fig = plt.figure()
    ax = fig.add_subplot()

    if (drawdots):
        ax.plot(real_x, complex_y.real, 'b.')
        ax.plot(real_x, complex_y.imag, 'r.')

    if drawlines:
        ax.plot(real_x, complex_y.real, 'b-')
        ax.plot(real_x, complex_y.imag, 'r-')

    if legend:
        ax.legend(legend, loc='upper center', bbox_to_anchor=(
            0.5, -.15), ncol=2, fancybox=True)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.grid()
    return fig, ax


def plot_complex3d(real_x, complex_y,
                   title='', legend=None,
                   xlabel='x', ylabel='Re{f(x)}', zlabel='Im{f(x)}'):
    '''
    Plot functions with real domain and complex range in a 3d plot
    '''
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')

    ax.plot(real_x, complex_y.real, complex_y.imag, 'b.')
    ax.plot(real_x, complex_y.real, complex_y.imag, 'b-')

    # Sometimes necessary to make sure limits are shown on graph
    ax.set_xlim(min(real_x), max(real_x))
    ax.set_ylim(min(complex_y.real), max(complex_y.real))
    ax.set_zlim(min(complex_y.imag), max(complex_y.imag))

    if legend:
        ax.legend(legend, loc='upper center', bbox_to_anchor=(0.5, -.15),
                  ncol=2, fancybox=True)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_zlabel(zlabel)
    ax.set_title(title)
    return fig, ax


def saveplot(filepath, *args, **kwargs):
    '''
    Save plot to file, ensuring that filepath exists
    '''
    ensure_dir(filepath)
    plt.savefig(filepath, *args, **kwargs)
