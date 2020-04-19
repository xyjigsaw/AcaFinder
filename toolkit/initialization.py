# Name: initialization
# Author: Reacubeth
# Time: 2020/2/28 15:46
# Mail: noverfitting@gmail.com
# Site: www.omegaxyz.com
# *_*coding:utf-8 *_*


import sys
import os
from Model.neo4j_models import Neo4jTool
from toolkit.embedding.vec_sim import EmbeddingModel


neo_con = Neo4jTool()  # Load neo4j
neo_con.connect2neo4j()
print('Neo4j has connected...')

# Load author embedding
author_emb = EmbeddingModel()
author_emb.read_vec(os.path.dirname(os.path.abspath(__file__)) + '/embedding/entity_embeddings.tsv', 'author')
