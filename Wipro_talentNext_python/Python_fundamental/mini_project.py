'''project 1'''
distance = float(input('how many miles do you want to travel:'))

if distance <= 3:
    print("ride bicycle")
elif distance < 300:
    print('ride motor cycle ')
else:
    print('drive super car')
    
    
    

'''project 2'''
per_hour = 0.51
per_day = per_hour * 24
per_week = per_day * 7
per_month = per_week * 4
day_for_918 = 918 / per_day
print(f'for per day : {per_day}')
print(f'for per week : {per_week}')
print(f'for per month : {per_month}')
print(f'days with 918 $ is {day_for_918}')
