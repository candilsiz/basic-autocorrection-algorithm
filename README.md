### Basic Auto-Correction Algrorithm Steps:
1. Identify a misspelled word
2. Find strings n edit distance away
3. Filter candidates
4. Calculate word probabilities

### Data Processing:
the function `process_data`:
- Reads in a corpus (text file)
- Changes everything to lowercase
- Returns a list of words. 

the function `get_count`:
- return dictionary's keys are words
- The value for each word is the number of times that word appears in the corpus. 

the function `get_probs`: 
-  gives you the probability that a word occurs in a sample.  
- returns a dictionary where the keys are words, and the value for each word is its probability in the corpus of words.

### String Manipulations:
* `delete_letter`: given a word, it returns all the possible strings that have **one character removed**. 
* `switch_letter`: given a word, it returns all the possible strings that have **two adjacent letters switched**.
* `replace_letter`: given a word, it returns all the possible strings that have **one character replaced by another different letter**.
* `insert_letter`: given a word, it returns all the possible strings that have an **additional character inserted**. 

### Combining Edits and Autocorrection:
* If the word is in the vocabulary, suggest the word. 
* Otherwise, if there are suggestions from `edit_one_letter` that are in the vocabulary, use those. 
* Otherwise, if there are suggestions from `edit_two_letters` that are in the vocabulary, use those. 
* Otherwise, suggest the input word.*  
* The idea is that words generated from fewer edits are more likely than words with more edits.

