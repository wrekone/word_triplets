import word_triplets

words = word_triplets.text_input()
words_list = word_triplets.text_transform(words)
words_triples = word_triplets.text_triple_maker(words_list)
words_triples_count = word_triplets.triple_count(words_triples)
word_triplets.pipe_out(words_triples_count)
# word_triplets.save_output(words_triples_count)  # Refactor after hearing back from Corey on expectations.