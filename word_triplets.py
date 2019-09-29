import word_triplets_processor


words = word_triplets_processor.text_input()
word_list = word_triplets_processor.text_transform(words)
word_triples = word_triplets_processor.text_triple_maker(word_list)
output = word_triplets_processor.group_count(word_triples)
print(output)
