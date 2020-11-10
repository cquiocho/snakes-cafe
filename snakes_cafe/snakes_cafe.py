print("*" * 36)
print("**  Welcome to the Snakes Cafe!   **\n**  Please see our menu below.    **\n**\n**To quit at any time, type \"quit\"**")
print("*" * 36)
print("\n")
print("Appetizers\n-----\nWings\nSpring Rolls\n")
print("\nEntrees\n-----\nSalmon\nSteak\nMeat Tornado\nA Literal Garden\n")
print("\nDesserts\n-----\nIce Cream\nCake\nPie\nCookies\n")
print("*" * 36)
print("**  What would you like to order? **")
print("*" * 36)

response = input("> ")
i = 0
order = {

}

while response != quit:
  if response in order:
    order[response] += 1
  else:
    order[response] = 1

  if order[response] > 1:
    reply = f"** {order[response]} orders of {response} have been added to your meal **"
    print(reply)
    response = input("> ")
  else:
    reply = f"** {order[response]} order of {response} has been added to your meal **"
    print(reply)
  response = input("> ")
