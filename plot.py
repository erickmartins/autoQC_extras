import plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np
import os


def plot_psf(frame, directory, lateral, axial):
    newframe = pd.DataFrame()
    print(frame)
    counter = 0
    for index, row in frame.iterrows():

        for i in range(3, 6):

            newframe.loc[counter, 'date'] = row['date']
            measure = row[i]
            newframe.loc[counter, 'Rayleigh limit (um)'] = measure
            if i == 3:
                newframe.loc[counter, 'measurement'] = 'red'
                newframe.loc[counter, 'axis'] = 'x'
            if i == 4:
                newframe.loc[counter, 'measurement'] = 'blue'
                newframe.loc[counter, 'axis'] = 'y'
            if i == 5:
                newframe.loc[counter, 'measurement'] = 'green'
                newframe.loc[counter, 'axis'] = 'z'
            counter = counter + 1
    summary = newframe.groupby(['date', 'measurement']).aggregate(np.average)
    summary = summary.add_suffix('_summary').reset_index()

    trace1 = go.Scatter(
        x=newframe['date'],
        y=newframe['Rayleigh limit (um)'],

        mode='markers',
        opacity=0.5,
        showlegend=False,
        # hoverinfo="x+y",
        text=newframe['axis'],
        marker=dict(
            size=10,
            color=newframe['measurement'],  # set color equal to a variable
            colorscale='Viridis',
            showscale=False,
            xaxis=dict(
                title='Date',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            ),
            yaxis=dict(
                title='Resolution (um)',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            ),

            line=dict(
                color='rgb(0, 0, 0)',
                width=2
            )
        )
    )

    trace2 = go.Scatter(
        x=summary['date'],
        y=summary['Rayleigh limit (um)_summary'],
        mode='markers',
        name='average',
        opacity=0.5,
        showlegend=False,
        marker=dict(
            size=15,

            showscale=False,
            symbol='line-ew-open',
            color=summary['measurement'],

            line={

                'width': 5
            }

        )
    )

    layout = {


        'yaxis': {
            'range': [0, 1]
        },
        'shapes': [
            # Line reference to the axes
            {
                'type': 'line',
                'xref': 'x',
                'yref': 'y',
                'x0': '2018-01-01',
                'x1': '2019-12-31',
                'y0': lateral,
                'y1': lateral,
                'line': {
                    'color': 'rgb(0, 0, 0)',
                    'width': 3,
                    'dash': 'dash'
                },
            },
            # Line reference to the plot
            {
                'type': 'line',
                'xref': 'x',
                'yref': 'y',
                'x0': '2018-01-01',
                'x1': '2019-12-31',
                'y0': axial,
                'y1': axial,
                'line': {
                    'color': 'rgb(10, 171, 30)',
                    'width': 3,
                    'dash': 'dash'
                },
            },
        ],

    }
    data = [trace1, trace2]
    if (type(lateral) != list):
        trace3 = go.Scatter(
            x=['2018-03-01', '2018-03-01'],
            y=[lateral - 0.07, axial - 0.07],
            text=['Lateral diffraction limit', 'Axial diffraction limit'],
            mode='text',
            textfont=dict(
                color='black',
                size=10,
                family='Arial',
            ),
            showlegend=False
        )
        data.append(trace3)

    fig = {
        'data': data,
        'layout': layout,
    }
    url = py.offline.plot(fig, include_plotlyjs=False, output_type='div')
    f = open(os.path.join(directory, "psf.html"), 'w')
    f.write('<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>\n')
    f.write(url)
    f.close()

    return []


def plot_pow(frame, directory):
    lengths = frame.laser_wavelength.unique()
    data = []
    for length in lengths:
        subframe = frame[frame['laser_wavelength'] == length]
        subframe = subframe.sort_values(['date'])
        trace = go.Scatter(
            x=subframe['date'],
            y=subframe['laser_power'],
            mode='lines+markers',
            opacity=1.0,
            name=str(length),
            marker=dict(
                size=10,
                # set color equal to a variable
                color='rgb' + str(wavelength_to_rgb(int(length), 1.0)),

                showscale=False,
                line=dict(
                    color='black',
                    width=1.5
                )


            ),
            xaxis=dict(
                title='Date',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            ),
            yaxis=dict(
                title='Laser power (mW)',
                titlefont=dict(
                    family='Courier New, monospace',
                    size=18,
                    color='#7f7f7f'
                )
            ),
            line=dict(
                color='rgb' + str(wavelength_to_rgb(int(length), 1.0)),
                width=3
            )
        )
        data.append(trace)
    layout = {
        'xaxis': {
            'range': ['2018-01-01', '2019-12-31']
        }
    }
    fig = {
        'data': data,
        'layout': layout,
    }
    url = py.offline.plot(fig, include_plotlyjs=False, output_type='div')
    f = open(os.path.join(directory, "pow.html"), 'w')
    f.write('<script src="https://cdn.plot.ly/plotly-latest.min.js"></script>\n')
    f.write(url)
    f.close()
    return []


def wavelength_to_rgb(wavelength, gamma=0.8):
    '''This converts a given wavelength of light to an 
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    '''

    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return (int(R), int(G), int(B))
