import processor


words = processor.text_input()
word_list = processor.text_transform(words)
word_triples = processor.text_triple_maker(word_list)
output = processor.group_count(word_triples)
print(output)
