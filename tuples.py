zoo = ('python','elephant','penguin') #remember the parentetheses are optional

print('The number of animals inzoo is', len(zoo),"\n")

new_zoo = ('monkey','camel',zoo)

print('Number of cages in the new zoo is', len(new_zoo),"\n")
print('All animals in the new zoo are', new_zoo,"\n")
print("Animals brought from new zooo are", new_zoo[2],"\n")
print("Last animal brought form old zoo is",new_zoo[2][2],"\n")
print("Number of the animals in both of the zoos is", len(new_zoo)-1+len(new_zoo[2]))
