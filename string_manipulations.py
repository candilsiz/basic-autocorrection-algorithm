
class TextManipulations:

    def __init__(self):
        self.letters = 'abcdefghijklmnopqrstuvwxyz'
    
    @staticmethod
    def delete_letter(word, verbose = False):
        '''
        Input:
            word: the string/word for which you will generate all possible words 
                    in the vocabulary which have 1 missing character
        Output:
            delete_l: a list of all possible strings obtained by deleting 1 character from word
        '''
        delete_l = []
        split_l = []
        split_l = [(word[:i], word[i:]) for i in range(len(word))]
        for L,R in split_l:
            delete_l.append(L + R[1:])

        if verbose: print(f"input word {word}, \nsplit_l = {split_l}, \ndelete_l = {delete_l}")
        return  delete_l
    
    @staticmethod
    def switch_letter(word, verbose=False):
        '''
        Input:
            word: input string
        Output:
            switches: a list of all possible strings with one adjacent charater switched
        ''' 
        switch_l = []
        split_l = []
        split_l = [(word[:i], word[i:]) for i in range(len(word))]
        for L,R in split_l:
            if len(R) >= 2 :
                to_switch = R[1] + R[0]
                rest_of_it = R[2:]
                new_word = L + to_switch + rest_of_it
                switch_l.append(new_word)

        if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nswitch_l = {switch_l}") 
        return switch_l

    def replace_letter(self, word, verbose=False):
        '''
        Input:
            word: the input string/word 
        Output:
            replaces: a list of all possible strings where we replaced one letter from the original word. 
        ''' 
        replace_l = []
        split_l = []
        split_l = [(word[:i], word[i:]) for i in range(len(word))]
        replace_l = [a + lttr + (b[1:] if len(b) > 1 else '') for a, b in split_l if b for lttr in self.letters]
        replace_set = set(replace_l)
        replace_set.remove(word)
        replace_l = sorted(list(replace_set))

        if verbose: print(f"Input word = {word} \nsplit_l = {split_l} \nreplace_l {replace_l}")   
        return replace_l

    def insert_letter(self, word, verbose=False):
        '''
        Input:
            word: the input string/word 
        Output:
            inserts: a set of all possible strings with one new letter inserted at every offset
        ''' 
        insert_l = []
        split_l = []
        split_l = [(word[:i], word[i:]) for i in range(len(word) + 1)]
        for lttr in self.letters:
            for L,R in split_l:
                inserted_word = L + lttr + R
                insert_l.append(inserted_word)
        
        if verbose: print(f"Input word {word} \nsplit_l = {split_l} \ninsert_l = {insert_l}")
        return insert_l

    def edit_one_letter(self, word, allow_switches = True):
        """
        Input:
            word: the string/word for which we will generate all possible words that are one edit away.
        Output:
            edit_one_set: a set of words with one possible edit.
        """
        edit_one_set = set()
        edit_one_list = list()
        s_word = [] # for allow_switches = False

        # OPERATIONS: delete_letter, switch_letter, replace_letter, insert_letter 
        d_word = self.delete_letter(word)
        r_word = self.replace_letter(word)
        i_word = self.insert_letter(word)
        if allow_switches:
            s_word = self.switch_letter(word)
        edit_one_list = d_word + r_word + i_word + s_word
        edit_one_set = set(edit_one_list)

        return edit_one_set
    
    def edit_two_letters(self, word, allow_switches = True):
        '''
        Input:
            word: the input string/word 
        Output:
            edit_two_set: a set of strings with all possible two edits
        '''  
        edit_two_set = set()
        edit_one = self.edit_one_letter(word, allow_switches=allow_switches)
        for w in edit_one:
            if w:
                edit_two = self.edit_one_letter(w, allow_switches=allow_switches)
                edit_two_set.update(edit_two)
        return set(edit_two_set)
    
    



