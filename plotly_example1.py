import plotly.express as px
import numpy as np
import pandas as pd

# Generate random data for male and female groups
num_samples = 100

# Male data
male_weights = np.random.normal(180, 20, num_samples)  # Mean weight 180 lbs, std dev 20 lbs
male_heights = np.random.normal(70, 3, num_samples)    # Mean height 70 inches, std dev 3 inches

# Female data
female_weights = np.random.normal(140, 15, num_samples)  # Mean weight 140 lbs, std dev 15 lbs
female_heights = np.random.normal(65, 2.5, num_samples)  # Mean height 65 inches, std dev 2.5 inches

male_df = pd.DataFrame({
    'weight': male_weights,
    'height': male_heights,
    'gender': ['male'] * len(male_weights)  # Create a list of 'male' strings
})

female_df = pd.DataFrame({
    'weight': female_weights,
    'height': female_heights,
    'gender': ['female'] * len(female_weights)  # Create a list of 'female' strings
})
data = pd.concat([male_df, female_df], ignore_index=True)

# Create a scatter plot
fig = px.scatter(data_frame=data, x='height', y='weight', color='gender',
                 title='Simple Scatter Plot')

# Show the plot
fig.show()