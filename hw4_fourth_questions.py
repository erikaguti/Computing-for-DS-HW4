###############
# Use the data in covid.csv for this exercise
#
# 10) In a separate file, write a piece of code that
# loads the covid.csv file and prints the list of countries
#  and the total average of death/confirmed among those countries
# for those countries that have more than 500, 1000 and 5000
# active cases respectively.

# filter first, then compute the death/confirmed, then compute the average
# Follow DRY principles in order to complete this exercise.
#
#
# #
import sys

try: 
    import pandas as pd
except:
    print('Pandas not installed. Please install pandas first by running: pip install pandas')
    sys.exit()

path = ''

covid = pd.read_csv(path + 'covid.csv')

covid['Deaths/Confirmed'] = covid.Deaths/covid.Confirmed

for n in [500,1000,5000]:
    print('''total average of death/confirmed for countries with > ''' + str(n) + ''' active cases:
''', covid[covid.Active > n][['Deaths/Confirmed']].mean(),'''
          ''')