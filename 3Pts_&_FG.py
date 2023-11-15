import matplotlib.pyplot as plt
# Data for Eastern Kentucky
eastern_kentucky_fg = 44
eastern_kentucky_fga = 104
eastern_kentucky_3pt = 15
eastern_kentucky_3pta = 41
# Data for WVU Tech
wvu_tech_fg = 31
wvu_tech_fga = 76
wvu_tech_3pt = 6
wvu_tech_3pta = 20
# Calculate percentages
eastern_kentucky_fg_percentage = eastern_kentucky_fg / eastern_kentucky_fga * 100
eastern_kentucky_3pt_percentage = eastern_kentucky_3pt / eastern_kentucky_3pta * 100
wvu_tech_fg_percentage = wvu_tech_fg / wvu_tech_fga * 100
wvu_tech_3pt_percentage = wvu_tech_3pt / wvu_tech_3pta * 100
# Create the graph
fig, ax = plt.subplots()
# Set the labels
ax.set_xlabel("Team")
ax.set_ylabel("Percentage")
ax.set_title("Field Goal and 3-Point Percentages")
# Set the bars
ax.bar(["Eastern Kentucky", "WVU Tech"], [eastern_kentucky_fg_percentage, wvu_tech_fg_percentage], label="Field Goal Percentage")
ax.bar(["Eastern Kentucky", "WVU Tech"], [eastern_kentucky_3pt_percentage, wvu_tech_3pt_percentage], label="3-Point Percentage")
# Set the colors
eastern_kentucky_color = "#800000"  # Maroon
eastern_kentucky_3pt_color = "#000000"  # Black
wvu_tech_color = "#FFFF00"  # Yellow
wvu_tech_3pt_color = "#002D72"  # Blue
# Set the bars with custom colors
ax.bar(["Eastern Kentucky", "WVU Tech"], [eastern_kentucky_fg_percentage, wvu_tech_fg_percentage], label="Field Goal Percentage", color=[eastern_kentucky_color, wvu_tech_color])
ax.bar(["Eastern Kentucky", "WVU Tech"], [eastern_kentucky_3pt_percentage, wvu_tech_3pt_percentage], label="3-Point Percentage", color=[eastern_kentucky_3pt_color, wvu_tech_3pt_color])

# Add a legend
ax.legend()
ax.legend(loc='center right', bbox_to_anchor=(1.13, 0.5))

# Show the graph
plt.show()