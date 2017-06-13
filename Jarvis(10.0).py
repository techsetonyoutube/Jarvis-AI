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
from difflib import SequenceMatcher
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tokenize import PunktSentenceTokenizer
import speech_recognition as sr
from sys import exit
from time import sleep
import os
import random
r = sr.Recognizer()
m = sr.Microphone()



#Brain functions, vocab!
what_i_should_call_someone = [""]
Good_Things = ["love","sweat","nice","happy","fun","awesome","great"]
Bad_Things = ["death","kill","hurt","harm","discomfort","rape","pain","sad","depression","depressed","angry","mad","broken","raging","rage"]
Static_Greetings = ["hey","hello","hi","hey there","hi there","hello there"]
Name = ["Jarvis","jarvis"]
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


Sample_Questions = ["what is the weather like","where are we today","why did you do that","where is the dog","when are we going to leave","why do you hate me","what is the Answer to question 8","what is a dinosour","what do i do in an hour","why do we have to leave at 6.00", "When is the apointment"]

Question_Keyword_Answer = []

Int_Question_Keywords_In_Input = []

Possible_Question_Key_Words = ["whats","what","where","when","why","isn't","whats","who","should","would","could","can","do","does","can","can","did"]

# In this function: Analyze the user input find out if it's (Question, Answer, Command. Etc) and what is being: Asked, Commanded, ETC.
def Analyze():





    
    #In this function: determin if the input is a question or not.
    def Analyze_for_question():
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
                        print ("Similar to: "+Ran_Question)
                        return True
            # In this function: if the first word of the users input is a question keyword and there is a different question keyword in the input return true.
            def Question_Verb_Noun_Check():
                #if you say "hey jarvis" before somthing like a question or command it will still understand
                try:
                    
                    if what_person_said_l_wt[0] in Static_Greetings or what_person_said_l_wt[0] in Name or what_person_said_l_wt[1] in Name or what_person_said_l_wt[1] in Static_Greetings:
                            print (what_person_said_l_wt[0])
                            return True
                except IndexError:
                    pass
            
            Question_Keyword_Check()                  
            Question_Sentence_Match()
            Question_Verb_Noun_Check()

    Analyze_for_question() 










conversation=True

while conversation==True:

    try:
        print("A moment of silence, please...")
        with m as source: r.adjust_for_ambient_noise(source)
        print("Set minimum energy threshold to {}".format(r.energy_threshold))
 
        print("Say something!")
        with m as source: audio = r.listen(source)
        print("Got it! Now to recognize it...")
        try:
            # recognize speech using Google Speech Recognition
            value = r.recognize_google(audio)

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


   
