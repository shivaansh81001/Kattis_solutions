'''
  -https://github.com/cheran-senthil/PyRival/blob/master/pyrival/data_structures/Trie.py
  -https://www.geeksforgeeks.org/count-the-number-of-words-with-given-prefix-using-trie/
'''
class Trie:
    def __init__(self):
        self.root = {}

    def add(self, word):
        current_dict = self.root
        for letter in word:
            current_dict = current_dict.setdefault(letter, {})
        # Instead of setting '_end_' to True, we can use it to count occurrences.
        current_dict['_end_'] = current_dict.get('_end_', 0)+1
    def __delitem__(self, word):
        current_dict = self.root
        nodes = [current_dict]
        for letter in word:
            current_dict = current_dict[letter]
            nodes.append(current_dict)
        del current_dict["_end_"]
        
    @staticmethod
    def count(word):
        ct=word.get('_end_',0)
        #print('=',ct)
        for i in word:
            if i=='_end_':
                pass
            else:
                ct+=Trie.count(word[i])
        return ct

    def prefixes(self,pref):
        ret=0
        current_dict=self.root
        for i in pref:
            if i in current_dict:
                current_dict=current_dict[i]
            else:
                return ret
        return self.count(current_dict)+ret
    
    def prr():
        print(self.root)
    

def main():
    tree=Trie()
    n=int(input())
    for i in range(n):
        temp=input()
        print(tree.prefixes(temp))
        tree.add(temp)
        #tree.prr()

main()