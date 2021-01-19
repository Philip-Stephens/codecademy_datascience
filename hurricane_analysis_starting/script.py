# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day', 'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen', 'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix', 'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September', 'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August', 'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September', 'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980, 1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185, 160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'], ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'], ['The Bahamas', 'Northeastern United States'], ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'], ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'], ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'], ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'], ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'], ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'], ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'], ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'], ['The Caribbean', 'United States East coast'], ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'], ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'], ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'], ['Central America', 'Yucatn Peninsula', 'South Florida'], ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'], ['The Caribbean', 'Venezuela', 'United States Gulf Coast'], ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'], ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'], ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'], ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'], ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'], ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic', 'Turks and Caicos Islands'], ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M', '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B', '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B', '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90,4000,16,3103,179,184,408,682,5,1023,43,319,688,259,37,11,2068,269,318,107,65,19325,51,124,17,1836,125,87,45,133,603,138,3057,74]

# format damages
def damage_conversion(index):
  conversion = {"M": 1000000, "B": 1000000000}
  if index.endswith("M"):
    return float(index[:1])*conversion["M"]
  elif index.endswith("B"):
    return float(index[:-1])*conversion["B"]
  else:
    return index

updated_damages = []
for cost in damages:
  updated_damages.append(damage_conversion(cost))

# create hurricane dictionary
hurricanes = {}
for i in range(len(names)):
  hurricanes[names[i]] = {
    "Name": names[i],
    "Month": months[i],
    "Year": years[i],
    "Max Sustained Wind": max_sustained_winds[i],
    "Areas Affected": areas_affected[i],
    "Damage": updated_damages[i],
    "Deaths": deaths[i]}

# sort hurricanes by year, can't sort by areas affected
def sorted_hurricanes(sort_key):
  sorted_dictionary = {}
  for i in hurricanes.values():
    current_sort = i[sort_key]
    if current_sort not in sorted_dictionary:
      sorted_dictionary[current_sort] = [i]
    elif current_sort in sorted_dictionary:
      sorted_dictionary[current_sort].append([i])
  return sorted_dictionary

hurricanes_by_year = sorted_hurricanes("Year")

# areas affected and the amount of hurricanes
def area_affected_count():
  import collections
  new_dictionary = collections.defaultdict(int)
  for i in hurricanes.values():
    for area in i["Areas Affected"]:
      new_dictionary[area] += 1
  return new_dictionary

affected_areas_count = area_affected_count()

# area most affected
def max_area_affected():
  max_area = "Central America"
  max_area_count = 0
  for area, count in affected_areas_count.items():
    if count > max_area_count:
      max_area = area
      max_area_count = count
    else:
      continue
  print("{} was affected by {} hurricanes.".format(max_area, max_area_count))

max_area_affected()

# hurricane with most deaths
def max_deaths():
  name = "Cuba I"
  max_death_count = 0
  for k, v in hurricanes.items():
    if v["Deaths"] > max_death_count:
      name = k
      max_death_count = v["Deaths"]
    else: continue
  print("Hurricane {} caused {} deaths.".format(name, max_death_count))

max_deaths()

# mortality scale
def sort_by_mortality_rating():
  mortality_scale = {
    0: 0,
    1: 100,
    2: 500,
    3: 1000,
    4: 10000}
  new_dictionary = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for i in hurricanes.values():
    current_death_count = i["Deaths"]
    if current_death_count <= mortality_scale[0]:
      new_dictionary[0].append([i])
    elif current_death_count <= mortality_scale[1]:
      new_dictionary[1].append([i])
    elif current_death_count <= mortality_scale[2]:
      new_dictionary[2].append([i])
    elif current_death_count <= mortality_scale[3]:
      new_dictionary[3].append([i])
    elif current_death_count <= mortality_scale[4]:
      new_dictionary[4].append([i]) 
    else:
      new_dictionary[5].append([i])
  return new_dictionary
hurricanes_by_mortality = sort_by_mortality_rating()

# Hurricane with most damage
def max_damage():
  name = "Cuba I"
  cost = 0.0
  for i in hurricanes.values():
    if isinstance(i["Damage"], str):
      continue 
    elif float(i["Damage"]) > cost:
      name = i["Name"]
      cost = i["Damage"]
    else:
      continue
  print("Hurricane {} caused the most damage which cost ${}.".format(name, cost))

max_damage()

# sort hurricanes by damage scale
def sort_by_damage_scale():
  damage_scale = {
    0: 0,
    1: 100000000,
    2: 1000000000,
    3: 10000000000,
    4: 50000000000}
  new_dictionary = {0:[],1:[],2:[],3:[],4:[],5:[]}
  for i in hurricanes.values():
    try:
      current_cost = float(i["Damage"])
      if current_cost <= damage_scale[0]:
        new_dictionary[0].append([i])
      elif current_cost <= damage_scale[1]:
        new_dictionary[1].append([i])
      elif current_cost <= damage_scale[2]:
        new_dictionary[2].append([i])
      elif current_cost <= damage_scale[3]:
        new_dictionary[3].append([i])
      elif current_cost <= damage_scale[4]:
        new_dictionary[4].append([i])
      else:
        new_dictionary[5].append([i])
    except ValueError:
      new_dictionary[0].append([i])
  return new_dictionary

hurricanes_by_damage_scale = sort_by_damage_scale()
print(hurricanes_by_damage_scale)