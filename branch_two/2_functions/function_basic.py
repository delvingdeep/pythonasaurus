
# A function which takes population and land area as argumnets
# and returns population density as output:
def population_density(population, land_area):
    density  = (population/land_area)
    return density

# Here are test cases to verify that function works as expected:
test1 = population_density(10, 1)
expected_result1 = 10
print("expected result: {}, actual result: {}".format(expected_result1, test1))

test2 = population_density(864816, 121.4)
expected_result2 = 7123.6902801
print("expected result: {}..., actual result: {}".format(expected_result2, test2))
