import random

tenses = ["past", "present", "future"]
quantity = random.randint(1, 2)
randtense = random.choice(tenses)


def main():
    print(f"{get_determiner(quantity).capitalize()} {get_noun(quantity)} {get_verb(quantity, randtense)} {get_prepositional_phrase(quantity)}")

def get_determiner(quantity):
    if quantity == 1:
        words = ["the", "one"]
    else:
        words = ["some", "many"]

    # Randomly choose and return a determiner.
    word = random.choice(words)
    return word

def get_noun(quantity):

    if quantity == 1:
        nouns = ["adult", "bird", "boy", "car", "cat", "child", "dog", "girl", "man", "woman"]
    else:
        nouns = ["adults", "birds", "boys", "cars", "cats", "children", "dogs", "girls", "men", "women"]

    noun = random.choice(nouns)
    return noun
    
def get_verb(quantity, tense):

    if tense == "past":
        verbs = ["drank", "ate", "grew", "laughed", "thought", "ran", "slept", "talked", "walked", "wrote"]

    if tense == "present":
        if quantity == 1:
            verbs = ["drinks", "eats", "grows", "laughs", "thinks", "runs", "sleeps", "talks", "walks", "writes"]
        if quantity != 1:
            verbs = ["drink", "eat", "grow", "laugh", "think", "run", "sleep", "talk", "walk", "write"]
    if tense == "future":
        verbs = ["will drink", "will eat", "will grow", "will laugh", "will think", "will run", "will sleep", "will talk", "will walk", "will write"]

    verb = random.choice(verbs)
    return verb

def get_preposition():
    prespositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    
    preposition = random.choice(prespositions)
    return preposition
    
def get_prepositional_phrase(quantity):
    prepositional_phrase = (f"{get_preposition()} {get_determiner(quantity)} {get_noun(quantity)}")
    return prepositional_phrase

main()





   