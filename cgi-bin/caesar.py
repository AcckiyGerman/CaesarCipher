#!/usr/bin/env python3
"""
functions for encoding/decoding messages with the Caesar cipher
"""
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

def encode(message, rot):
    """shifting every symbol in 'message' by 'rot' in ALPHABET. Shift is circled"""
    encoded = []
    rot = round(rot)  # if rot is not integer it will be :)
    for symbol in message.lower():  # and we don't use capitals
        if symbol in ALPHABET:
            shift = (ALPHABET.find(symbol) + rot) % len(ALPHABET)
            # '% MAXROT' is circling shift to avoid 'index out of range' exception
            # and also that operation is a part of Caesar cipher :)
            encoded.append(ALPHABET[shift])
        else:
            encoded.append(symbol)

    return ''.join(encoded)

def decode(cipher, rot):
    return encode(cipher, -rot)

def frequency_dict(text):
    """
    calculates frequency of symbols in text
    :param: text
    :return: dict
    """
    return {symbol: text.count(symbol) for symbol in text if symbol in ALPHABET}

def frequency_list(text):
    """
    returns list of letters presented in text, sorted by frequency
    """
    lettersList = list(set(c for c in text.lower() if c in ALPHABET))
    sortedLettersList = []
    # then pop symbols one by one from max frequency and put it into sortedLettersList
    while lettersList:
        s = lettersList.pop(lettersList.index(max(lettersList, key=text.lower().count)))
        sortedLettersList.append(s)
    return sortedLettersList

def is_english(text):
    """ trying to recognize english text, not ideal can mistakes sometime
    :param text:
    :return: True or False
    """
    text = text.lower()
    F = frequency_list(text)
    if len(F) < 4: return False
    lenth = len(text) if len(text) > 30 else 30
    # magic starts here :)
    P = 0  # Probability
    P += text.count('the') * 1.6
    P += text.count('and') * 0.7
    P += text.count(' a ') * 0.7
    P += text.count('you') * 0.5
    if F[0] == 'e' or F[1] == 'e': P += 0.7
    if F[1] == 't' or F[2] == 't': P += 0.5
    # my probability function :)
    return (P * lenth/40) >= 1

def try_to_guess(text):
    """
    trying to restore text from caesar cipher
    :param text
    :return: text
    """
    answer = ''
    if is_english(text):
        return 'I think the message is not encoded:\n'+text
    # mostFrequencyLetter
    M = frequency_list(text)[0]
    # probablyRotateValue
    pRot = ALPHABET.index(M) - ALPHABET.index('e')
    decodedText = decode(text, pRot)
    if is_english(decodedText):
        return 'I think the message is encoded, probably ROTATE = '+str(pRot)+ \
        '\nDecoded message must be:\n' + decodedText
    for pRot in range(len(ALPHABET)):
        decodedText = decode(text, pRot)
        if is_english(decodedText):
            return 'It was hard to decode this, probably ROTATE = '+str(pRot)+ \
            '\nDecoded message must be:\n' + decodedText
    return 'This message is to hard for me, I need more data :('


if __name__ == '__main__':
    # -----encode-----
    assert encode('a-z0-9', 1) == 'b-a0-9'
    assert encode('abz0-9', -1) == 'zay0-9'
    assert encode('a-z', -len(ALPHABET)*200 - 2) == 'y-x'
    assert encode('veni, vidi, vici', 1) == 'wfoj, wjej, wjdj'
    assert encode('veni, vidi, vici', 0) == 'veni, vidi, vici'
    assert encode('veni, vidi, vici', len(ALPHABET)) == 'veni, vidi, vici'
    assert encode('veni, vidi, vici', len(ALPHABET)*10 + 1) == 'wfoj, wjej, wjdj'
    assert encode('veni, vidi, vici', 2.6) == encode('veni, vidi, vici', 3)
    # -----decode-----
    assert decode('b-a', 1) == 'a-z'
    assert decode('zay0-9', -1) == 'abz0-9'
    assert decode('veni, vidi, vici', 2.6) == decode('veni, vidi, vici', 3)
    assert decode('wfoj, wjej, wjdj', 1) == 'veni, vidi, vici'
    # -----frequency_dict-----
    assert frequency_dict('aaabbc') == {'a':3, 'b':2, 'c':1}
    assert frequency_dict('zzzy5ww\n\t буквы не из алфавита') == {'z':3, 'y':1, 'w':2}
    # -----frequency_list-----
    assert frequency_list('aaabbc') == ['a', 'b', 'c']
    assert frequency_list('zzz---999777 bb y') == ['z', 'b', 'y']
    # -----try_to_guess------
    assert try_to_guess('the good the bad and the ugly') == \
           'I think the message is not encoded:\nthe good the bad and the ugly'