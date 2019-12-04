# using input, converting datatypes, rounding to 2 decimals, etc

print("How many kilometers did you run, run man?")
kms = input()
# miles = float(kms) / 1.6
# miles = round(miles, 2)
miles = round((float(kms) / 1.6), 2)

print(f'Your {kms}km run was {miles}mi.')