import pandas as pd

class Standardizer:

    def __init__(self):
        self.format = ['is_hatespeech','class','text']
        self.classes = {
            'none': 0,
            'other': 0,
            'origin': 1,
            'racism': 1,
            'religion': 2,
            'disability': 3,
            'sexist': 4,
            'sexism': 4,
            'gender': 4,
            'sexual_orientation': 5,
            'toxic': 6,
            'obscene': 7,
        }
        self.data = []

    def add(self, is_hatespeech, text, type = 'none'):
        self.data.append({ self.format[0]: is_hatespeech, self.format[1]: self.classes[type], self.format[2]: text })

    def export(self, filename):
        df = pd.DataFrame(self.data)
        df.to_csv('datasets/' + filename + '_standard.csv')