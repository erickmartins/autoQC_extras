import plotly as py
import plotly.graph_objs as go
import pandas as pd
import numpy as np



def plot_psf(frame):
    newframe = pd.DataFrame()
    counter = 0
    for index, row in frame.iterrows():
            
        
        for i in range(3,6):
            
            newframe.loc[counter,'date'] = row['date']
            measure = row[i]
            newframe.loc[counter,'Rayleigh limit (um)'] = measure
            if i == 3:
                newframe.loc[counter,'measurement'] = 'red'
            if i == 4:
                newframe.loc[counter,'measurement'] = 'blue'
            if i == 5:
                newframe.loc[counter,'measurement'] = 'green'
            counter = counter +1 
    summary = newframe.groupby(['date', 'measurement']).aggregate(np.average)    
    summary = summary.add_suffix('_summary').reset_index()
    
    x_points = newframe[newframe['measurement'] == 'red']
    y_points = newframe[newframe['measurement'] == 'blue']
    z_points = newframe[newframe['measurement'] == 'green']
    
    trace1x = go.Scatter(
    x = x_points['date'],
    y = x_points['Rayleigh limit (um)'],
    mode='markers',
    opacity = 0.5,
    name = 'x',
    marker=dict(
        size=10,
        color = x_points['measurement'], #set color equal to a variable
        colorscale='Viridis',
        showscale=False,
        
        line = dict(
            color = 'rgb(0, 0, 0)',
            width = 2
          )
    )
    )

    trace1y = go.Scatter(
    x = y_points['date'],
    y = y_points['Rayleigh limit (um)'],
    mode='markers',
    name = 'y',
    opacity = 0.5,
    marker=dict(
        size=10,
        color = y_points['measurement'], #set color equal to a variable
        colorscale='Viridis',
        showscale=False,
        line = dict(
            color = 'rgb(0, 0, 0)',
            width = 2
          )
    )
    )

    trace1z = go.Scatter(
    x = z_points['date'],
    y = z_points['Rayleigh limit (um)'],
    mode='markers',
    name = 'z',
    opacity = 0.5,
    marker=dict(
        size=10,
        color = z_points['measurement'], #set color equal to a variable
        colorscale='Viridis',
        showscale=False,
        line = dict(
            color = 'rgb(0, 0, 0)',
            width = 2
          )
    )
    )
    
    trace2 = go.Scatter(
    x = summary['date'],
    y = summary['Rayleigh limit (um)_summary'],
    mode='markers',
    opacity = 0.5,
    showlegend=False,
    marker=dict(
        size=15,
        
        showscale=False,
        symbol='line-ew-open',
        color = summary['measurement'],
        
        line = {
                
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
            'y0': 0.25,
            'y1': 0.25,
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
            'y0': 0.55,
            'y1': 0.55,
            'line': {
                'color': 'rgb(10, 171, 30)',
                'width': 3,
                'dash': 'dash'
            },
        },
    ],
    # 'annotations': [
    #     dict(
    #         x='2018-03-01',
    #         y=0.18,
    #         xref='x',
    #         yref='y',
    #         text='Lateral diffraction limit',
            
    #     ),
    #     dict(
    #         x='2018-03-01',
    #         y=0.48,
    #         xref='x',
    #         yref='y',
    #         text='Axial diffraction limit',
            
    #     )
    # ]
}
    trace3 = go.Scatter(
    x=['2018-03-01','2018-03-01'],
    y=[0.18, 0.48],
    text=['Lateral diffraction limit', 'Axial diffraction limit'],
    mode='text',
    textfont=dict(
        color='black',
        size=10,
        family='Arial',
    ),
    showlegend=False
)

    
    data = [trace1x, trace1y, trace1z, trace2, trace3]
    fig = {
    'data': data,
    'layout': layout,
}
    url = py.offline.plot(fig, filename="psf.html")

    return []


def plot_pow(frame):
    lengths = frame.laser_wavelength.unique()
    data = []
    for length in lengths:
        subframe = frame[frame['laser_wavelength']==length]
        subframe = subframe.sort_values(['date'])
        trace = go.Scatter(
            x = subframe['date'],
            y = subframe['laser_power'],
            mode='lines+markers',
            opacity = 1.0,
            name = str(length),
            marker=dict(
                size=10,
                color = 'rgb'+str(wavelength_to_rgb(int(length),1.0)), #set color equal to a variable
                
                showscale=False,
                line = dict(
                    color = 'black',
                    width = 1.5
                )
            
                
            ),
            line = dict(
                    color = 'rgb'+str(wavelength_to_rgb(int(length),1.0)),
                    width = 3
                )
            )
        data.append(trace)
    url = py.offline.plot(data, filename="pow.html")
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