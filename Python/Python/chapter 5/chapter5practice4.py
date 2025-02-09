"""what will be the length of following set
s=set()
s.add(20)
s.add(20.0)
s.add("20")
"""
s=set()
s.add(20)
s.add(20.0)
s.add("20")
print(len(s))
#its return 2 cause 20==20.0 and set is count only unic numbers