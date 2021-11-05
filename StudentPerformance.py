from enum import unique
import dash 
from dash import html 
from dash import dcc
from dash.dependencies import Input, Output, State
from dash.development.base_component import Component
from dash.html.H1 import H1
from pandas.core.indexes import multi 
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd



app = dash.Dash(__name__,external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css'])
data = pd.read_csv('StudentsPerformance.csv')
listy = ['math score' , 'reading score' , 'writing score']                    
df_cross = pd.crosstab(data['gender'],data['race/ethnicity'])
d = []
for x in df_cross.columns:
       d.append(go.Bar(name=str(x), x=df_cross.index, y=df_cross[x]))

fig3 = go.Figure(d)
fig3.update_layout(barmode = 'group')

d = []

f = pd.crosstab(data['race/ethnicity'],data['parental level of education'])
for x in f:
       d.append(go.Bar(name=str(x), x=f.index, y=f[x]))
fig4 = go.Figure(d)
fig4.update_layout(barmode = 'group')

app.layout = html.Div(children=[
             html.H1('Student Performance Analysis', style = {'color':'Orange','fontsize':80,'textAlign':'center'}), 

               html.Div(
                [
                    
                    html.H2('Subject Score', style = {'color':'Orange','fontsize':80,'textAlign':'center'}), 

                    dcc.Dropdown( id= 'DD' ,
                    options=[
                    {'label': str(i ), 'value': str(i)} for i in listy],value= 'math score' ,clearable=False,),
                    dcc.Graph( figure  = px.histogram( data ,x= 'math score'  ) ,  id = 'fig' ),
                    html.H2('Correlation', style = {'color':'Orange','fontsize':80,'textAlign':'center'}), 
                    html.Br(),
                    html.Div([ 
                        dcc.Dropdown( id= 'DD2' ,
                    options=[
                    {'label': str(i ), 'value': str(i)} for i in listy],value= 'math score' ,clearable=False,),
                    ],className = 'three columns'),
                    html.Div([
                        dcc.Dropdown( id= 'DD3' ,
                    options=[
                    {'label': str(i ), 'value': str(i)} for i in listy],value= 'math score' ,clearable=False,),
                    ],className = 'three columns') ,
                    html.H1(), 
                    html.Br(),
                    html.Div([ dcc.Graph(figure = px.scatter(data , x='math score' , y= 'reading score'  ),id='fig2' ),]),       

                   
                    
                ],className='six columns'
            
            ),
               
               html.Div(
                [
                    html.H2('Gender vs Race', style = {'color':'Orange','fontsize':80,'textAlign':'center'}), 

                    dcc.Graph(figure=fig3 , id= 'fig3'),
                    html.Br(),
                    html.Br(),
                    html.H2('Race vs Parental Education', style = {'color':'Orange','fontsize':80,'textAlign':'center'}), 
                    dcc.Graph(figure=fig4 , id= 'fig4'),

                    
                    
                   
                    
                ],className='five columns'
            
            ),
  
          
          ])


@app.callback(
    Output(component_property='figure' ,  component_id= 'fig'),
    Output(component_property='figure' ,  component_id= 'fig2'),

    Input (component_property='value' , component_id= 'DD'),
    Input (component_property='value' , component_id= 'DD2'),
    Input (component_property='value' , component_id= 'DD3'),

    


    

)

def listen (z,z1,z2):
    fig = px.histogram( data,x= z)
    fig2=px.scatter(data , x=z1 , y= z2  )

    return fig ,fig2


app.run_server()