class Score:
    def __init__(self, value=0):
        self.value = value
        
    def add(self, add):
        self.value += add
        
    def decrease(self, decrease):
        self.value -= decrease
        
    def __str__(self):
        return "{}".format(self.value)
        
score = Score()
print(score)    # 0
score.add(5)
print(score)    # 5
score.decrease(10)
print(score)    # -5

#----------------------------------------------------------

class Sentence(object):
    def __init__(self, sentence=""):
        self.sentence = sentence
        self.word_list = self.sentence.strip().split()
        
    def get_first_word(self):
        return self.word_list[0]
        
    def get_all_words(self):
        return self.word_list
        
    def replace(self, index, new_word):
        try:
            self.word_list[index] = new_word
            return self.word_list
        except IndexError:
            return
        
    def __str__(self):
        return "{}".format(self.word_list)
        
sent = Sentence('This is a test')
print(sent.get_first_word())      # This
print(sent.get_all_words())       #['This', 'is', 'a', 'test']
sent.replace(3, "must")
print(sent.get_all_words())       #['This', 'is', 'a', 'must']
