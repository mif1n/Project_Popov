# Известны марки машин, выпускаемые в данной стране и экспортируемых в N заданных
# стран. Определить какие марки машин были доставлены во все указанные страны, какие в
# некоторые из стран и какие не доставлены ни в одну страну.


cars = {'bmv', 'merc', 'lada', 'vaz', 'opel', 'zig', 'tesla'}

spain = {'bmv', 'lada', 'vaz'}
gonduras = {'merc', 'vaz', 'opel'}
usa = {'zig', 'vaz'}
print ('завезены во все страны: ', spain & gonduras & usa)
c = spain | gonduras | usa
print ('некоторые из стран: ', c)
b = spain | gonduras | usa
print('не входят:', cars - b)