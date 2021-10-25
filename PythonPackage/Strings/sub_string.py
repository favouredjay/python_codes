sentence = 'grateful for life and for good health'
print(sentence.rfind('for'))

for i in sentence.split():
    if i.endswith('e'):
        print(i,  end = " ")
        print()


print('1 2 3 4 5'.replace(' ', '-->', 1))

print('www.wahala.movies.com'.replace('.', '%20'))
