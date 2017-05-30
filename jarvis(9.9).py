#JARVIS mark 12  python 3.5.1 version
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
"""
#Brain functions, vocab!
what_i_should_call_someone = [""]
Good_Things = ["love","sweat","nice","happy","fun","awesome","great"]
Bad_Things = ["death","kill","hurt","harm","discomfort","rape","pain","sad","depression","depressed","angry","mad","broken","raging","rage"]
Static_Greetings = ["hey","hello","hi","hey there","hi there","hello there"]
Sample_questions = ["what is the weather like","where are we today","why did you do that","where is the dog","when are we going to leave","why do you hate me","what is the Answer to question 8","what is a dinosour","what do i do in an hour","why do we have to leave at 6.00", "When is the apointment"]
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
"""

Question_Keyword_Answer = []

Int_Question_Keywords_In_Input = []

possible_question_key_words = ["what's","what","where","when","why","isn't","whats"]
def Analyze():
    def Analyze_for_question():
            def Question_Keyword_Check():
                global possible_question_key_words
                Int_Question_Keywords_In_Input = []
                for words in what_person_said_l_wt:
                    if words in possible_question_key_words:
                        #print (words)
                        #os.system("say '"+words+"'")
                        Int_Question_Keywords_In_Input.append(words)
                for item in Int_Question_Keywords_In_Input:
                    print(item, end=" ")
                print()
                print(len(Int_Question_Keywords_In_Input))
                return Int_Question_Keywords_In_Input
            def Question_Sentence_Match():
                
                #simularity check
                pass








            
            Question_Keyword_Check()            
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
            print (random.choice("what was that?","what","What did you say i didn't hear you"))
        except sr.RequestError as e:
            print("Uh oh! Sorry sir Couldn't request results from Google Speech Recognition service; {0}".format(e))
    except KeyboardInterrupt:
        pass


   
