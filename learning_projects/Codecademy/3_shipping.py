# Platform: Codecademy 
# Course: Learn Python 3
# Author: Berea Robinson
# Date: 2023-11-29
# Objective: Shipping prices
# Description: Program dislays shipping prices based on 
# shipping rates. Weight is the changing variable.


weight = 41.5
premium = 125

# Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.5 + 20
elif weight <= 6:
  cost_ground = weight * 3 + 20
elif weight <= 10:
  cost_ground = weight * 4 + 20
else:
  cost_ground = weight * 4.75 + 20

# Drone Shipping
if weight <= 2: 
  cost_fly = weight * 4.5 + 0
elif weight <= 6:
  cost_fly = weight * 9 + 0
elif weight <= 10:
  cost_fly = weight * 12 + 0
else:
  cost_fly = weight * 14.25 + 0

print("Ground Shipping $",f"{cost_ground:.2f}")
print("Ground Shipping Premium $",f"{premium:.2f}")
print("Drone Shipping $",f"{cost_fly:.2f}")