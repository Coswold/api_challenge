class Search(object):

    def __init__(self, search_list, match):
        self.sl = search_list
        self.match = match

    def find(self):
        for obj in self.sl:
            i = 0
            while i < len(self.match):
                if self.match[i] != obj['state'][i].lower():
                    break
                i += 1
            if i == len(self.match):
                return obj
        return None
