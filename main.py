import numpy as np
import matplotlib.pyplot as plt

# Radar chart data
locations = ['Gaza', 'Vietnam', 'Hanoi']
tons_per_sq_km_values = [109.58904109589, 15.0961625554784, 5.95238095238095]

# Population data
locations1 = ['Gaza', 'Vietnam']
populations = [365, 331210]

# Bubble chart data
areas = [365, 331210]
bubble_sizes = [1000, 50000]

# Radar chart plotting
labels = np.array(locations)
values = np.array(tons_per_sq_km_values)

# Number of variables
num_vars = len(locations)

# Compute angle for each axis
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

# Make the plot close to a circle
values = np.concatenate((values, [values[0]]))
angles += angles[:1]

# Create figure and subplot for radar chart
fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Set the background color of the entire plot to black
fig.patch.set_facecolor('black')
ax.set_facecolor('black')

# Plot radar chart with red line and change font color to light blue
ax.fill(angles, values, color='red', alpha=0.25)
ax.plot(angles, values, color='red', linewidth=2)  # Change the line thickness if needed

# Set the labels and change font to sci-fi style, increase size
ax.set_yticklabels([])
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels, fontsize=14, fontname='Times', color='lightblue')

plt.title('Tons Per Sq Km', color='lightblue', fontsize=18, fontname='Times')

# Fancy gridlines
ax.grid(color='lightblue', linestyle='--', linewidth=1, alpha=0.5)

# Population comparison bar graph
plt.figure(figsize=(8, 6), facecolor='black')
bar_color = 'navy'

bars = plt.bar(locations1, populations, color=bar_color)

for bar in bars:
    bar.set_edgecolor('black')
    bar.set_linewidth(2)

plt.xticks(color='lightblue', fontname='Times')
plt.yticks(color='lightblue', fontname='Times')
plt.title('Population Comparison', color='lightblue', fontname='Times', fontsize=18)
plt.xlabel('Locations', color='lightblue', fontname='Times')
plt.ylabel('Population', color='lightblue', fontname='Times')

plt.grid(axis='y', linestyle='--', alpha=0.5)

# Bubble chart
plt.figure(figsize=(8, 6), facecolor='black')

x_positions = [0, 1]
plt.scatter(x_positions, [1]*len(locations1), s=bubble_sizes, color='navy', alpha=0.5)

plt.xticks(x_positions, locations1, color='lightblue', fontname='Times')
plt.yticks([])

for x, area in zip(x_positions, areas):
    plt.text(x, 1, f'{area} km²', color='white', ha='center', va='center', fontname='Times')

plt.xlim(-0.5, 1.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_color('lightblue')

plt.title('Size Comparison: Gaza vs Vietnam', color='lightblue', fontname='Times', fontsize=18)

plt.show()


# Data
countries = ['Ukraine', 'Iraq', 'Yemen', 'Gaza']
children_killed = [510, 3119, 3774, 5500]
time_periods = [21 * 12 * 4, 14 * 52, 8 * 52, 7]

# Calculate children killed per week
children_per_week = [ck / tp for ck, tp in zip(children_killed, time_periods)]

# Create horizontal bar chart
fig, ax = plt.subplots()
bars = ax.barh(countries, children_per_week, color='skyblue')

# Add lollipops
for i, bar in enumerate(bars):
    ax.plot([children_per_week[i]], [i], marker='o', markersize=8, color='orange')

# Set labels and title
ax.set_xlabel('Children Killed Per Week')
ax.set_ylabel('Region Under Attack')
ax.set_title('Zionist "War" = An Unprecedented Genocide of Children')

# Show the plot
plt.tight_layout()
plt.show()
