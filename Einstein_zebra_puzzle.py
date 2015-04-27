
# Einstein's Riddle
# Solve zebra puzzle

# There are five houses.
# Each house has its own unique color.
# All house owners are of different nationalities.
# They all have different pets.
# They all drink different drinks.
# They all smoke different cigarettes.
# The English man lives in the red house.
# The Swede has a dog.
# The Dane drinks tea.
# The green house is on the left side of the white house.
# They drink coffee in the green house.
# The man who smokes Pall Mall has birds.
# In the yellow house they smoke Dunhill.
# In the middle house they drink milk.
# The Norwegian lives in the first house.
# The man who smokes Blend lives in the house next to the house with cats.
# In the house next to the house where they have a horse, they smoke Dunhill.
# The man who smokes Blue Master drinks beer.
# The German smokes Prince.
# The Norwegian lives next to the blue house.
# They drink water in the house next to the house where they smoke Blend.
# ...who owns the Zebra?

from itertools import permutations
import time
from random import shuffle

start_time = time.time()

num = range(1,6)
colors_list = ['yellow', 'blue', 'red', 'green', 'white']
country_list = ['Norwegian', 'Dane', 'English', 'German', 'Swede']
pets_list = ['cats', 'horse', 'birds', 'zebra', 'dog']
drinks_list = ['water', 'tea', 'milk', 'coffee', 'beer']
cigarettes_list = ['Dunhill', 'Blend', 'Pall Mall', 'Prince', 'Blue Master'] 

colors = {colors_list[i] : i for i in range(5) }
country = {country_list[i] : i for i in range(5) }
pets = {pets_list[i] : i for i in range(5) }
drinks = {drinks_list[i] : i for i in range(5) }
cigarettes = {cigarettes_list[i] : i for i in range(5) }


init_state = {'colors': colors,'country': country, 'pets':pets,
'drinks': drinks, 'cigarettes': cigarettes}


def check_condition(state):
	"""
	check the Einstein riddle problem condition 
	"""
	# The English man lives in the red house.
	if state['country']['English'] != state['colors']['red']:
		# print 'The English man lives in the red house.'
		return False
	# The Swede has a dog.
	elif state['country']['Swede'] != state['pets']['dog']:
		# print 'The Swede has a dog.'
		return False
	# The Dane drinks tea
	elif state['country']['Dane'] != state['drinks']['tea']:
		# print 'The Dane drinks tea'
		return False
	# The green house is on the left side of the white house
	elif state['colors']['green'] > state['colors']['white']:
		# print 'The green house is on the left side of the white house'
		return False
	# They drink coffee in the green house
	elif state['drinks']['coffee'] != state['colors']['green']:
		# print 'They drink coffee in the green house'
		return False
	# The man who smokes Pall Mall has birds
	elif state['cigarettes']['Pall Mall'] != state['pets']['birds']:
		# print 'The man who smokes Pall Mall has birds'
		return False
	# In the yellow house they smoke Dunhill
	elif state['colors']['yellow'] != state['cigarettes']['Dunhill']:
		# print 'In the yellow house they smoke Dunhill'
		return False
	# In the middle house they drink milk
	elif state['drinks']['milk'] != 2:
		# print 'In the middle house they drink milk'
		return False
	# The Norwegian lives in the first house
	elif state['country']['Norwegian'] != 0:
		# print 'The Norwegian lives in the first house'
		return False
	# The man who smokes Blend lives in the house next to the house with cats
	elif abs(state['cigarettes']['Blend'] - state['pets']['cats']) != 1:
		# print 'The man who smokes Blend lives in the house next to the house with cats'
		return False
	# In the house next to the house where they have a horse, they smoke Dunhill
	elif abs(state['pets']['horse'] - state['cigarettes']['Dunhill']) != 1:
		# print  'In the house next to the house where they have a horse, they smoke Dunhill'
		return False
	# The man who smoke Blue Master drinks beer
	elif state['cigarettes']['Blue Master'] != state['drinks']['beer']:
		# print  'The man who smoke Blue Master drinks beer'
		return False
	# The German smokes Prince
	elif state['cigarettes']['Prince'] != state['country']['German']:
		# print  'The German smokes Prince'
		return False
	# The Norwegian lives next to the blue house
	elif abs(state['country']['Norwegian'] - state ['colors']['blue']) != 1:
		# print 'The Norwegian lives next to the blue house'
		return False
	# They drink water in the house next to the house where they smoke Blend
	elif abs(state['drinks']['water'] - state['cigarettes']['Blend']) != 1:
		# print 'They drink water in the house next to the house where they smoke Blend'
		return False
	return True



# Test
print init_state
print check_condition(init_state)
if check_condition(init_state):
	print init_state

shuffle(colors_list)
shuffle(country_list)
shuffle(drinks_list)
shuffle(cigarettes_list)
shuffle(pets_list)

counter = 0
def loop_over():
# Loop over all the possible outcomes : 120^5 = 24883200000 outcomes
	all_outcomes = list(permutations(range(5)))
	counter = 0
	for color in all_outcomes:
		for count in all_outcomes:
			for pet in all_outcomes:
				for drink in all_outcomes:
					for cigar in all_outcomes:
						counter += 1
						# print counter
						colors = {colors_list[i] : i for i in color }
						country = {country_list[i] : i for i in count }
						pets = {pets_list[i] : i for i in pet }
						drinks = {drinks_list[i] : i for i in drink }
						cigarettes = {cigarettes_list[i] : i for i in cigar }
						state = {'colors': colors,'country': country, 'pets':pets,
						'drinks': drinks, 'cigarettes': cigarettes}
						if check_condition(state):
							print 'iterate over %d outcomes'%(counter)
							# print state
							return state
	return None

s = loop_over()
print s
elapsed_time = time.time() - start_time
print 'elapsed_time is %f'%(elapsed_time)