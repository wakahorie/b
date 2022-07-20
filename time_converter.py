time = int(input("type in your time"))
choice = int(input("is your time in 1)hours or 2)minutes?"))

if choice == 1:
  finalTime = time * 60

elif choice == 2:
  finalTime = time / 60

else:
  print("please insert number 1 or 2")

print(finalTime)
