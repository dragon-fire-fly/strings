
>>> test = "DCI is {}"
>>> test.format("just awesome man")
'DCI is just awesome man'
>>> test
'DCI is {}'
>>> test.replace("DCI", "McDonalds")
'McDonalds is {}'
>>> test
'DCI is {}'
>>> test = "Something {} and something {} and something {}"
>>> test.format("cool", "wonderful", "awesome")
'Something cool and something wonderful and something awesome'



>>> str_test = "{2}. {1} ({0})"
>>> str_test.format("Team", "Player", 1)
'1. Player (Team)'


test = "{0} and {1} and {3} and {2}"
>>> test.format("Apple", "Peach", "Carrot", "Pumpkin")
'Apple and Peach and Pumpkin and Carrot'

>>> test = "{Continent} - {Country} - {City}"
>>> test.format(Continent="Europe", Country="Germany", City="The best city Berlin")
'Europe - Germany - The best city Berlin'
