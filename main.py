def calc(inp: int):
  a = sum([i for i in range(1, inp+1)])
  return a

a = calc(int(input()))
print("\r{0}".format(a))