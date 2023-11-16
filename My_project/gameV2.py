import numpy as np

def random_predict(number:int=1) -> int:
    """Predicting game for computer.

    Args:
        number (int, optional): Hidden word. Defaults to 1.

    Returns:
        int: Guess count
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
    return count
# print(f'Number of tries: {random_predict()}')

def score_game(random_predict) -> int:
    """Mean number of tries per 1000 when computer guess.

    Args:
        random_predict (_type_): Predicting function

    Returns:
        int: guess count per 1000
    """
    count_lst = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size=(1000))
    for number in random_array:
        count_lst.append(random_predict(number))
        
    score = int(np.mean(count_lst))
    print(f'Your algorythm predict the number mean at {score} times!')
    return (score)

if __name__ == '__main__':
    score_game(random_predict)