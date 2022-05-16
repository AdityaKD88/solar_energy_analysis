import pandas as pd
import plotly
import plotly.express as px
import json
from flask import Flask, render_template
app = Flask(__name__)

df = pd.read_csv('datasets/dataset.csv')

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/usage')
def usage():
  fig1 = px.bar(df,x='Urban Utility',y='State',color='State',title='Energy Usage in urban area',height=600)
  graph1 = json.dumps(fig1, cls=plotly.utils.PlotlyJSONEncoder)

  fig2 = px.bar(df,x='Rural Utility',y='State',color='State',title='Energy Usage in rural area',height=600)
  graph2 = json.dumps(fig2, cls=plotly.utils.PlotlyJSONEncoder)

  return render_template('usage.html',graph1=graph1,graph2=graph2)

@app.route('/solarwind')
def solarwind():
  sp_df=df.sort_values('Solar Photovoltic',ascending=False)
  sp_df=sp_df[:20]
  fig3 = px.bar(sp_df,x='State',y='Solar Photovoltic',color='State',
          title='States with highest Solar Photovotic Energy production',
          labels={'x':'State','y':'Energy'})
  graph3 = json.dumps(fig3, cls=plotly.utils.PlotlyJSONEncoder)

  st_df=df.sort_values('Solar Thermal',ascending=False)
  st_df=st_df[:15]
  fig4 = px.bar(st_df,x='State',y='Solar Thermal',color='State',
          title='States with highest Solar Thermal Energy production',
          labels={'x':'State','y':'Energy'})
  graph4 = json.dumps(fig4, cls=plotly.utils.PlotlyJSONEncoder)

  onw_df=df.sort_values('Onshore Wind',ascending=False)
  onw_df=onw_df[:17]
  fig5 = px.bar(onw_df,x='State',y='Onshore Wind',color='State',
          title='States with highest onshore wind Energy production',
          labels={'x':'State','y':'Energy'})
  graph5 = json.dumps(fig5, cls=plotly.utils.PlotlyJSONEncoder)

  ofw_df=df.sort_values('Offshore Wind',ascending=False)
  ofw_df=ofw_df[:20]
  fig6 = px.bar(ofw_df,x='State',y='Offshore Wind',color='State',
          title='States with highest offshore wind Energy production',
          labels={'x':'State','y':'Energy'})
  graph6 = json.dumps(fig6, cls=plotly.utils.PlotlyJSONEncoder)

  return render_template('solarwind.html',graph3=graph3,graph4=graph4,graph5=graph5,graph6=graph6)

@app.route('/bio')
def bio():
  bs_df=df.sort_values('Bio-Solid',ascending=False)
  bs_df=bs_df[:20]
  fig7 = px.bar(bs_df,x='State',y='Bio-Solid',color='State',
          title='States with highest Bioplant-Solid Energy production',
          labels={'x':'State','y':'Energy'})
  graph7 = json.dumps(fig7, cls=plotly.utils.PlotlyJSONEncoder)

  bg_df=df.sort_values('Bio-gas',ascending=False)
  bg_df=bg_df[:20]
  fig8 = px.bar(bg_df,x='State',y='Bio-gas',color='State',
          title='States with highest Bioplant-Gas Energy production',
          labels={'x':'State','y':'Energy'})
  graph8 = json.dumps(fig8, cls=plotly.utils.PlotlyJSONEncoder)

  hp_df=df.sort_values('Hydropower',ascending=False)
  hp_df=hp_df[:20]
  fig9 = px.bar(hp_df,x='State',y='Hydropower',color='State',
          title='States with highest Hydropower Energy production',
          labels={'x':'State','y':'Energy'})
  graph9 = json.dumps(fig9, cls=plotly.utils.PlotlyJSONEncoder)

  hsc_df=df.sort_values('Hydropower Sites Count',ascending=False)
  hsc_df=hsc_df[:20]
  fig10 = px.bar(hsc_df,x='State',y='Hydropower Sites Count',color='State',
          title='States with highest Hydropower Sites Count',
          labels={'x':'State','y':'Energy'})
  graph10 = json.dumps(fig10, cls=plotly.utils.PlotlyJSONEncoder)

  return render_template('bio.html',graph7=graph7,graph8=graph8,graph9=graph9,graph10=graph10)

@app.route('/thermal')
def thermal():
  hy_df=df.sort_values('Hydrothermal',ascending=False)
  hy_df=hy_df[:12]
  fig11 = px.bar(hy_df,x='State',y='Hydrothermal',color='State',
          title='States with highest Hydrothermal Energy production',
          labels={'x':'State','y':'Energy'})
  graph11 = json.dumps(fig11, cls=plotly.utils.PlotlyJSONEncoder)

  geo_df=df.sort_values('Enhanced Geothermal',ascending=False)
  geo_df=geo_df[:20]
  fig12 = px.bar(geo_df,x='State',y='Enhanced Geothermal',color='State',
          title='States with highest Geothermal Energy production',
          labels={'x':'State','y':'Energy'})
  graph12 = json.dumps(fig12, cls=plotly.utils.PlotlyJSONEncoder)

  return render_template('thermal.html',graph11=graph11,graph12=graph12)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 