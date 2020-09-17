# %% [markdown]
# **[Python Home Page](https://www.kaggle.com/learn/python)**
# 
# ---
# 

# %% [markdown]
# # Try It Yourself
# 
# You are almost done with the course. Nice job. 
# 
# Fortunately, we have a couple more interesting problems for you before you go. 
# 
# As always, run the setup code below before working on the questions.

# %% [code]
from learntools.core import binder; binder.bind(globals())
from learntools.python.ex6 import *
print('Setup complete.')

# %% [markdown]
# # Exercises

# %% [markdown]
# ## 0. 
# 
# Let's start with a string lightning round to warm up. What are the lengths of the strings below?
# 
# For each of the five strings below, predict what `len()` would return when passed that string. Use the variable `length` to record your answer, then run the cell to check whether you were right.  

# %% [code]
a = ""
length = len(a)
q0.a.check()

# %% [code]
b = "it's ok"
length = len(b)
q0.b.check()

# %% [code]
c = 'it\'s ok'
length = 7
q0.c.check()

# %% [code]
d = """hey"""
length = 3
q0.d.check()

# %% [code]
e = '\n'
length = 1
q0.e.check()

# %% [markdown]
# ## 1.
# 
# There is a saying that "Data scientists spend 80% of their time cleaning data, and 20% of their time complaining about cleaning data." Let's see if you can write a function to help clean US zip code data. Given a string, it should return whether or not that string represents a valid zip code. For our purposes, a valid zip code is any string consisting of exactly 5 digits.
# 
# HINT: `str` has a method that will be useful here. Use `help(str)` to review a list of string methods.

# %% [code]
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """         
    if (len(str(zip_code))==5 and zip_code.isdigit()==True):
        return True
    return False

# Check your answer
q1.check() 

# %% [code]
help(str)

# %% [code]
#q1.hint()
#q1.solution()

# %% [markdown]
# ## 2.
# 
# A researcher has gathered thousands of news articles. But she wants to focus her attention on articles including a specific word. Complete the function below to help her filter her list of articles.
# 
# Your function should meet the following criteria:
# 
# - Do not include documents where the keyword string shows up only as a part of a larger word. For example, if she were looking for the keyword “closed”, you would not include the string “enclosed.” 
# - She does not want you to distinguish upper case from lower case letters. So the phrase “Closed the case.” would be included when the keyword is “closed”
# - Do not let periods or commas affect what is matched. “It is closed.” would be included when the keyword is “closed”. But you can assume there are no other types of punctuation.

# %% [code]
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
    list_index=[]
    keyword=keyword.lower()
    for doc in doc_list:
        doc_orig=doc
        doc=doc.lower()
        if doc.find(keyword)!=-1 and doc.find(keyword)+len(keyword)>=len(doc):
            if doc[(doc.find(keyword)-1)]==" ":
                list_index.append(doc_list.index(doc_orig))
        if doc.find(keyword)!=-1 and doc.find(keyword)+len(keyword)<len(doc): 
            if (doc[doc.find(keyword)+len(keyword)]==" " or doc[doc.find(keyword)+len(keyword)]=="." or doc[doc.find(keyword)+len(keyword)]==",") and (doc[(doc.find(keyword)-1)]==" " or doc[doc.find(keyword)-1]==doc[-1]):
                list_index.append(doc_list.index(doc_orig))
    return list_index
        
# Check your answer
q2.check()

# %% [code]
list=["a", "b", "cd", "d"]
a="abcd encode"
keyword="a"
print(a.find(keyword))
print(a[a.find(keyword)-1])
print(list.index("cd"))
"code" in a

# %% [code]
q2.hint()
q2.solution()

# %% [code]
documents=["a","b","c"]
print(list(enumerate(documents)))
documents.index("a")

# %% [code]
def word_search(documents, keyword):
    # list to hold the indices of matching documents
    indices = [] 
    # Iterate through the indices (i) and elements (doc) of documents
    for i, doc in enumerate(documents):
        # Split the string doc into a list of words (according to whitespace)
        tokens = doc.split()
        # Make a transformed list where we 'normalize' each word to facilitate matching.
        # Periods and commas are removed from the end of each word, and it's set to all lowercase.
        normalized = [token.rstrip('.,').lower() for token in tokens]
        # Is there a match? If so, update the list of matching indices.
        if keyword.lower() in normalized:
            indices.append(i)
    return indices


word_search(["The Learn Python Challenge Casino.", "They bought a car", "Casinoville bought"], ["Casino","bought"])

# %% [markdown]
# ## 3.
# 
# Now the researcher wants to supply multiple keywords to search for. Complete the function below to help her.
# 
# (You're encouraged to use the `word_search` function you just wrote when implementing this function. Reusing code in this way makes your programs more robust and readable - and it saves typing!)

# %% [code]
def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    indices=[]
    keys=[]
    for keyword in keywords:
        indices_check=[]
        lista_indice=[]
        for i, doc in enumerate(doc_list):
            tokens = doc.split()
            normalized = [token.rstrip('.,').lower() for token in tokens] #lista do respectivo doc, normalizada!
            if keyword.lower() in normalized:
                lista_indice.append(i)
                indices_check.append(i)
        if indices_check==[]:
            indices.append(indices_check)
        else:
            indices.append(lista_indice)
        keys.append(keyword)
    dictionary={key:indices[keys.index(key)] for key in keys}
    return dictionary

# Check your answer
q3.check()

# %% [code]
q3.solution()

# %% [markdown]
# # Keep Going
# 
# You've learned a lot. But even the best programmers rely heavily on "libraries" of code from other programmers. You'll learn about that in **[the last lesson](https://www.kaggle.com/colinmorris/working-with-external-libraries)**.
# 

# %% [markdown]
# ---
# **[Python Home Page](https://www.kaggle.com/learn/python)**
# 
# 
# 
# 
# 
# *Have questions or comments? Visit the [Learn Discussion forum](https://www.kaggle.com/learn-forum/161283) to chat with other Learners.*