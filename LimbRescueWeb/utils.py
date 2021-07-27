import os

import numpy as np
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import plotly.offline as plo
from django.conf import settings
from django.core.files.storage import FileSystemStorage


def process_csv(file):
    xs, ys = [], []
    with open(file) as f:
        for line in f:
            x, y, _ = line.split(",")
            if not x.isdigit():
                continue
            xs.append(int(x))
            ys.append(float(y))
    return xs, ys


def plot(file):
    xs, ys = process_csv(file)
    print(xs, ys)
    xs = np.array(xs)
    ys = np.array(ys)
    fig = go.Figure()
    scatter = go.Scatter(
        x=(xs - xs[0]) / 1e9, y=ys, mode="lines", name="test", opacity=0.8, marker_color="green"
    )
    fig.add_trace(scatter)
    plt_div = plo.plot(
        fig, output_type="div", include_plotlyjs=False, show_link=False, link_text=""
    )
    return plt_div

def plot2(file):
    df = pd.read_csv(file)
    df.Time  = (df.Time - df.Time[0]) / 1e9
    fig = go.Figure()

    for arm in ["LEFT_ARM", "RIGHT_ARM"]:
        scatter = go.Scatter(
            x=df.Time, y=df.Value[df.Limb == arm], mode="lines", name=arm, opacity=0.8,
        )
        fig.add_trace(scatter)
    plt_div = plo.plot(
        fig, output_type="div", include_plotlyjs=False, show_link=False, link_text=""
    )
    return plt_div


class OverwriteStorage(FileSystemStorage):
    def get_available_name(self, name, *args, **kwargs):
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return super().get_available_name(name, *args, **kwargs)
