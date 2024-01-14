for a in range(1,1000):
  for b in range(1,1000):
    if a<b:
      c = 1000-a-b
      if a + b + c == 1000 and (a**2) + (b**2) == (c**2):
        print(f'This is product of abc: {a*b*c}, {a},{b},{c}')