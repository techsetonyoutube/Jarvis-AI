#JARVIS mark 10. python 3.5.1 version
#JUST.A.RATHER.VERY.INTELEGENT.SYSTEM.
##import speech_recognition
##import datetime
##import os
##import random
##import datetime
##import webbrowser
##import time
##import calendar

print(
"""
-----------------------------------------------------------------------
|        __    ______    ______   __           __  _      _____       |       
|       |  |  |  __  |  |  __  \  \ \         / / | |    / ____]      |
|       |  |  | |__| |  | |  | |   \ \       / /  | |   / /           |
|       |  |  |  __  |  | '--'_/    \ \     / /   | |   \ \____       |
|  _    |  |  | |  | |  |  _  \      \ \   / /    | |    \___  \      |
| | |___|  |  | |  | |  | | \  \      \ \_/ /     | |    ____}  |     |
|  \_______/  |_|  |_|  |_|  \__\      \___/      |_|    \_____/      |     
|                                                                     |
-----------------------------------------------------------------------
""")

from difflib import SequenceMatcher
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import PunktSentenceTokenizer
import speech_recognition as sr
import sys
from time import sleep
import os
import random
r = sr.Recognizer()
m = sr.Microphone()
m2 = sr.Microphone(device_index=2)



#Brain functions, vocab!
what_i_should_call_someone = [""]
Good_Things = ["love","sweet","nice","happy","fun","awesome","great"]
Bad_Things = ["death","kill","hurt","harm","discomfort","rape","pain","sad","depression","depressed","angry","mad","broken","raging","rage"]
# Words that you might says in the beginning of your input, for example: "um hey where are we!?!"
Slang_Words = ["um","uh","hm","eh"]
# Put all greetings in here
Static_Greetings = ["Hey","Hi","Hello"]
# Put your AIs Name and other names just in case.
Name = ["jarvis"]
posible_answer_key_words = ["becuase","yes","no"]
Chance_that_question_was_asked_1 = 0
Chance_that_question_was_asked_2 = 0
certainty_question_was_asked = 0
Me_statment_keywords = ["you","your","yours"]
You_statment_keywords = ["i","i'm","me"]
global certainty_person_is_talking_to_me
what_i_said = ("")
Just_asked_querstion = False
the_last_thing_i_said = ("")
the_last_thing_person_said = ("")
what_person_said = ("")
what_person_said_means = [""]
what_im_about_to_say = [""]
why_im_about_to_say_it = [""]
who_im_talking_to = [""]
how_i_feel = [""]
why_do_i_feel_the_way_i_do = [""]
what_i_am_thinking = ("")
# ways to describe the nouns last said
it_pronouns = ["it","they","she","he"]
# last person place or thing described spoken or descussed!
last_nouns = [""]

# Sample of random questions so Jarvis has somthing to index to know what a question is!
Sample_Questions = ["what is the weather like","where are we today","why did you do that","where is the dog","when are we going to leave","why do you hate me","what is the Answer to question 8",
                    "what is a dinosour","what do i do in an hour","why do we have to leave at 6.00", "When is the apointment","where did you go","why did you do that","how did he win","why won’t you help me",
                    "when did he find you","how do you get it","who does all the shipping","where do you buy stuff","why don’t you just find it in the target","why don't you buy stuff at target","where did you say it was",
                    "when did he grab the phone","what happened at seven am","did you take my phone","do you like me","do you know what happened yesterday","did it break when it dropped","does it hurt everyday",
                    "does the car break down often","can you drive me home","where did you find me"
                    "can it fly from here to target","could you find it for me"]

Sample_Greetings = ["hey","hello","hi","hey there","hi there","hello there","hey jarvis","hey dude"]

Question_Keyword_Answer = []

Int_Question_Keywords_In_Input = []

Possible_Question_Key_Words = ["whats","what","where","when","why","isn't","whats","who","should","would","could","can","do","does","can","can","did"]

Possible_Greeting_Key_Words = ["hey","hi","hello",Name]

# In this function: Analyze the user input find out if it's (Question, Answer, Command. Etc) and what is being: Asked, Commanded, ETC.
def Analyze():


    def Analyze_For_Greeting():
       
        def Greeting_Keyword_Check():
                global Possible_Greeting_Key_Words
                Int_Greeting_Keywords_In_Input = []
                for words in what_person_said_l_wt:
                    if words in Possible_Greeting_Key_Words:
                        Int_Greeting_Keywords_In_Input.append(words)
                Amount_Greeting_Keywords = (len(Int_Greeting_Keywords_In_Input))
                if Amount_Greeting_Keywords > 0:
                    return True
        def Greeting_Sentence_Match():
             
                for Ran_Greeting in Sample_Greetings:
                    Greeting_Matcher = SequenceMatcher(None, Ran_Greeting, what_person_said_l).ratio()
                    if Greeting_Matcher > 0.5:
                        print (Greeting_Matcher)
                        print ("Similar to Greeting: "+Ran_Greeting)
                        return True


        
        Greeting_Keyword_Check()
        Greeting_Sentence_Match()
    
    #In this function: determin if the input is a question or not.
    def Analyze_For_Question():
            # In this function: if there is atleast one question keyword in the user input then return true.
            def Question_Keyword_Check():
                global Possible_Question_Key_Words
                Int_Question_Keywords_In_Input = []
                for words in what_person_said_l_wt:
                    if words in Possible_Question_Key_Words:
                        Int_Question_Keywords_In_Input.append(words)
                Amount_Question_keywords = (len(Int_Question_Keywords_In_Input))
                if Amount_Question_keywords > 0:
                    return True
            # In this function: if the users input is simular to other sample questions, return true.
            def Question_Sentence_Match():
                for Ran_Question in Sample_Questions:
                    Question_Matcher = SequenceMatcher(None, Ran_Question, what_person_said_l).ratio()
                    if Question_Matcher > 0.5:
                        print (Question_Matcher)
                        print ("Similar to Question: "+Ran_Question)
                        return True
            # In this function: if the first word of the users input is a question keyword and there is a different question keyword in the input return true.
            def Question_Verb_Noun_Check():
                #if you say "hey jarvis" before somthing like a question or command it will still understand
                try:
                    for word in what_person_said_l_wt:
                        if word in Static_Greetings or word in Name:
                                print (word)
                                Minus_Begin_Greet1 = what_person_said_l_wt.remove(word)
                                print (Minus_Begin_Greet1)
                                return True 
                except IndexError:
                    pass

            Question_Keyword_Check()                  
            Question_Sentence_Match()
            Question_Verb_Noun_Check()
            if Question_Keyword_Check()==True and Question_Sentence_Match()==True and Question_Verb_Noun_Check()==True:
                return True
            else:
                return False                


            
    # All the funtions in Analyze
    Analyze_For_Greeting()
    Analyze_For_Question() 

    if Analyze_For_Question()==True:
        print ("This was a Question")
    









Conversation=True
Conversation_Started=False

while Conversation==True:

    try:
        if Conversation_Started==False:
            #Greeting()
            Conversation_Started=True
            
        with m2 as source: r.adjust_for_ambient_noise(source)
        print(format(r.energy_threshold))
 
        print("Say something!") # just here for now and testing porposes so we know whats happening
        with m2 as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)
            #other choices of API for STT \/
            """
            value = r.recognize_bing(audio, Key=BING_KEY)
            value = r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)
            vaule = r.recognize_ibm(audio, username=IBM_USERNAME, password=IBM_PASSWORD)
            value = r.recognize_wit(audio, key=WIT_AI_KEY)
            value = r.recognize_google_cloud(audio, credentials_json=GOOGLE_CLOUD_SPEECH_CREDENTIALS)
            value = r.recognize_sphinx(audio)
            """
            # we need some special handling here to correctly print unicode characters to standard output
            if str is bytes:  # this version of Python uses bytes for strings (Python 2)
                print(u"You said {}".format(value).encode("utf-8"))
            else:  # this version of Python uses unicode for strings (Python 3+)
                print("You said {}".format(value))
                          
            what_person_said_l = value.lower()
            what_person_said_l_wt = word_tokenize(what_person_said_l)
            Analyze()
            
 
        except sr.UnknownValueError:
            print ("what was that?")
        except sr.RequestError as e:
            print("Uh oh! Sorry sir Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass   
        
