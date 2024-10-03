def arrange_words_by_length(sentence):
    words = sentence.split()
    words.sort(key=len)
    return ' '.join(words)

input_sentence =input() 
output_sentence = arrange_words_by_length(input_sentence)
print(output_sentence)  
