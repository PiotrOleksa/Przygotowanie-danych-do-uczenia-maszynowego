import random
import collections

#------------------------- List Manipulation
#a
fruit_names = ['apple', 'banana', 'pear', 'cherry', 'blackberry']

#b
fruit_names.append('carrot')
fruit_names.append('celery')

#c
random.shuffle(fruit_names)

#e
fruit_names.remove('pear')

#d
veg = []
for i in range(len(fruit_names)):
    if fruit_names[i] == 'celery' or fruit_names[i] == 'carrot':
        veg.append(i)
    else:
        None

first_vegetable = veg[0]

#f
print('List: ', fruit_names, 'First vegetable on position: ', first_vegetable)

#g
sort = sorted(fruit_names)

#h
for x in fruit_names:
    print(x)


#------------------------- Tuples
first_list = ["a" + str(number) for number in range(1, 10)]
second_list = ["b" + str(number) for number in range(1, 10)]

#paired
paired_list = []
for x, y in zip(first_list, second_list):
    paired_list.append([x, y])

#f-string
for i in range(len(paired_list)):
    print(f'Index of {paired_list[i][0]} and {paired_list[i][1]} is  equal {i}')


#------------------------- Sets
fake_names_1 = ['Sherry', 'Mary', 'Matthew', 'Danielle', 'Jeffrey', 'Lauren',
              'Keith', 'Carlos', 'Monique', 'Laura', 'Jared', 'Valerie', 'Juan',
              'Christopher', 'Erica', 'Dawn', 'Joshua', 'Brandon', 'Stephanie']

fake_names_2 = ['Andre', 'Anthony', 'Lauren', 'Douglas', 'Jonathan', 'Richard',
                'Alyssa', 'Vincent', 'Travis', 'Clifford', 'Jerry', 'Justin',
                'Matthew', 'Jared', 'Erica']

#overlap
counter_1 = collections.Counter(fake_names_1)
counter_2 = collections.Counter(fake_names_2)
overlap = list((counter_1 & counter_2).elements())

print(len(overlap))

#union
union = list(set().union(fake_names_1, fake_names_2))
print(union)

#difference
diff = list(set(fake_names_1) - set(fake_names_2))
print(diff)