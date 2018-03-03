import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')

species.fillna('No Intervention', inplace = True)


protection_counts = species.groupby('conservation_status')\
    .scientific_name.nunique().reset_index()\
    .sort_values(by='scientific_name')

    
print protection_counts

plt.figure(figsize=(10,4))
ax = plt.subplot()
plt.bar(range(5), protection_counts.scientific_name)
ax.set_xticks(range(len(protection_counts.scientific_name)))
ax.set_xticklabels(protection_counts.conservation_status)
plt.ylabel('Number of Species')
plt.title('Conservation Status by Species')
plt.show()