doors = ["0", "x", "0"]
guess = int(input("Choose door 1,2 or 3:"))

if doors[guess-1] == "x":
    print(":)")
else:
    print(":(")

