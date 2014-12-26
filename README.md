word-topic-document-representations
===================================

distributed representations of words, topics and documents

author: Li-Qiang Niu, 2014.12.23, NanJing University.

===================================

1.datasets: 
        
        english gigaword 5th edition(https://catalog.ldc.upenn.edu/LDC2011T07), ltw_eng

        s-datasets: 
            #100 000 documents (random select document which's length is more than 1000 characters)
            
            #102644 words (at least occur 5 times)

        b-datasets: 
            #1 000 000 documents

===================================

2.data preprocessing

        source code:

            step1_data_preprocessing.py: select documents from gigaword, filter documents that involve less than 1000 characters 
  
            step2_glda_format.py: filter words that occur less than 5 times

        gibbs lda: http://gibbslda.sourceforge.net/

===================================

3. Using GibbdLDA, we get the topic words of LDA, the file is model-final.twords

===================================

4. 1


