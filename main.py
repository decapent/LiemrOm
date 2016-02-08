# -*- coding: utf-8 -*-
"""
 Ceci script permet de traduire du LiemrOm au francais.
 Le langage LiemrOm est tiré du livre de Ghislain Taschereau - Etoiles Tombantes.

 L'auteur en question m'a lancé le défi de trouver l'erreur
 qui s'était glissée dans sa langue inventée.

 Le programme ne corrige pas les fautes de francais. Cette verification
 doit se faire manuellement.

 TL;DR Challenge accepted!
"""

import Repository


def is_vowel(l):
    for vowel in _vowels:
        if l == vowel:
            return True

    return False


def is_translatable(l):
    for character in _specialCharacters:
        if l == character:
            return False

    return True


def translate_sentence(s):
    s = s.lower()
    translation = ""
    for char in s:
        if is_translatable(char):
            if is_vowel(char):
                translation += _vowels[_vowels.index(char) + 1] if _vowels.index(char) < len(_vowels) - 1 else _vowels[0]
            else:
                translation += _consonants[_consonants.index(char) + 1] if _consonants.index(char) < len(_consonants) - 1 else _consonants[0]
        else:
            translation += char

    return translation


def pretty_print_and_export(dictionary, filename):
    output = open(filename, "w")
    for translatedPage in sorted(dictionary):
        header = "\nTraduction de la page %s" % translatedPage
        print header
        output.write(header + "\n")

        for translatedSentence in dictionary[translatedPage]:
            print translatedSentence
            output.write(translatedSentence + "\n")

    output.close()

# Main Program
_vowels = Repository.vowels
_consonants = Repository.consonants
_specialCharacters = Repository.specialChars
_liemrOmDictionary = Repository.liemrOmDictionary

# Etape 1 - Traduction du dialecte de Lothaire Fillion
translatedDictionary = {}
for page in _liemrOmDictionary.keys():
    translatedPageSentences = []
    for sentence in _liemrOmDictionary[page]:
        translatedPageSentences.append(translate_sentence(sentence))

    translatedDictionary[page] = translatedPageSentences

# Etape 2 - Export de la traduction
pretty_print_and_export(translatedDictionary, "translation.txt")
