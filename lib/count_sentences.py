#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.value = ""
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
    return self.value.endswith(".")
  
  def is_question(self):
    return self.value.endswith("?")
  
  def is_exclamation(self):
    return self.value.endswith("!")
  
  def count_sentences(self):
        if not self.value:
            return 0
        # Split the value by periods, question marks, and exclamation points
        sentences = self.value.split('.')
        # Further split by question marks and exclamation points
        split_sentences = []
        for sentence in sentences:
            split_sentences.extend(sentence.split('?'))
        final_sentences = []
        for sentence in split_sentences:
            final_sentences.extend(sentence.split('!'))
        # Filter out empty strings and strings with only whitespace
        final_sentences = [s for s in final_sentences if s.strip()]
        return len(final_sentences)
