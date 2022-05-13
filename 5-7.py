
def cout_word(sent_str):
    alphabet_str = 'abcdefghijklmnopqrstuvwxyz'
    let_dict={word:0 for word in alphabet_str}
    words_str = sent_str.lower().split()
    for i in words_str:
        let_dict[i[0]] +=1
    return let_dict

str_example = "Fibonacci numbers are strongly related to the golden ratio: Binet's formula expresses the nth Fibonacci number in terms of n and the golden ratio, and implies that the ratio of two consecutive Fibonacci numbers tends to the golden ratio as n increases."
print(cout_word(str_example))
