from utils import cache


@cache()
def square(x):
  print 'Caculating ...'
  return x * x

print square(2)
print square(3)
print square(10)
print square(2)
