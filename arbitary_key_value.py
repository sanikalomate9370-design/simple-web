def call_by_value(n):
   return n**2
x=10
print(f"number before call:{x}")
x=call_by_value(x)
print(f"number after call:{x}")