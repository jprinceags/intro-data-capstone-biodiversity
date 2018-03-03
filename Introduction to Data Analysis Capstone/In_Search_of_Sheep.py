import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

species = pd.read_csv('species_info.csv')
species.fillna('No Intervention', inplace = True)
species['is_protected'] = species.conservation_status != 'No Intervention'

observations = pd.read_csv('observations.csv')
print observations.head()

get_sheep = lambda x: 'Sheep' in x
species['is_sheep'] = species.common_names.apply(get_sheep)

species_is_sheep = species[(species.is_sheep == True)]
print species_is_sheep

sheep_species = species[(species.is_sheep == True)&(species.category == 'Mammal')]
print sheep_species

sheep_observations = pd.merge(sheep_species, observations)
print sheep_observations.head()

obs_by_park = sheep_observations.groupby(['park_name']).observations.sum().reset_index()
print obs_by_park