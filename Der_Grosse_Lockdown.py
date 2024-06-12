import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

external_stylesheets = ['/assets/styles.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Nav([
        html.Ul([
            html.Li(html.A('Home', href='/')),
            html.Li(html.A('Über das Projekt', href='/about')),
            html.Li(html.A('Ergebnisse', href='/results')),
            html.Li(html.A('Diskussion', href='/discussion')),
            html.Li(html.A('Literatur', href='/references')),
            html.Li(html.A('Kontakt', href='/contact'))
        ], className='nav-list')
    ], className='navbar'),
    html.Div(id='page-content')
])

home_page = html.Div([
    html.Section(id='home', className='hero-section', children=[
        html.Div([
            html.H1('Der große Lockdown 2020-2021', className='hero-title'),
            html.P('Here is where your presentation begins', className='hero-description'),
            html.Button('Mehr erfahren', className='hero-button')
        ], className='hero-content')
    ])
])

about_page = html.Div([
    html.Section(id='about', children=[
        html.H2('Über das Projekt'),
        html.P('Detaillierte Beschreibung des Projekts, seiner Ziele und Methodik.')
    ], className='section')
])

results_page = html.Div([
    html.Section(id='results', children=[
        html.H2('Ergebnisse'),
        dcc.Graph(
            id='example-graph',
            className='graph',
            figure={
                'data': [
                    {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                    {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Montreal'}
                ],
                'layout': {
                    'title': 'Ergebnisse'
                }
            }
        )
    ], className='section')
])

discussion_page = html.Div([
    html.Section(id='discussion', children=[
        html.H2('Diskussion'),
        html.P('Analyse der Ergebnisse, Herausforderungen und zukünftige Forschungsmöglichkeiten.')
    ], className='section')
])

references_page = html.Div([
    html.Section(id='references', children=[
        html.H2('Literatur'),
        html.Ul([
            html.Li('Quelle 1'),
            html.Li('Quelle 2'),
            html.Li('Quelle 3')
        ])
    ], className='section')
])

contact_page = html.Div([
    html.Section(id='contact', children=[
        html.H2('Kontakt'),
        html.P('Kontaktinformationen des Präsentierenden.'),
        html.A('Download Handout als PDF', href='/path/to/handout.pdf', className='download-link')
    ], className='section')
])

footer = html.Footer([
    html.P('Präsentierende Kontaktinformationen und soziale Medien Links')
], className='footer')

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/about':
        return about_page
    elif pathname == '/results':
        return results_page
    elif pathname == '/discussion':
        return discussion_page
    elif pathname == '/references':
        return references_page
    elif pathname == '/contact':
        return contact_page
    else:
        return home_page

if __name__ == '__main__':
    app.run_server(debug=True)
