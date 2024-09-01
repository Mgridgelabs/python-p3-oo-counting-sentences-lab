#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = ''  
        self.value = value  

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")  

    def is_sentence(self):
        return self._value.endswith('.')

    def is_question(self):
        return self._value.endswith('?')

    def is_exclamation(self):
        return self._value.endswith('!')

    def count_sentences(self):
        import re

        sentence_endings = re.compile(r'[.!?]')
        cleaned_value = re.sub(r'[^\w\s.!?]', ' ', self._value)
        sentences = sentence_endings.split(cleaned_value)
        return len([s for s in sentences if s.strip()])

string = MyString()
string.value = "This is a string! It has three sentences. Right?"
print(string.count_sentences())  

print(string.is_sentence())      
print(string.is_question())     
print(string.is_exclamation())   

string.value = 123  

