import kashgari
from kashgari.embeddings import WordEmbedding

# need to spesify task for the downstream task,
# if use embedding for feature extraction, just set `task=kashgari.CLASSIFICATION`
bert = WordEmbedding('sgns.sogou.word',
                     sequence_length=600)
# call for bulk embed
embed_tensor = bert.embed([['语', '言', '模', '型']])

# call for single embed

print(embed_tensor)