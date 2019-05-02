#import nltk.tokenize as nt
#from nltk.tag import pos_tag
from collections import Counter
import string
import nltk


def get_labels(text, title, **kwargs):
    naked = text.translate(str.maketrans('','',string.punctuation))
    words = naked.split()
    counts = Counter(words)
    tagged = nltk.pos_tag(words)
    #looking for tag NNP (noun prpper singular)
    entities = nltk.chunk.ne_chunk(tagged)
    
    #title_words = title.split()
    #title_counts = Counter(title_words)
    #title_tagged = nltk.pos_tag(title_words)
    #title_entities = nltk.chunk.ne_chunk(title_tagged)
    
    #pronouns = set()
    pronouns = {}
    for chunck in entities:
        if type(chunck) == nltk.tree.Tree:
            name = ""
            total_score = 0
            score = {}
            remove_list = []
            word_scores = []
            word_scores.append(0)
            in_title = 1
            for word, tag in chunck:
                if word.lower() in title.lower():
                    in_title = 5
                if tag == "NNP":
                    name += word + " "
                    #total_score += (counts[word] * in_title)
                    score[word] = counts[word]
                    word_scores.append(counts[word])
                    remove_list.append(word)
                else:
                    break
                #score["score list"] = word_scores
            for l in remove_list:
                pronouns[l] = ""
                del pronouns[l]
            score["total"] = max(word_scores) * in_title
            name = name.strip()
            if name != "":
                pronouns[name] = score
        else:
            if chunck[1] == "NNP":
                score = {"total": counts[chunck[0]]}
                pronouns[chunck[0]] = score
    
    #pronouns = set()
    #for item in tagged:
    #    if item[1] == "NNP":
    #        pronouns.add((item[0], counts[item[0]]))
            
    #entities = nltk.chunk.ne_chunk(tagged)
    #pronouns = list(pronouns)
    #pronouns = sorted(pronouns, key=lambda tup: tup[1])
    #num_results = min(len(pronouns), 3)
    
    return pronouns



