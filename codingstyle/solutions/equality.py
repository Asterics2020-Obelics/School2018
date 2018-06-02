attr = 1
# Just check the value
if attr:
    print('attr is truthy!')
    
# or check for the opposite
if not attr:
    print('attr is falsey!')

# or, since None is considered false, explicitly check for it
if attr is None:
    print('attr is None!')
