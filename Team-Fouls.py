import matplotlib.pyplot as plt

# Example data for teams
teams = ['WVU Tech Golden Bears', 'Eastern Kentucky Colonels']
fouls = [16, 10]

# Create a bar graph
plt.bar(teams, fouls)

# Add title and labels
plt.title('Team Fouls')
plt.xlabel('Teams')
plt.ylabel('Fouls')

# Show the plot
plt.show()
