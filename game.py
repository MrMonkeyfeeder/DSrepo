import numpy as np

number = np.random.randint(1, 101)
count = 0

while True:
    count += 1
    predict_number = int(input('Predict the number!'))
    
    if predict_number < number:
        print('The number is greater!')
    elif predict_number > number:
        print('The number is less!')
    else:
        print(f'You found it! The number was {number} and you did it by {count} steps.')
        break