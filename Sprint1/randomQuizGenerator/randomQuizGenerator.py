import random
capitais = {'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix',
   'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver',
   'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee',
   'Georgia': 'Atlanta', 'Hawaii': 'Honolulu', 'Idaho': 'Boise', 'Illinois':
   'Springfield', 'Indiana': 'Indianapolis', 'Iowa': 'Des Moines', 'Kansas':
   'Topeka', 'Kentucky': 'Frankfort', 'Louisiana': 'Baton Rouge', 'Maine':
   'Augusta', 'Maryland': 'Annapolis', 'Massachusetts': 'Boston', 'Michigan':
   'Lansing', 'Minnesota': 'Saint Paul', 'Mississippi': 'Jackson', 'Missouri':
   'Jefferson City', 'Montana': 'Helena', 'Nebraska': 'Lincoln', 'Nevada':
   'Carson City', 'New Hampshire': 'Concord', 'New Jersey': 'Trenton', 'NewMexico': 'Santa Fe',
    'New York': 'Albany', 'North Carolina': 'Raleigh',
   'North Dakota': 'Bismarck', 'Ohio': 'Columbus', 'Oklahoma': 'Oklahoma City',
   'Oregon': 'Salem', 'Pennsylvania': 'Harrisburg', 'Rhode Island': 'Providence',
   'South Carolina': 'Columbia', 'South Dakota': 'Pierre', 'Tennessee':
   'Nashville', 'Texas': 'Austin', 'Utah': 'Salt Lake City', 'Vermont':
   'Montpelier', 'Virginia': 'Richmond', 'Washington': 'Olympia', 'West Virginia':
   'Charleston', 'Wisconsin': 'Madison', 'Wyoming': 'Cheyenne'}
for quizNum in range(35):
    quizFile = open('quiz_%s.txt' %(quizNum + 1), 'w')
    respostaFile = open('quiz_resposta_%s.txt' %(quizNum + 1), 'w')
    estado = list(capitais.keys())
    random.shuffle(estado)
    for Num in range(50):
        certa = capitais[estado[Num]]
        errada = list(capitais.values())
        del errada[errada.index(certa)]
        errada = random.sample(errada, 3)
        alternativas = errada + [certa]
        random.shuffle(alternativas)
        quizFile.write('%s. Qual a capital de %s?\n' %(Num + 1, estado[Num]))
        for value in range(4):
            quizFile.write('    %s. %s\n\n' %('ABCD'[value], alternativas[value]))
        respostaFile.write('%s. %s\n' %(Num + 1, 'ABCD'[alternativas.index(certa)]))
quizFile.close()
