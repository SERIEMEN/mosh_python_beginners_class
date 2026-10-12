# You can directly convert to an integer from the output
weight = input('How much do you weigh without the unit? ')
unit = input('(L)bs or (KG): ')

if unit.upper() == 'KG':
    conv_weight = float(weight) / 0.45
    print(f'You are {conv_weight} pounds')
else:
    convert_weight = float(weight) * 0.45
    print(f'You are {convert_weight} kg')