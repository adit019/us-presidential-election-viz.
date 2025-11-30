import pandas as pd
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv('election_data.csv')

years = data['Year']

# Plot popular vote percentage
plt.figure(figsize=(10, 6))
plt.plot(years, data['Democrat'], marker='o', label='Democrat')
plt.plot(years, data['Republican'], marker='o', label='Republican')
plt.plot(years, data['Other'], marker='o', label='Other')
plt.title('U.S. Presidential Elections: Popular Vote Share (1976-2020)')
plt.xlabel('Year')
plt.ylabel('Popular Vote (%)')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('popular_vote.png')
plt.show()

# Plot electoral college votes
plt.figure(figsize=(10, 6))
width = 0.25
plt.bar(years - width, data['Democrat_EV'], width, label='Democrat')
plt.bar(years, data['Republican_EV'], width, label='Republican')
plt.bar(years + width, data['Other_EV'], width, label='Other')
plt.title('U.S. Presidential Elections: Electoral College Votes (1976-2020)')
plt.xlabel('Year')
plt.ylabel('Electoral Votes')
plt.legend()
plt.grid(axis='y')
plt.tight_layout()
plt.savefig('electoral_college.png')
plt.show()
