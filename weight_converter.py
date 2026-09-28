weight = int(input("Weight:"))
# print(type(weight))

weight_type = input("(L)bs or (K)g: ").lower

if weight_type == "l":
    print(f'Your weight in kg is: [{weight*0.45}]')
else:
    print(f'Your weight in Lbs is: [{weight//0.45}]')
