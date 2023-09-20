#MASHQLAR
#1-mashq
#countries = ['France', 'Spain', 'Portugal', 'USA', 'Uzbekistan', 'Australia']
#print(countries)
#print(len(countries))


#2-mashq
#print(sorted(countries))
#print(sorted(countries, reverse=True))
#print(countries)


#3-mashq
#countries.reverse()
#print(countries)


#4-mashq
#countries.sort()
#print(countries)
#countries.sort(reverse=True)
#rint(countries)


#5-mashq
#numbers = list(range(120,1200,2))
#print(numbers)
#print(sum(numbers))
#print(max(numbers)-min(numbers))
#print(len(numbers))

#cut_Start = numbers[:20]
#cut_center = numbers[270:290]
#cut_End = numbers[520:]
#print(cut_Start)
#print(cut_center)
#print(cut_End)


#6-mashq
taomlar = ['osh', 'manti', 'somsa', 'sho\'rva', 'jiz']
nonushta = taomlar[:]

nonushta = taomlar[2:4]
nonushta.append('bifshteks')
nonushta.append('beshbarmoq')
#print(nonushta)
#print(taomlar)


nonushta = tuple(nonushta)
print(nonushta)
nonushta[0] = 'qaymoq va non'
print(nonushta)

