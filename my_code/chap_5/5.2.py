questions = [
    "We don't serve strings around here. Are you a string?",
    "What is said on Father's Day in the forest?",
    "What makes the sound 'Sis! Boom! Bah!'?"
]
answers = [
    "An exploding sheep.",
    "No, I'm a frayed knot.",
    "'Pop!' goes the weasel."
]

print(f'Q: {questions[0]} \nA: {answers[1]}') #python 3.6 f-string
print('Q: %s \nA: %s' % (questions[1],answers[2])) #python 2 style
print('Q: {} \nA: {}'.format(questions[2],answers[0])) #python 3 style

