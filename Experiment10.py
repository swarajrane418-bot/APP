
import numpy as np


heart_rate = np.random.randint(80,151,10)


print("heart rate for 10 minutes:")
print(heart_rate)


first_5_minutes = heart_rate[:5]


print("\nheart rates during first 5 minutes:")
print(first_5_minutes)


maximum = np.max(heart_rate)


minimum = np.min(heart_rate)


average = np.mean(heart_rate)


print("\nmaximum heart rate :",maximum,"BPM")
print("\nminimum heart rate :",minimum,"BPM")
print("average heart rate:",round(average,2),"BPM")


high_rate = heart_rate >120


print("\nheart rate exceeding 120 BPM:")
print(heart_rate[high_rate])


minutes = np.where (heart_rate >120)[0]+1


print("\nminutes where heart rate exceeded 120 BPM:")
print(minutes)