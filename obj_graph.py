# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 18:42:31 2017

@author: Ryan Lott

                        Game rules:
                            
Objective: Connect both keyboard sides with a single word
All letters in the word must form a single chain

"""
import time
import os
from graph_func import Graph

# Start timer
start_time = time.time() 
# Grab data 
a = os.getcwd()
a= open(a+'\\words.txt','r').read()
words = a.lower().split("\n")
# Graph of possible connections
graph = { "a" : ["q",'w','s','z'],
          "b" : ["v", "g",'h','n'],
          "c" : ["x", "d", "f", "v"],
          "d" : ["s", "e", "r", "f",'c','x'],
          "e" : ["w", "s", "d", "r"],
          "f" : ["d", "r", "t", "g",'v','c'],
          "g" : ["f", "t", "y", "h",'b','v'],
          "h" : ["g", "y", "u", "j",'n','b'],
          "i" : ["u", "j", "k", "o"],
          "j" : ["h", "u", "i", "k",'m','n'],
          "k" : ["j", "i", "o", "l",'m'],
          "l" : ["k", "o", "p"],
          "m" : ["n", "j", "k"],
          "n" : ["b", "h", "j", "m"],
          "o" : ["i", "k", "l", "p"],
          "p" : ["o", "l"],
          "q" : ["w", "a"],
          "r" : ["e", "d", "f", "t"],
          "s" : ["a", "w", "e", "d",'x','z'],
          "t" : ["r", "f", "g", "y"],
          "u" : ["y", "h", "j", "i"],
          "v" : ["c", "f", "g", "b"],
          "w" : ["q", "a", "s", "e"],
          "x" : ["z", "s", "d", "c"],
          "y" : ["t", "g", "h", "u"],
          "z" : ["a", "s", "x"]  }
# Stores all words that cross the keyboard for outputing
successes = []
# Define edge connections that would infer success
attempts = ['qp','ap','zp','ql','al','zl','qm','am','zm']
# Loop all words in 466k words in dictionary and test against parameters
for word in words:
    if len(word) > 6: # Impossible to cross in 6, fastest method to eliminate
        # Limit graph to only have access to connections for letters in word
        dicts = {}
        letters = [letter for letter in word]
        for letter in letters:
            # Try/Except to handle special characters
            try:
                matches = [match for match in graph[letter] if match in letters]
                dicts[letter] = matches
            except: pass
        if not any(dicts[key] == [] for key in dicts.keys()): # Error handling
            # Create graph
            g = Graph(dicts)
            links = []
            for key in dicts.keys():
                for key1 in dicts.keys():
                    links.append([key,key1])
            # Test for a single contiguous chain of letters
            if not any(str(g.find_path(link[0],link[1]))=="None" for link in links):
                # Test if  letter combination that crosses the keyboard exists
                for attempt in attempts:
                    if g.find_path(attempt[0],attempt[1]):
                        print(attempt," success: ", word)
                        successes.append(word+": "+attempt)   
# Takes roughly 6.5s
end_time = time.time() - start_time
print("Time to complete: ",end_time)