import pytest
from sentences import get_adjective, get_determiner, get_noun, get_verb, get_preposition, get_prepositional_phrase
import random



def test_get_determiner():
    # 1. Test the single determiners.

    single_determiners = ["a", "one", "the"]

    # This loop will repeat the statements inside it 4 times.
    # If a loop's counting variable is not used inside the
    # body of the loop, many programmers will use underscore
    # (_) as the variable name for the counting variable.
    for _ in range(4):

        # Call the get_determiner function which
        # should return a single determiner.
        word = get_determiner(1)

        # Verify that the word returned from get_determiner
        # is one of the words in the single_determiners list.
        assert word in single_determiners

    # 2. Test the plural determiners.

    plural_determiners = ["two", "some", "many", "the"]

    # This loop will repeat the statements inside it 4 times.
    for _ in range(4):

        # Get a random number between 2 and 10 inclusive.
        quantity = random.randint(2, 11)

        # Call the get_determiner function which
        # should return a plural determiner.
        word = get_determiner(quantity)

        # Verify that the word returned from get_determiner
        # is one of the words in the plural_determiners list.
        assert word in plural_determiners


def test_get_noun():
    single_noun = ["bird", "boy", "car", "cat", "child",
        "dog", "girl", "man", "rabbit", "woman"]

    for _ in range(4):
        noun = get_noun(1)
        assert noun in single_noun

    plural_noun = ["birds", "boys", "cars", "cats", "children",
        "dogs", "girls", "men", "rabbits", "women"]
    
    for _ in range(4):
        quantity = random.randint(2, 11)
        noun = get_noun(quantity)
        assert noun in plural_noun

def test_get_verb():
    past_verb = ["drank", "ate", "grew", "laughed", "thought",
        "ran", "slept", "talked", "walked", "wrote"]
    for _ in range(4):
        verb = get_verb(1,"past")
        assert verb in past_verb
    present_verb = ["drinks", "eats", "grows", "laughs", "thinks",
        "runs", "sleeps", "talks", "walks", "writes"]
    for _ in range(4):
        verb = get_verb(1,"present")
        assert verb in present_verb
    present_plural_verb = ["drink", "eat", "grow", "laugh", "think",
        "run", "sleep", "talk", "walk", "write"]
    for _ in range(4):
        quantity = random.randint(2, 11)
        verb = get_verb(quantity,"present")
        assert verb in present_plural_verb
    future_verb = ["will drink", "will eat", "will grow", "will laugh",
        "will think", "will run", "will sleep", "will talk",
        "will walk", "will write"]
    for _ in range(4):
        verb = get_verb(1, "future")
        assert verb in future_verb

def test_get_preposition():
    prepositions = ["about", "above", "across", "after", "along",
        "around", "at", "before", "behind", "below",
        "beyond", "by", "despite", "except", "for",
        "from", "in", "into", "near", "of",
        "off", "on", "onto", "out", "over",
        "past", "to", "under", "with", "without"]
    for _ in range(4):
        preposition = get_preposition()
        assert preposition in prepositions

def test_get_prepositional_phrase():
    quantity = random.randint(2,11)
    phrases = get_prepositional_phrase(quantity) 
    words = phrases.split(' ')
    
    assert len(words) == 4

def test_get_adjective():
    adjectives = ["charming", "cruel", "fantastic", "gentle",
     "huge", "perfect", "rough", "sharp"]
    for _ in range(4):
        adjective = get_adjective()
        assert adjective in adjectives


pytest.main(["-v", "--tb=line", "-rN", __file__])