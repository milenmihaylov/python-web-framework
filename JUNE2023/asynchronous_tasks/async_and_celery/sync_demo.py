import random
import time

breads = [
	'white',
	'whole',
	'banana',
]

cheeses = [
	'bulgarian',
	'feta',
	'blue',
]


def buy_bread():
	time.sleep(1.2)
	return random.choice(breads)


def slice_bread(bread):
	time.sleep(0.5)
	return f"Sliced {bread} bread"


def buy_cheese():
	time.sleep(1.5)
	return random.choice(cheeses)


def slice_cheese(cheese):
	time.sleep(0.7)
	return f"Sliced {cheese} cheese"


def buy_butter():
	time.sleep(2)
	return 'butter'


def slice_butter(butter):
	time.sleep(1.5)
	return 'sliced ' + butter


def make_sandwich(sliced_cheese, sliced_bread, sliced_butter):
	time.sleep(1.7)
	return f'{sliced_bread} + {sliced_cheese} + {sliced_butter}'


def run_sync():
	bread = buy_bread()
	slice_bread(bread)
	cheese = buy_cheese()
	slice_cheese(cheese)
	butter = buy_butter()
	slice_butter(butter)
	sandwich = make_sandwich(cheese, bread, butter)
	print(sandwich)


def run():
	start_time = time.time()
	run_sync()
	end_time = time.time()
	print(f"Time elapsed {end_time - start_time} seconds")


run()
