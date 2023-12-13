import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

# Radar chart data
locations = ['Gaza', 'Hanoi', 'London']
tons_per_sq_km_values = [109.58904109589, 5.95238095238095, 11.64]

# Radar chart Data
lbs_per_sq_km_per_day = [4870.62, 1094, 87.2]  # Update with your data

# Population data
locations1 = ['Gaza', 'Vietnam']
populations = [2100000, 28263031]

# Population per Sq Km data for bar graph
locations_bar = ['Gaza', 'Vietnam']
pop_per_sq_km = [5753.42, 85.33]  # Update with your data

# Bubble chart data
areas = [2100000, 28263031]
bubble_sizes = [2100, 28263]
# Radar chart plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), subplot_kw=dict(polar=True))

# Radar chart 1 - Tons Per Sq Km
labels = np.array(locations)
values = np.array(tons_per_sq_km_values)

num_vars = len(locations)
angles = np.linspace(0, 2 * np.pi, num_vars, endpoint=False).tolist()

values = np.concatenate((values, [values[0]]))
angles += angles[:1]

ax1.fill(angles, values, color='#FF5733', alpha=0.4)
ax1.plot(angles, values, color='#FF5733', linewidth=2, linestyle='dashed',
         marker='o', markersize=8, markerfacecolor='#FFC300', markeredgewidth=2, markeredgecolor='black')

ax1.set_yticklabels([])
ax1.set_xticks(angles[:-1])
ax1.set_xticklabels(labels, fontsize=14, fontname='Ubuntu', color='red')  # Set font color to red

ax1.set_title('Tons Per Sq Km', color='red', fontsize=18, fontname='Times New Roman')  # Set title color to red

# Radar chart 2 - Lbs Per Sq Km Per Day
angles_radar = np.linspace(0, 2 * np.pi, len(locations), endpoint=False).tolist()
values_radar = np.array(lbs_per_sq_km_per_day)

values_radar = np.concatenate((values_radar, [values_radar[0]]))
angles_radar += angles_radar[:1]

ax2.fill(angles_radar, values_radar, color='#FF5733', alpha=0.4)
ax2.plot(angles_radar, values_radar, color='#FF5733', linewidth=2, linestyle='dashed',
          marker='o', markersize=8, markerfacecolor='#FFC300', markeredgewidth=2, markeredgecolor='black')

ax2.set_yticklabels([])
ax2.set_xticks(angles_radar[:-1])
ax2.set_xticklabels(locations, fontsize=14, fontname='Times New Roman', color='red')  # Set font color to red

ax2.set_title('Lbs Per Sq Km Per Day', color='red', fontsize=18, fontname='Times New Roman')  # Set title color to red

plt.tight_layout()
plt.show()

# Population per Sq Km comparison bar graph
fig, (ax3, ax4) = plt.subplots(1, 2, figsize=(12, 6), facecolor='#111111')

colors = ['#2E86C1', '#85C1E9']
cmap = LinearSegmentedColormap.from_list('custom', colors)

bars_bar = ax3.bar(locations_bar, pop_per_sq_km, color=cmap(np.linspace(0, 1, len(locations_bar))))

ax3.set_xticks(np.arange(len(locations_bar)))
ax3.set_xticklabels(locations_bar, color='#FFC300', fontname='Times New Roman')
ax3.set_yticklabels([], fontname='Times New Roman')

ax3.set_title('Population per Sq Km Comparison', color='#FFC300', fontname='Times New Roman', fontsize=18)
ax3.set_xlabel('Locations', color='#FFC300', fontname='Times New Roman')
ax3.set_ylabel('Population per Sq Km', color='#FFC300', fontname='Times New Roman')

ax3.grid(axis='y', linestyle='--', alpha=0.5)

# Population comparison bar graph
bars = ax4.bar(locations1, populations, color=cmap(np.linspace(0, 1, len(locations1))))

ax4.set_xticks(np.arange(len(locations1)))
ax4.set_xticklabels(locations1, color='#FFC300', fontname='Times New Roman')
ax4.set_yticklabels([], fontname='Times New Roman')

ax4.set_title('Population Comparison', color='#FFC300', fontname='Times New Roman', fontsize=18)
ax4.set_xlabel('Locations', color='#FFC300', fontname='Times New Roman')
ax4.set_ylabel('Population', color='#FFC300', fontname='Times New Roman')

ax4.grid(axis='y', linestyle='--', alpha=0.5)

plt.tight_layout()
plt.show()


# Bubble chart
plt.figure(figsize=(8, 6), facecolor='#111111')

x_positions = [0, 1]
plt.scatter(x_positions, [1]*len(locations1), s=bubble_sizes, color=cmap(np.linspace(0, 1, len(locations1))), alpha=0.8, edgecolors='black')

plt.xticks(x_positions, locations1, color='#FFC300', fontname='Times New Roman')
plt.yticks([], fontname='Times New Roman')

for x, area in zip(x_positions, areas):
    plt.text(x, 1, f'{area} km²', color='white', ha='center', va='center', fontname='Times New Roman')

plt.xlim(-0.5, 1.5)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['left'].set_visible(False)
plt.gca().spines['bottom'].set_color('#FFC300')

plt.title('Size Comparison: Gaza vs Vietnam', color='#FFC300', fontname='Times New Roman', fontsize=18)

plt.show()


# Data for lollipop chart
countries = ['Ukraine', 'Iraq', 'Yemen', 'Gaza']
children_killed = [510, 3119, 3774, 5500]
time_periods = [21 * 12 * 4, 14 * 52, 8 * 52, 7]

# Calculate children killed per week
children_per_week = [ck / tp for ck, tp in zip(children_killed, time_periods)]

# Create lollipop chart
fig, ax = plt.subplots(figsize=(8, 6), facecolor='#111111')

bar_colors = cmap(np.linspace(0, 1, len(countries)))

bars = ax.barh(countries, children_per_week, color=bar_colors)

for i, bar in enumerate(bars):
    ax.plot([children_per_week[i]], [i], marker='o', markersize=10, color='#FFC300', mec='black', mew=1.5, alpha=0.7)

ax.set_xlabel('Children Killed Per Week', color='#FFC300', fontsize=14, fontname='Times New Roman')
ax.set_ylabel('Region Under Attack', color='#FFC300', fontsize=14, fontname='Times New Roman')
ax.set_title('Zionist "War" = An Unprecedented Genocide of Children', color='#FFC300', fontsize=20, fontname='Arial')

plt.xticks(color='#FFC300', fontsize=12, fontname='Times New Roman')
plt.yticks(color='#FFC300', fontsize=12, fontname='Times New Roman')
ax.spines['bottom'].set_color('#FFC300')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)

ax.grid(axis='x', linestyle='--', color='#FFC300', alpha=0.3)

plt.tight_layout()
plt.show()

# Data
locations2 = ['Jabalia Refugee Camp', 'Gaza Strip', 'Hanoi', 'London']
tons_per_sq_km_values2 = [2105.26316, 109.58904109589, 5.95238095238095, 11.64]

# Create the plot
plt.figure(figsize=(6, 8))
plt.stem(locations2, tons_per_sq_km_values2, markerfmt=' ', linefmt='C0-', basefmt='k-')
plt.xlabel('Locations')
plt.ylabel('Tons per Sq Km')
plt.title('Tons of Bombs Dropped per Sq Km in Different Locations')
plt.xticks(rotation=45)
plt.tight_layout()

# Show the plot
plt.show()

# Data
areas2 = [1.9, 2100000, 28263031]  # Areas in sq km
bubble_sizes2 = [0.0019, 2100, 28263]  # Bubble sizes for visualization

# Labels for the bubbles
labels = ['Jabalia Refugee Camp', 'Gaza', 'Vietnam']

# Create the bubble chart
plt.figure(figsize=(8, 6))
plt.scatter(range(len(areas2)), [1] * len(areas2), s=bubble_sizes2, alpha=0.5)
plt.xticks(range(len(areas2)), labels)
plt.xlabel('Locations')
plt.title('Relative Sizes of Areas')

# Set scale to logarithmic for better visualization
plt.yscale('log')
plt.ylabel('Area (sq km)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Show the bubble chart
plt.tight_layout()
plt.show()

