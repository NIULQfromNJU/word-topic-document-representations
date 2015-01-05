word-topic-document-representations
===================================

distributed representations of words, topics and documents

author: Li-Qiang Niu, 2014.12.23, NanJing University.

===================================

1.datasets: 
   
        english gigaword 5th edition(https://catalog.ldc.upenn.edu/LDC2011T07)

        s-datasets: 
            #100 000 documents from subfolder ltw_eng (random select document which's length is more than 1000 characters)
            
            #102644 words (at least occur 5 times)


        b-datasets: 
            #1 000 000 documents from subfolder nyt_eng
            
            #227400 words (at least occur 10 times)

===================================

2.data preprocessing

        source code:

            step1_data_preprocessing.py: select documents from gigaword, filter documents that involve less than 1000 characters 
  
            step2_glda_format.py: filter words that occur less than 5/10 times

        gibbs lda: http://gibbslda.sourceforge.net/

===================================

3.Using GibbdLDA, we get the topic words of LDA, the file is model-final.twords.

        In our experiments, we compare the LDA with our model TW about topic words.

===================================

4. Models:


        word2vec:proposed by Mikolov et al., available at https://code.google.com/p/word2vec/.
                CBOW:


                Skip-gram:
        
        TW:     combining word and topic information
                CBOW:


                Skip-gram:


        LW:     combining word an lemma information
                CBOW:


                Skip-gram:
        
        TW-LW:  combining word, lemma and topic information
                CBOW:


                Skip-gram:
        
        DTW:    combining word, topic and document information
                CBOW:


                Skip-gram:

===================================

5. Experiments
        


        (1).word analogies:
                google dataset:
                        Athens Greece Beijing China
                        ......
                microsoft dataset:
                        good better rough rougher
                        ......
        (2).word similarity:
                WordSim-353:
                        love    sex     6.77
                        ......
                calculateWordSim353.py: after learning word vectors, calculate wordsim353 spearman rank correlation coefficient.
        (3).topic representation:
                compare with LDA results:
                        top N=15 related words or topics:
                        
        (4).sentence representation
                paraphrase identification:
                        
        

===================================

6. Conslusions
        


        we ......
        

===================================


