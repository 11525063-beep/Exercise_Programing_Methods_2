torques = [1.2, 5.5, 0.8, 10.2, 4.9, -2.1, 7.0]
safty_list=[]
for i in range (len(torques)):
  if -5<=torques[i]<=5:
    safty_list.append(torques[i])
safty_list.append(0.0)
print(safty_list)