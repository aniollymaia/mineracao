
# coding: utf-8

# UNIVERSIDADE FEDERAL DE MINAS GERAIS - UFMG 
# ESCOLA DE CIÊNCIA DA INFORMAÇÃO – ECI 
# PROGRAMA DE PÓS-GRADUAÇÃO EM GESTÃO & ORGANIZAÇÃO DO CONHECIMENTO
# DISCIPLINA: Tópicos Especiais em GET II: Representações Distribuídas de Texto e Modelagem de Tópicos 
# DOCENTE: Prof. Renato Rocha de Souza / Prof. Mauricio Barcellos Almeida / Profa. Renata Maria Abrantes Baracho Porto 
# DISCENTE: Maria Aniolly Queiroz Maia
# 
# Belo Horizonte, 05 de dezembro de 2017
# 
# 
# 1 Objetivo geral
# 
# Desenvolver uma word cloud a partir das palavras recorrentes nos resumos dos artigos de temática "Usabilidade" disponíveis no indexador Scielo.
# 
# 2 Objetivos específicos:
# 
# • Minerar artigos científicos na temática Usabilidade, no idioma português da Scielo, fazendo uso de Python;
# 
# • Capturar os artigos de temática Usabilidade por título, periódico, autor e resumo;
# 
# • Criar uma lista de palavras, remover as stop words dessa lista, apresentando a recorrência de cada palavra a partir dos resumos disponíveis nas publicações mineradas;
# 
# 3 Metodologia
# 
# Para efetivação do objetivo proposto, incicialmente foi realizada a mineração dos dados disponíveis na base de dados Scielo, a partir de uma pesquisa ao termo "Usabilidade", no idioma português, no qual foi possível identificar um total de 117 documentos. Posteriormente foi realizada a captura (web crawler) dos seguintes dados: título dos artigos, título dos periódicos, autorias e resumos em português.
# Em seguida, foi criada uma lista de palavras a partir da remoção das stop words dos resumos no idioma português. Além disso, foi identificada a recorrência de cada palavra descrita nos resumos, essas palavras foram utilizadas para o desenvolvimento da word cloud. Para alcançar os objetivos propostos, utilizou-se diversas bibliotecas de Python, com destaque para:
# 
# BeautifulSoup: Utilizada para extrair dados de arquivos HTML e XML. Funciona com o seu analisador favorito para fornecer maneiras idiomáticas de navegar, pesquisar e modificar a árvore de análise. Geralmente economiza horas ou dias de trabalho do programador;
# Pandas: Oferece estruturas de dados de alto desempenho. Essa biblioteca é de fácil de uso, sendo uma grande ferramentas de análise de dados;
# Gensim: Tem o objetivo de lidar com grandes coleções de texto, usando streaming de dados e algoritmos incrementais eficientes, o que o diferencia da maioria dos outros pacotes de software científicos que apenas destinam o processamento em lote e na memória;
# Matplotlib: Fornece uma API orientada a objetos para incorporar gráficos em aplicativos que usam kits de ferramentas de uso geral;
# NLTK: Biblioteca para Processamento de Linguagem Natural (PLN) e Text Analytics, originalmente criada para o ensino de PLN, mas que vem sendo amplamente adotado no desenvolvimento de aplicações de PLN em geral. Trata-se de um kit de ferramentas útil para separar as sentenças em um parágrafo, separar as palavras dentro de cada sentença, reconhecer padrões no texto e criar modelos de classificação que permitam, por exemplo, realizar análise de sentimentos em um conjunto de dados.
# 
# 
# 4 Dificuldades e limitações
# 
# Ao considerar Python como uma linguagem de programação relativamente fácil, se comparada a outras linguagens, tive dificuldades para alcançar os objetivos propostos, principalmente pelo fato de nunca ter trabalhado com uma linguagem de programação, o que exigiu maiores esforços de minha parte, fazendo além do curso sugerido pelo Prof. Renato Rocha, outros cursos online, com destaque para dois suportes que me ajudaram bastante, um minicurso de título "Mineração de Emoção em Textos com Python e NLTK" da empresa Udemy, e o Github de autoria de Bárbara Babosa (@bahbbc).
# Vale ressaltar ainda que a disciplina possibilitou que eu aprendesse um pouco acerca dessa relevante área (Mineração de dados) que cresce exponencialmente, exigindo profissionais qualificados para tratar, organizar e disseminar esses dados, e o profissional da informação, deve estar atento e capacitado para atuar nesse contexto. Como sugestão, acredito que a disciplina poderia ter uma carga horária maior com aulas práticas e presenciais, o que ao meu ver, facilitaria o processo de aprendizagem.
# Por fim, agradeço pelo desafio e parabenizo os professores envolvidos na construção da disciplina.

# In[131]:


# Nessa etapa, foi realizada uma mineração de dados sobre a temática Usabilidade na Biblioteca Digital Scielo. A busca geral retornou um total de 117 documentos.
# Desse total de documentos, foram minerados a partir da atividades de captura (web crawler) os seguintes dados: título, autor, nome do periódico e resumo na idioma portugês.

# Etapa 1: Mineração referente aos títulos dos artigos da temática "Usabilidade".
 
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from requests import get
import time
import unicodedata
import re
import csv
import pandas


def getURLBase(string_busca,quantidade_busca, a_partir, numero_pagina):
    return 'http://search.scielo.org/?q={0}&lang=pt&count={1}&from={2}&output=site&format=summary&lang=pt&page={3}'            .format(string_busca, str(quantidade_busca), a_partir, numero_pagina)
   

string_busca = "usabilidade"
quantidade_busca = 100
a_partir = 0
titulos = []
contador = 0

for i in range(1, 3):
    base_url = getURLBase(string_busca,quantidade_busca, a_partir, i)
    a_partir += quantidade_busca + 1
    driver = webdriver.Chrome()
    driver.get(base_url)
    bs_obj = bs(driver.page_source,'html.parser')
    driver.close()

    for elemento in bs_obj.findAll("strong", { "class" : "title" }):
       titulos.append(elemento.text.strip()) 
    
print(titulos)   


# In[132]:


# Etapa 2: Mineração referente aos títulos das revistas nas quais os artigos foram publicados.
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from requests import get
import time
import unicodedata
import re
import csv
import pandas


def getURLBase(string_busca,quantidade_busca, a_partir, numero_pagina):
    return 'http://search.scielo.org/?q={0}&lang=pt&count={1}&from={2}&output=site&format=summary&lang=pt&page={3}'            .format(string_busca, str(quantidade_busca), a_partir, numero_pagina)
   

string_busca = "usabilidade"
quantidade_busca = 100
a_partir = 0
titulos = []
con = 0

for i in range(1, 3):
    base_url = getURLBase(string_busca,quantidade_busca, a_partir, i)
    a_partir += quantidade_busca + 1
    driver = webdriver.Chrome()
    driver.get(base_url)
    bs_obj = bs(driver.page_source,'html.parser')
    driver.close()
    
    for elemento in bs_obj.findAll("div", { "class" : "item" }):
      
       revista = elemento.find("a", {"class": "openJournalInfo"})
       print(revista.string)   
       con += 1
       print(con)
    
   


# In[135]:


# Etapa 3: Mineração da indicação de autoria dos artigos publicados.

from bs4 import BeautifulSoup as bs
from selenium import webdriver
from requests import get
import time
import unicodedata
import re
import csv
import pandas


def getURLBase(string_busca,quantidade_busca, a_partir, numero_pagina):
    return 'http://search.scielo.org/?q={0}&lang=pt&count={1}&from={2}&output=site&format=summary&lang=pt&page={3}'            .format(string_busca, str(quantidade_busca), a_partir, numero_pagina)
   

string_busca = "usabilidade"
quantidade_busca = 100
a_partir = 0
titulos = []
con = 0

for i in range(1, 3):
    base_url = getURLBase(string_busca,quantidade_busca, a_partir, i)
    a_partir += quantidade_busca + 1
    driver = webdriver.Chrome()
    driver.get(base_url)
    bs_obj = bs(driver.page_source,'html.parser')
    driver.close()
    
    for elemento in bs_obj.findAll ("div", { "class" : "item" }):
        autor = elemento.find ("div", { "class" : "authors"})
        print(autor.text.strip()) 
             


# In[62]:


# Etapa 4 - Criação de lista de palavras (Dicionário) a partir da captura (web crawler) dos resumos no idioma português, remoção das stop words, recorrência de cada palavra e desenvolvimento de uma word cloud

import re
import os
import codecs
import string
import numpy as np
import pandas as pd
import gensim

import nltk
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.tokenize import word_tokenize

from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn import feature_extraction
import mpld3

import pyLDAvis
import pyLDAvis.gensim
from IPython.display import Image

def getURLBase(string_busca,quantidade_busca, a_partir, numero_pagina):
    return 'http://search.scielo.org/?q={0}&lang=pt&count={1}&from={2}&output=site&format=summary&lang=pt&page={3}'            .format(string_busca, str(quantidade_busca), a_partir, numero_pagina)
   

string_busca = "usabilidade"
quantidade_busca = 117
a_partir = 0
resumos = []
contador = 0

for i in range(1, 3):
    base_url = getURLBase(string_busca,quantidade_busca, a_partir, i)
    a_partir += quantidade_busca + 1
    driver = webdriver.Chrome()
    driver.get(base_url)
    bs_obj = bs(driver.page_source,'html.parser')
    driver.close()

    for elemento in bs_obj.findAll ("div", id=lambda x: x and x.endswith('_pt')):
       resumos.append(elemento.text.strip()) 
    
print(resumos)

#print stopwords.nltk

stopwordsnltk = nltk.corpus.stopwords.words('portuguese')

def removestopwords(texto):
    palavras = []
    for (words) in texto:
        words = words.replace(',', '')
        words = words.replace('.', '')
        words = words.replace(':', '')
        words = words.replace(';', '')
        words = words.replace('-', '')
        words = words.replace('(', '')
        words = words.replace(')', '')
        words = words.replace('é', '')
        words = words.lower()
        semstop = [p for p in words.split() if p not in stopwordsnltk]
        palavras.append((semstop))
    return palavras
    
texto_filtrado = removestopwords(resumos)

dictionary = gensim.corpora.Dictionary(texto_filtrado)

print(removestopwords(resumos))

import operator
ordenado = sorted(dictionary.dfs.items(), key=operator.itemgetter(1), reverse=True)
palavras = ""

print("Palavra - Ocorrência")
for item in ordenado:    
    print("{0} - {1}".format(dictionary[item[0]], item[1]))
    palavras += str(dictionary[item[0]])
    palavras += " "   
from wordcloud import WordCloud    

# Generate a word cloud image
wordcloud = WordCloud().generate(palavras)

import matplotlib.pyplot as plt
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

plt.show()

