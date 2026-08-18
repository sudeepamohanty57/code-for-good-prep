import plotly.express as px

fig = px.bar(
    df,
    x="city",
    y="income",
    title="Income by City"
)

fig.show()