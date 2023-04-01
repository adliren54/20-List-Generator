print("List Generator")

start = int(input("Start at: "))
stop = int(input("End before: "))
increment = int(input("Increment between values: "))

for i in range(start, stop, increment):
  print(i)