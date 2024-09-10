import dash

import dash_html_components as html


app = dash.Dash(__name__)

app.layout = html.Div([
    html.H1("Main Heading"),
    html.H2("2nd Heading"),
    html.H3("3rd Heading")
    # Add other components if needed
])


if __name__ == "__main__":
    app.run_server(debug=True)
