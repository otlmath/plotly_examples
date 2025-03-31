import plotly.express as px
import numpy as np
import pandas as pd

# Generate fake data
np.random.seed(42)  # For reproducibility
male_height = np.random.normal(175, 7, 100)
male_weight = np.random.normal(75, 10, 100)
female_height = np.random.normal(163, 6, 100)
female_weight = np.random.normal(60, 8, 100)

# Create a Pandas DataFrame
data = pd.DataFrame({
    'Height': np.concatenate([male_height, female_height]),
    'Weight': np.concatenate([male_weight, female_weight]),
    'Gender': ['Male'] * 100 + ['Female'] * 100
})

# Create scatter plot with Plotly Express
fig = px.scatter(
    data,
    x='Height',
    y='Weight',
    color='Gender',
    title='Height vs Weight',
    category_orders={'Gender': ['Male', 'Female']}  # Ensure consistent color order
)

# Add selector
fig.update_layout(
    updatemenus=[
        dict(
            active=0,
            buttons=list([
                dict(label='All',
                     method='update',
                     args=[{'visible': [True, True]}]),
                dict(label='Male',
                     method='update',
                     args=[{'visible': [True, False]}]),
                dict(label='Female',
                     method='update',
                     args=[{'visible': [False, True]}])
            ]),
            x=0.8,
            y=1.15,
            xanchor='left',
            yanchor='top',
        )
    ],
    margin=dict(t=50),
)

fig.show()