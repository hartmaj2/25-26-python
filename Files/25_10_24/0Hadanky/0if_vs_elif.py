### Co vyíše tento program?
print("Narazila na tebe banda Robina Hooda. Bohatým berou a chudým dávají.")
print("Stiskni enter pro pokračování...")
input()

x = 20
if x < 30:
    print("Ty nejsi moc bohatej. Něco málo ti dáme.")
    x = x + 10
if x >= 30:
    print("Ty jsi docela prachatej, tak tě oberem!")
    x = x - 30
if x == 0:
    print("Ty nemáš dokonce žádný prachy, tak to ti pomůžeme!")
    x = x + 20