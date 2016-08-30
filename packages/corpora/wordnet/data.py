from unicodedata import east_asian_width
from sqlite3 import connect

conn=connect(database='cwn_dirty.sqlite')
c=conn.cursor()

offset=0
c.execute('select sense_id,sense_def from cwn_sense')
for sense_id,sense_def in c.fetchall():
    c.execute('select pos from cwn_pos where cwn_id like "%'+sense_id+'%"')
    try:
        pos=c.fetchone()[0].lower()[0]
        if pos=='n': #n,v,a,d
#           pos='r'
            c.execute('select lemma_type from cwn_lemma where lemma_id="'+sense_id[:6]+'"')
            lemma_type=c.fetchone()[0]
            c.execute('select example_cont from cwn_example where cwn_id="'+sense_id+'"')
            example=c.fetchone()[0].strip().replace('\r\n','').replace('\n','').replace('∥','').replace('|','')
            offset,lexname_index,pos,n_lemmas,lemma_name,lex_id,n_pointers,gloss,example=offset,              str(0).zfill(2),  pos,  str(1).zfill(2), lemma_type,    str(0), str(0).zfill(3), sense_def,     example
            line=' '.join(                                                          [str(offset).zfill(8),    lexname_index,    pos,  n_lemmas,        lemma_name,    lex_id, n_pointers, '|', gloss+';', '"'+example+'"' ]) + '\n'
            print(line,end='')
            offset+=len(line)+len([c for c in line if east_asian_width(c) in ('W','F')])*2
    except:pass
conn.close()
