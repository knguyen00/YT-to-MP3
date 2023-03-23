import random

# Define a list of vocabulary words and their definitions
vocab_list = [
    {'word': 'Serendipity', 'definition': 'the occurrence and development of events by chance in a happy or beneficial way.'},
    {'word': 'Quixotic', 'definition': 'exceedingly idealistic; unrealistic and impractical.'},
    {'word': 'Ephemeral', 'definition': 'lasting for a very short time.'},
    {'word': 'Ineffable', 'definition': 'too great or extreme to be expressed or described in words.'},
    {'word': 'Apathy', 'definition': 'lack of interest, enthusiasm, or concern.'},
    {'word': 'Magnanimous', 'definition': 'generous or forgiving, especially towards a rival or less powerful person.'},
    {'word': 'Ubiquitous', 'definition': 'present, appearing, or found everywhere.'},
    {'word': 'Candor', 'definition': 'the quality of being open and honest in expression; frankness.'},
    {'word': 'Discombobulate', 'definition': 'to confuse or disconcert; upset; frustrate.'},
    {'word': 'Sanguine', 'definition': 'optimistic or positive, especially in an apparently bad or difficult situation.'}
]

# Shuffle the list to randomize the order of the words
random.shuffle(vocab_list)

# Loop through the words in the list and prompt the user to study them
for word in vocab_list:
    print("Definition: {}".format(word['definition']))
    user_input = input("What is the word for this definition? ")
    if user_input.lower() == word['word'].lower():
        print("Correct!")
    else:
        print("Incorrect. The correct word is '{}'.".format(word['word']))
