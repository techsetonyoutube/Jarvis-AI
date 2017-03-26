

GREETING_KEYWORDS = ("hello", "hi", "greetings", "sup", "what's up",)

GREETING_RESPONSES = ["'sup bro", "hey", "*nods*", "hey you get my snap?"]
while 1:
    sentence = input()
    def check_for_greeting(sentence):
        """If any of the words in the user's input was a greeting, return a greeting response"""
        for word in sentence.words:
            if word.lower() in GREETING_KEYWORDS:
                return random.choice(GREETING_RESPONSES)
            
  
    def respond(sentence):
        cleaned = preprocess_text(sentence)
        parsed = TextBlob(cleaned)


        pronoun, noun, adjective, verb = find_candidate_parts_of_speech(parsed)
        resp = check_for_comment_about_bot(pronoun, noun, adjective)
        if not resp:
            resp = check_for_greeting(parsed)

        if not resp:
            if not pronoun:
                resp = random.choice(NONE_RESPONSES)
            elif pronoun == "1" and not verb:
                resp = random.choice(COMMENT_ABOUT_SELF)
            else:
                resp = construct_response(pronoun, noun, verb)
        if not resp:
            resp = random.choice(NONE_RESPONSES)

        logger.info("return phrase '%s'", resp)

        filter_response(resp)

        return resp

    def find_candidate_parts_of_speech(parsed):


        pronoun = None
        noun = None
        adjective = None
        Verb = None
        for sent in parsed.sentence:
            pronoun = find_pronoun(sent)
            noun = find_noun(sent)
            adjective = find_adjective(sent)
            verb = find_verb(sent)
        loggger.info("Pronoun=%s, noun=%s, adjective=%s, verb=%s", pronoun, noun, adjective, verb)
        return pronoun, noun, adjective, verb

    def find_pronoun(sent):
        """Given a sentence, find a preferred pronoun to respond with. Returns None if no candidate
        pronoun is found in the input"""
        pronoun = None

        for word, part_of_speech in sent.pos_tags:
            # Disambiguate pronouns
            if part_of_speech == 'PRP' and word.lower() == 'you':
                pronoun = 'I'
            elif part_of_speech == 'PRP' and word == 'I':
                # If the user mentioned themselves, then they will definitely be the pronoun
                pronoun = 'You'
        return pronoun


    
