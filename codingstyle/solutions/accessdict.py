d = {'hello': 'world'}

print(d.get('hello', 'default_value')) 
print(d.get('thingy', 'default_value'))

# Or:
if 'hello' in d:
    print(d['hello'])