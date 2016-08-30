from collections import defaultdict

lemma_pos_offset_map=defaultdict(dict)

for line in open('data.noun'): #noun,verb,adj,adv
    columns_str,gloss=line.split('|')
    offset,lexname_index,pos,n_lemmas,lemma,lex_id,n_pointers=columns_str.split()
    try:lemma_pos_offset_map[lemma][pos].append(offset)
    except:lemma_pos_offset_map[lemma][pos]=[offset]

n_synsets=n_senses=1
n_pointers=n_senses_ranked=0

for lemma in lemma_pos_offset_map:
    for pos,offsets in lemma_pos_offset_map[lemma].items():
        n_synsets=n_senses=len(offsets)
        print(lemma,pos,n_synsets,n_pointers,n_senses,n_senses_ranked,' '.join(offsets))
