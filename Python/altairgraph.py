import altair as alt
import pandas as pd

alt.data_transformers.enable('csv')

url = "C:/Users/maxwe/OneDrive/Documents/Data Vis/a2-DataVis-5ways/data/penglings.csv"

df = pd.read_csv(url)

print(df)

alt.renderers.enable('mimetype')

chart = alt.Chart(df).mark_point().encode(
    x='flipper_length_mm',
    y='body_mass_g',
    size='bill_length_mm'
)

chart.save('chart.html')
