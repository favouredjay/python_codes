print('{} {}'.format('Joy', 'udom'))
print('{0} {0} {1} {1}'.format('Joy', 'udom'))
print('{last} {first} {first} {last}'.format(first='Joy', last='Udom'))
print('{:c}\n{:c}\n{:c}'.format(45, 20, 30))
print('[{0:>10}]\n[{0:^10}]\n[{0:<10}]\n'.format('Joy'))

name = 'Joy '
name += 'Udom'
bar = '*'
bar *= len(name)
print(f'{bar}\n{name} \n{bar}')

user_name = '    Joy Udom'
print(user_name.lstrip())

word = "this is python"

print(word.title())