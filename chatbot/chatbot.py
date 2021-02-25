from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer, ChatterBotCorpusTrainer

# Creating ChatBot Instance
chatbot = ChatBot(
    'Asesor Virtual',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter',
        'chatterbot.logic.BestMatch',
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'Disculpa no logro comprenderte, sigo aprendiendo.',
            'maximum_similarity_threshold': 0.90
        }
    ],
    database_uri='sqlite:///database.sqlite3'
) 

 # Training with Personal Ques & Ans 
training_data_quesans = open('training_data/ques_ans.txt').read().splitlines()
training_data_personal = open('training_data/personal_ques.txt').read().splitlines()

training_data = training_data_quesans + training_data_personal

trainer = ListTrainer(chatbot)
trainer.train(training_data)  

# Training with inglish Corpus Data 
trainer_corpus = ChatterBotCorpusTrainer(chatbot)
trainer_corpus.train(
    'chatterbot.corpus.spanish'
) 