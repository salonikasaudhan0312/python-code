color = input("enter a color: ")
match color:
  case "red":
    print("stop")
  case "yellow":
    print("looks")
  case "green":
    print("go")
  case _:
    print("invalid color")