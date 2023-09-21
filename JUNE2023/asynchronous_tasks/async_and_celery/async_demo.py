import random
import time

import asyncio

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


async def buy_bread():
	# time.sleep(1.2)
	await asyncio.sleep(1.2)
	return random.choice(breads)


async def slice_bread(bread):
	await asyncio.sleep(0.5)
	return f"Sliced {bread} bread"


async def buy_cheese():
	await asyncio.sleep(1.5)
	return random.choice(cheeses)


async def slice_cheese(cheese):
	await asyncio.sleep(0.7)
	return f"Sliced {cheese} cheese"


async def buy_butter():
	await asyncio.sleep(2)
	return 'butter'


async def slice_butter(butter):
	await asyncio.sleep(1.5)
	return 'sliced ' + butter


async def make_sandwich(sliced_cheese, sliced_bread, sliced_butter):
	await asyncio.sleep(1.7)
	return f'{sliced_bread} + {sliced_cheese} + {sliced_butter}'


async def prepare_bread():
	bread = await buy_bread()
	sliced_bread = await slice_bread(bread)
	return sliced_bread


async def prepare_cheese():
	cheese = await buy_cheese()
	sliced_cheese = await slice_cheese(cheese)
	return sliced_cheese


async def prepare_butter():
	butter = await buy_butter()
	sliced_butter = await slice_butter(butter)
	return sliced_butter


async def run_async():
	cheese, bread, butter = await asyncio.gather(
		prepare_cheese(),
		prepare_bread(),
		prepare_butter(),
	)
	sandwich =   make_sandwich(cheese, bread, butter)
	print(sandwich)


async def run():
	start_time = time.time()
	await run_async()
	end_time = time.time()
	print(f"Time elapsed {end_time - start_time} seconds")


asyncio.run(run())
