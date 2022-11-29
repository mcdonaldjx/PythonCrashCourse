#Created 11/29/2022 by Jared
#Exercise 8-14- Cars: Write a function that stores information about a car in a dictionary. The function should always receive a manufacturer and a model name. It should then accept an arbitary number of keyword arguments. Call the function with the required information and two other name-value pairs, such as a color or an optional feature. Your function should work for a call like this one:
#  car = make_car('subaru', 'outback', color='blue', tow_package=True)
#  Print the dictionary that's returned to make sure all the information was stored correctly.
def make_car(manufacturer, model_name, **car_info):
  car_info['manufacturer']= manufacturer
  car_info['model'] = model_name
  return car_info
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(f"Car 1: {car}")
car_2 = make_car('toyota','camry',color='black',edition='sport')
print(f"Car 2: {car_2}")
car_3 = make_car('dodge','viper',color='red', year=2004)
print(f"Car 3: {car_3}")
