import word_triplets_processor


words = word_triplets_processor.text_input()
words_list = word_triplets_processor.text_transform(words)
words_triples = word_triplets_processor.text_triple_maker(words_list)
word_triplets_processor.triple_count(words_triples)
