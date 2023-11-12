# Dictionary

keys = ['Salman', 'John', 'Prime']
values = ['Python', 'Java', 'golang']
data = dict(zip(keys, values))
print(data)

print(data['Salman'])
data['captain'] = 'java script'
print(data)

del data['John']
print(data)

prog = {'JS': 'Atom', 'C#': 'VS', 'Python':['Pycharm', 'Sublime'], 'Java': {'Java SE': 'Netbeans', 'Java EE':'Eclipse'}}
print(prog)
print(prog['C#'])
print(prog['Python'])
print(prog['Python'][0])
print(prog['Java'])
print(prog['Java']['Java EE'])
