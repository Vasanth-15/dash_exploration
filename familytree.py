import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
import json, sys

app = dash.Dash()
df=[]
# maxcol=0
# maxrow=0
# mincol=sys.maxsize
# minrow=sys.maxsize

# FAMILY_LIST =   {'GrandFather',
#                  'GrandMother',
#                  'Father',
#                  'Mother',
#                  'Son',
#                  'Daughter'
#                 }

with open("family_tree.json") as dataframe:
    df = json.load(dataframe)

# familykey = []
# for keys in FAMILY_LIST:
#     if keys in df['Family tree']:
#         # print (df['Family tree'][keys])
#         rownum = int(df['Family tree'][keys]['row'])
#         colnum = int(df['Family tree'][keys]['column'])
#         familykey = familykey.append(keys)
#         if rownum > maxrow:
#             maxrow = rownum
#         elif rownum < minrow:
#             minrow = rownum
#         else:
#             pass
#         if colnum > maxcol:
#             maxcol = colnum
#         elif colnum < mincol:
#             mincol = colnum
#         else:
            # pass
# print (df['Family tree'])
# print ("Max row = ",maxrow)
# print ("Min row = ",minrow)
# print ("Max col = ",maxcol)
# print ("Min col = ",mincol)

print (tuple(df['Family tree']))

inoutlines = go.Scatter(
                        x=[],
                        y=[],
                        line={
                            'width': 0.5,
                            'color': '#888'
                        },
                        mode='lines'
                    )
nodes = go.Scatter(
                    y=[],
                    x=[],
                    text=[],
                    textposition='bottom center',
                    mode='markers+text',
                    opacity=0.7,
                    marker={
                        'size':15,
                        'line':{'width':0.5,'color':'white'}
                    },
                )
nodey=[]
inoutlinesy=[]
nodex=[]
inoutlinesx=[]
nodet=[]
for i,item in enumerate(df['Family tree']):
    nodey+=[df['Family tree'][i]['row']]
    nodex+=[df['Family tree'][i]['column']]
    nodet+=[df['Family tree'][i]['name']]
    inoutlinesy+=[df['Family tree'][i]['row'], df['Family tree'][i]['cr0'], None] 
    inoutlinesx+=[df['Family tree'][i]['column'],df['Family tree'][i]['cc0'], None]
nodes['y']=tuple(nodey)
inoutlines['y']=tuple(inoutlinesy)
nodes['x']=tuple(nodex)
inoutlines['x']=tuple(inoutlinesx)
nodes['text']=tuple(nodet)

app.layout = html.Div([
    dcc.Graph(
        id='family_tree',
        figure={
            'data': [nodes, inoutlines],
            'layout': go.Layout(
                xaxis={'autorange': True, 
                       'showgrid': False,
                       'zeroline': False,
                       'showline': False,
                       'ticks': '',
                       'showticklabels': False},
                yaxis={'autorange': True, 
                       'showgrid': False,
                       'zeroline': False,
                       'showline': False,
                       'ticks': '',
                       'showticklabels': False},
                # shapes={'type': 'rect',
                #        'xref': 'paper',
                #        'yref': 'paper',
                #        'x0': 0.25,
                #        'y0': 0,
                #        'x1': 0.5,
                #        'y1': 0.5,
                #        'line':{
                #             'color': 'rgb(50,127,71)',
                #             'width': 3},
                #         },
                hovermode='closest'
                )
            }
        )
    ])

if __name__ == '__main__':
    app.run_server(8050)
