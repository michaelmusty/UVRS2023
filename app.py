# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import glob
import os

import dash  # type: ignore
import pandas as pd  # type: ignore
import plotly.express as px  # type: ignore
import plotly.io as pio  # type: ignore
from dash import dcc, html  # type: ignore
from dash.dependencies import Input, Output  # type: ignore
from loguru import logger

from build import N

# read table with all race scores

path = os.path.abspath("output_data/tables/")
list_of_filenames = glob.glob(f"{path}/*")
filename_used = max(list_of_filenames, key=os.path.getctime)
logger.info(f"scores file: {filename_used}")
df = pd.read_csv(filename_used)
df = df[["Individual", "Score", "Race", "Age Group", "Net Time"]]
# df.sort_values(by=["Race"], inplace=True)  # maybe we need this for multiple races?

# compute df_overall: overall scores per individual sorted appropriately for download

df_overall = (
    df.groupby(["Individual", "Age Group"])
    .agg({"Score": {lambda x: x.nlargest(N).sum()}})
    .sort_values(["Age Group", ("Score", "<lambda>")], ascending=[True, False])
)
df_overall.columns = df_overall.columns.get_level_values(0)
df_overall.reset_index(inplace=True)

# participation
path = os.path.abspath("output_data/participation/")
list_of_filenames = glob.glob(f"{path}/*")
filename_used = max(list_of_filenames, key=os.path.getctime)
logger.info(f"participation file: {filename_used}")
participation = pd.read_csv(filename_used)
participation = participation[["Individual", "NumRaces"]]


def generate_table(dataframe, max_rows=1000):
    return html.Table(
        [
            html.Thead(html.Tr([html.Th(col) for col in dataframe.columns])),
            html.Tbody(
                [
                    html.Tr(
                        [html.Td(dataframe.iloc[i][col]) for col in dataframe.columns]
                    )
                    for i in range(min(len(dataframe), max_rows))
                ]
            ),
        ]
    )


# all the app stuff

available_indicators = sorted(df["Age Group"].unique())

app = dash.Dash(__name__)
app.title = "2023 UVRS Scorecard"
server = app.server


app.layout = html.Div(
    [
        html.H1("2023 Upper Valley Running Series Scorecard"),
        dcc.Markdown("Select Age Group"),
        # html.Div("Select Age Group"),
        html.Div(
            dcc.Dropdown(
                id="age-group",
                options=[{"label": i, "value": i} for i in available_indicators],
                value="Age Group",
            ),
            style={"width": "20%"},
        ),
        html.H2(f"Overall scores"),
        html.Button("Download overall scores CSV", id="btn_overall_scores_csv"),
        dcc.Download(id="download_overall_scores_csv"),
        dcc.Graph(id="overall_scores"),
        html.H2("Scores for all races"),
        html.Button(
            "Download scores for all races CSV", id="btn_scores_for_all_races_csv"
        ),
        dcc.Download(id="download_scores_for_all_races_csv"),
        dcc.Graph(id="all_scores"),
        html.H2("Participation"),
        # dcc.Graph(
        #     figure = px.bar(
        #         participation,
        #         y="Individual",
        #         x="NumRaces",
        #         orientation="h",
        #         barmode="stack",
        #     )
        # ),
        generate_table(participation),
        dcc.Markdown("[github](https://github.com/michaelmusty/UVRS2023)"),
    ]
)


@app.callback(
    Output("download_overall_scores_csv", "data"),
    Input("btn_overall_scores_csv", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df_overall.to_csv, "uvrs2023_overall_scores.csv")


@app.callback(
    Output("download_scores_for_all_races_csv", "data"),
    Input("btn_scores_for_all_races_csv", "n_clicks"),
    prevent_initial_call=True,
)
def func(n_clicks):
    return dcc.send_data_frame(df.to_csv, "uvrs2023_scores_for_all_races.csv")


@app.callback(Output("overall_scores", "figure"), Input("age-group", "value"))
def update_graph(age_group):
    dff = df_overall[df_overall["Age Group"] == age_group]
    fig = px.bar(
        dff,
        y="Individual",
        x="Score",
        orientation="h",
        barmode="stack",
    )
    fig.update_layout(barmode="stack", yaxis={"categoryorder": "total ascending"})
    return fig


@app.callback(Output("all_scores", "figure"), Input("age-group", "value"))
def update_graph(age_group):
    dff = df[df["Age Group"] == age_group]
    fig = px.bar(
        dff,
        y="Individual",
        x="Score",
        hover_data=["Net Time"],
        color="Race",
        orientation="h",
        barmode="stack",
    )
    fig.update_layout(barmode="stack", yaxis={"categoryorder": "total ascending"})
    return fig


if __name__ == "__main__":
    app.run_server(debug=True)
