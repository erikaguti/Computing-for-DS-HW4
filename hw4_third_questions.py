# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far in that country

def Total_registered_cases(data,country):
    keys = data.keys()
    for k in keys:
        if country in keys:
            cases=0
            for d in data[country]:
                cases = cases+d
            return cases
        else:
            return 0
        
#8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had

def total_registered_cases_per_country(data):
    my_dict = {}
    for country in data.keys():
        cases = 0
        for d in data[country]:
            cases = cases+d
        my_dict[country] = cases
    return my_dict

# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases

def country_with_most_cases(data):
    for country in data.keys():
        cases = 0
        for d in data[country]:
            cases = cases+d
        if list(data).index(country) == 0:
            max_=cases
            max_name = country
        else:
            if cases>max_:
                max_=cases
                max_name = country
    return max_name
