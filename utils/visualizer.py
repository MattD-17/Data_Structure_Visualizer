import plotly.graph_objects as go

def draw_stack(items, max_size=10):
    fig = go.Figure()   # create figure / canvas

    fig.update_layout(
        xaxis=dict(visible=False, range=[-1, 2]),
        yaxis=dict(visible=False),
        margin=dict(l=20, r=20, t=20, b=20)
    )

    # draw rectangle for each element
    for i, val in enumerate(items):
        fig.add_shape(
            type="rect",
            x0=0,
            x1=1,
            y0=i,       # visual stack is shown vertically
            y1=i + 1,
        )

        fig.add_annotation(
            x=0.5,
            y=i + 0.5,
            text=str(val),
            font=dict(color="red",
                    size=14,
                    family="Arial"
            ),
            showarrow=False
        )

    fig.add_shape(
        type="rect",
        x0=0,
        x1=1,
        y0=0,
        y1=max_size,
        line=dict(dash="dash")
    )

    fig.update_layout(
        height=400,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False, range=[0, max_size]),
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white"
    )
    return fig

def draw_queue(items, max_size=10):
    fig= go.Figure()
    
    fig.update_layout(
        xaxis=dict(visible=false, range=[-1, 2]),
        yaxis=dict(visible=false),
        margin=dict(l=20,r=20,t=20,b=20)
    )