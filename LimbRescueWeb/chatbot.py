# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer, ListTrainer

# # Creating ChatBot Instance
# chatbot = ChatBot("DoctorBot")

# # Training with Personal Ques & Ans
# conversation = [
#     "Hello",
#     "Hi there!",
#     "How are you doing?",
#     "I'm doing great.",
#     "That is good to hear",
#     "Thank you.",
#     "You're welcome.",
#     "What is lymphedema?",
#     "Lymphedema, or lymphatic obstruction, is a long-term condition where excess fluid collects in tissues causing swelling (edema).",
#     "How should I use the website?",
#     "You can use smartwatches to test you PPG waveform and input the result into the website. We will generate a diagnosis for you.",
# ]

# trainer = ListTrainer(chatbot)
# trainer.train(conversation)

# # Training with English Corpus Data
# trainer_corpus = ChatterBotCorpusTrainer(chatbot)
# trainer_corpus.train("chatterbot.corpus.english")
