# Some helper functions for Part 5
from collections import namedtuple
from hw3 import *
from random import randint

# compute the manhattan distance between two points a and b (represented as pairs)
def dist(a,b):
	x_dist = a[0] - b[0] if a[0] > b[0] else b[0] - a[0]
	y_dist = a[1] - b[1] if a[1] > b[1] else b[1] - a[1]
	return x_dist + y_dist

# Give a representation for riders/ drivers somewhere which can be included in your graph used in stable_outcome

# Given a (bipartite) graph G with edge values specified by v, 
# output a stable outcome (M,a) consisting of a matching and allocations
def stable_outcome(G,v):
	M = None
	a = None
	return (M,a)


Location = namedtuple("x", "y")
# curr_loc, end_loc are both Locations
Rider = namedtuple("Rider", ["name", "curr_loc", "end_loc", "val"])
Driver = namedtuple("Driver", ["name", "curr_loc"])

# Rider list contains riders. Driver list contains... drivers!
# i in both of the previous refers to their identifier
# n is size of grid
def generate_values(rider_list, driver_list):
	matchable_riders = []
	unmatchable_riders = []
	tot_temps = []
	for rider in rider_list:
		temp_list = []
		for driver in driver_list:
			temp_list.append(rider.val - (dist(driver.curr_loc, rider.curr_loc) + dist(rider.curr_loc, rider.end_loc)))
		if sum(1 for i in temp_list if i < 0) == len(temp_list):
			unmatchable_riders.append(rider.name)
		else:
			matchable_riders.append(rider)

	while True:
		rider_names = {i: rider.name for rider, i in zip(matchable_riders, range(len(matchable_riders)))}
		driver_names = {i: driver.name for driver, i in zip(driver_list, range(len(driver_list)))}
		temp_matchable = matchable_riders[:]
		temp_driver = driver_list[:]
		if len(matchable_riders) > len(driver_list):
			larger_tot = len(matchable_riders)
			for i in range(larger_tot - len(driver_list)):
				temp_driver.append(-1)
		else:
			larger_tot = len(driver_list)
			for i in range(larger_tot - len(matchable_riders)):
				temp_matchable.append(-1)
		values = [[0]*larger_tot for i in range(larger_tot)]
		rider_idx = 0
		for rider in temp_matchable:
			driver_idx = 0
			for driver in temp_driver:
				if driver == -1 or rider == -1:
					values[rider_idx][driver_idx] = 0
				else:
					total_dist = dist(driver.curr_loc, rider.curr_loc) + dist(rider.curr_loc, rider.end_loc)
					values[rider_idx][driver_idx] = rider.val - total_dist
				driver_idx += 1
			rider_idx += 1
		t = market_eq(larger_tot, values)
		if t[0]:
			break
		unmatchable_riders.append(rider_names[t[1]])
		matchable_riders.pop(t[1])


	pairings = []
	for i in range(len(rider_names)):
		if t[2][i] in driver_names:
			pairings.append((rider_names[i], driver_names[t[2][i]], t[1][i]))
		else:
			unmatchable_riders.append(rider_names[i])

	matched_drivers = [i[1] for i in pairings]
	unmatchable_drivers = []
	for driver in driver_list:
		if driver.name not in matched_drivers:
			unmatchable_drivers.append(driver.name)
	print("Unmatchable riders: {}".format(unmatchable_riders))
	print("Unmatchable drivers: {}".format(unmatchable_drivers))
	print("Matchings:{}".format(pairings))
	return t


def test_1():
	r_1 = Rider("a", curr_loc=(0,0), end_loc=(5,2), val=15)
	r_2 = Rider("b", curr_loc = (0,1), end_loc = (0,2), val=10)
	r_3 = Rider("c", curr_loc = (3,4), end_loc = (5,1), val=18)
	r_4 = Rider("d", curr_loc = (9,8), end_loc = (8,1), val=20)
	r_5 = Rider("e", curr_loc = (6,3), end_loc = (3,0), val=4)
	d_1 = Driver("f", curr_loc=(1,1))
	d_2 = Driver("g", curr_loc=(4,2))
	d_3 = Driver("h", curr_loc=(4,9))
	d_4 = Driver("i", curr_loc=(8,5))
	d_5 = Driver("j", curr_loc=(5,5))
	d_6 = Driver("k", curr_loc=(2,1))

	generate_values([r_1, r_2, r_3, r_4, r_5], [d_1, d_2, d_3, d_4, d_5, d_6])

def test_2():
	r_1 = Rider("joe", curr_loc=(1,3), end_loc=(4,2), val=15)
	r_2 = Rider("tom", curr_loc = (3,5), end_loc = (2,5), val=10)
	r_3 = Rider("jane", curr_loc = (4,9), end_loc = (8,2), val=24)
	r_4 = Rider("jess", curr_loc = (4,8), end_loc = (8,1), val=22)
	r_5 = Rider("t", curr_loc = (5,6), end_loc = (6,5), val=18)
	d_1 = Driver("a", curr_loc=(3,1))
	d_2 = Driver("b", curr_loc=(4,4))
	d_3 = Driver("c", curr_loc=(9,5))
	d_4 = Driver("d", curr_loc=(9,3))
	d_5 = Driver("e", curr_loc=(3,3))

	generate_values([r_1, r_2, r_3, r_4, r_5], [d_1, d_2, d_3, d_4, d_5])

def gen_random(r, d):
	riders = [Rider(name=i, curr_loc=(randint(0,100), randint(0,100)), end_loc=(randint(0,100), randint(0,100)), val=100) for i in range(r)]
	drivers = [Driver(name=i, curr_loc=(randint(0,100), randint(0,100))) for i in range(d)]
	generate_values(riders, drivers)

test_1()
test_2()

for r, d in zip([10, 20, 5], [10, 5, 20]):
	print("Doing {} riders, {} drivers".format(r, d))
	for i in range(100):
		gen_random(r, d)
	print("-"*30)

