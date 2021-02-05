import utils
import pickle
import time

with open(f'{utils.get_project_root()}/src/lyrics_model.pickle', 'rb') as file:
    predictor = pickle.load(file)

print('Model successfully loaded!')
time.sleep(1)
print('I really know a lot of artists....\nI\'ve heard of Steely Dan')
time.sleep(2)
print('The Clash')
time.sleep(2)
print('Destroyer')
time.sleep(2)
print('aaaand that\'s about it...')



lyrics = input('Now let\'s start.. Give me some lyrics. Also, you can just leave by pressing \'x\': ')
while lyrics != 'x':
    try:
        answer = predictor.predict([lyrics])
        print(f'Oh this is easy. It is {answer[0].capitalize()}, why do you even bother wasting my time?\n')
        lyrics = input('Go, shoot me some difficult lyrics, please: ')
        if lyrics == 'x':
            print('OK THEN GET OFF! AND I REALLY KNOW THE OTHERS! I SWEAR! BYE!')
        if lyrics == 'should i stay or should i go?':
            print('\nHonestly I think you should go now...')
            time.sleep(2)
            print('Yes, you should go.')
            time.sleep(2)
    except KeyboardInterrupt:
        print('\n\nHaha\nI told you how can get out of here. This cheap trick wont work on me!')

