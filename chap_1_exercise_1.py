def C_to_F (Celcius):
  return (Celcius*1.8)+32
vol = 5.5
cel = 30
print(f"Voltage: {vol}V\nTemperature: {cel}C ({C_to_F(cel)}F)")
if 3<=vol<=7 and 25<=cel<=32:
  print("The system is safe.")
else:print("warning!!! Turn it off")