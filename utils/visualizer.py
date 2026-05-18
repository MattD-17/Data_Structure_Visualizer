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
        xaxis=dict(visible=False, range=[-1, 2]),
        yaxis=dict(visible=False),
        margin=dict(l=20,r=20,t=20,b=20)
    )

    # draw each item
    for i, val in enumerate(items):
        # draw rectangle for each item
        fig.add_shape(
            type="rect",
            x0=0,
            y0= i,
            x1= 1,
            y1=i + 1
        )

        # print each item inside rectangle
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

    # draw stack outline
    fig.add_shape(
    type="rect",
    x0=0,
    x1=1,
    y0=0,
    y1=max_size,
    line=dict(dash="dash")
    )

    # create layout such that the whole stack is visible
    fig.update_layout(
        height=400,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False, range=[0, max_size]),
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white"
    )
    


    return fig


def draw_linked_list(linked_list, max_size):

    fig = go.Figure()

    fig.update_layout(
        xaxis=dict(visible=False, range=[-1, 10]),
        yaxis=dict(visible=False),
        margin=dict(l=20, r=20, t=20, b = 20)
    )

    save_max = 0

    for i, val in enumerate(linked_list):
        
        save_max = i
        fig.add_shape(
            type="rect",
            x0=2*i,
            y0=0,
            x1=(2*i)+1,
            y1=1
        )

        fig.add_annotation(
            x=(2*i)+0.5,
            y=0.5,
            text=str(val),
            font=dict(color="red",
                      size=14,
                      family="Arial"
            ),
            showarrow=False
        )

        fig.add_annotation(
            x=(2*i+2), y=0.5,
            ax=(2*i)+1, ay=0.5,
            xref="x", yref="y",
            axref="x", ayref="y",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=1,
            arrowcolor="red"
        )

    fig.add_shape(
        type="rect",
        x0=2*save_max+2,
        y0=0,
        x1=2*save_max+3,
        y1=1
    )

    fig.add_annotation(
        x=2*save_max+2.5,
        y=0.5,
        text="None",
        font=dict(color="red",
        size=14,
        family="Arial")
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


def draw_binary_tree(items, edges, max_size):

    fig = go.Figure()

    # adjust layout to fit all nodes to be visible within figure layout
    fig.update_layout(
        xaxis=dict(visible=False, range=[-max_size*2, max_size*2]),
        yaxis=dict(visible=False, range=[-max_size*2, 1]),
        margin=dict(l=20, r=20, t=20, b=20)
    )

    for i, item in enumerate(items):
        
        fig.add_shape(
            type="rect",
            x0=2*item.x,
            x1=2*item.x + 1,
            y0=2*item.y,
            y1=2*item.y + 1
        )

        fig.add_annotation(
            x=2*item.x+0.5,
            y=2*item.y + 0.5,
            text=str(item.value),
            font=dict(color="red",
                      size=14,
                      family="Arial"
            ),
            showarrow=False
        )   

    for edge in edges:

        fig.add_annotation(
            x=2*edge.x_coords[1] + 0.5,
            y=2*edge.y_coords[1] + 1,
            ax=2*edge.x_coords[0] + 0.5,
            ay=2*edge.y_coords[0],
            xref="x", yref="y",
            axref="x", ayref="y",
            showarrow=True,
            arrowhead=2,
            arrowsize=1,
            arrowwidth=1,
            arrowcolor="red"
        )    

    fig.update_layout(
        height=400,
        xaxis=dict(visible=False),
        yaxis=dict(visible=False, range=[-max_size*2, 1]),
        margin=dict(l=20, r=20, t=20, b=20),
        paper_bgcolor="white",
        plot_bgcolor="white"
    )

    return fig