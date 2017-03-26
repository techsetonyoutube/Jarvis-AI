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
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
what_i_should_call_someone = [""]


#simply vocab/small talk




static_greetings = ["hey","hello","hi"]

possible_question_key_words = ["what's","what","where","when","why","is this","isn't this","is that","isn't that"]

certainty_question_was_asked = 0

me_statment = ["you","your","yours"]


#Brain function!
certainty_person_is_talking_to_me = 0

The_last_thing_person_said = ("")

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




while "conversation":
    


    
    what_person_said = input()

    
    what_person_said_p1 = word_tokenize(what_person_said)

# try to define/name each word in the sentence! if the sentence is not as long as 9ish words it will except so it doest throw a index error!

     # word one in sentence 
    try: 
        word1 = what_person_said_p1[0]
        print(word1)
    except IndexError:
         pass
    
     # word two in sentence
    try:
        word2 = what_person_said_p1[1]
        print(word2)
    except IndexError:
         pass
        
     #sentence three in 
    try:
        word3 = what_person_said_p1[2]
        print(word3)
    except IndexError:
         pass
        
    try:
        word4 = what_person_said_p1[3]
        print(word4)
    except IndexError:
        pass
    
    try:
        word5 = what_person_said_p1[4]
        print(word5)
    except IndexError:
        pass
        
    try:
        word6 = what_person_said_p1[5]
        print(word6)
    except IndexError:
        pass
    
  
    try:
        word7 = what_person_said_p1[6]
        print(word7)
    except IndexError:
        pass
    
    try:
        word8 = what_person_said_p1[7]
        print(word8)
    except IndexError:
        pass
    
 
    try:
        word9 = what_person_said_p1[8]
        print(word9)
    except IndexError:
        pass

 
    try:
        word10 = what_person_said_p1[9]
        print(word10)
    except IndexError:
        pass


    try:
        word11 = what_person_said_p1[10]
        print(word11)
    except IndexError:
        pass

    try:
        word12 = what_person_said_p1[11]
        print(word12)
    except IndexError:
        pass


    try:
        word13 = what_person_said_p1[12]
        print(word13)
    except IndexError:
        pass


    try:
        word14 = what_person_said_p1[13]
        print(word14)
    except IndexError:
        pass


    try:
        word15 = what_person_said_p1[14]
        print(word15)
    except IndexError:
        pass



    try:
        word16 = what_person_said_p1[15]
        print(word16)
    except IndexError:
        pass























    
