def capitalize_sentences(text):
    sentences = text.split('.')
    capitalized_sentences = []
    check_results = []
    for sentence in sentences:
        new_sentence = sentence.strip()  # 去除前后空格
        if new_sentence:  # 确保不是空字符串
            is_correct = new_sentence[0].isupper()
            check_results.append((new_sentence, is_correct))
            capitalized_sentences.append(new_sentence[0].upper() + new_sentence[1:])
        else:
            capitalized_sentences.append('')
    return '. '.join(capitalized_sentences), check_results

text = "hello world. This is a test. another sentence."
print("original sentence:", text)
capitalize_sentence, check_results = capitalize_sentences(text)
for sentence, is_correct in check_results:
    print(f"{sentence}: {is_correct}")
print("capitalized sentence:", capitalize_sentence)