from collections import defaultdict

somedict = {}
print(somedict[3]) # KeyError

someddict = defaultdict(int)
print(someddict[3333]) # print int(), thus 0




dd_int = defaultdict(int)
dd_lambda = defaultdict(lambda: 0)

print(f"dd_int['foo']: {dd_int['foo']}")
print(f"dd_lambda['bar']: {dd_lambda['bar']}")
