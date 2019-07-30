bri = set(['Brazil','Russia','India'])
'India' in bri
'Usa' in bri
bric = bri.copy()
bric.add('China')
bric.issuperset(bri)
bri.remove('Russia')
bri & bric #Or bri.intersection(bric)
