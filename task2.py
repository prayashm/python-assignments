import re

def sentences_from(paragraph):
    # Extract Sentences
    # Check for delimiters: .?!
    intermediate_para = re.sub(r'([.!?])', r'\1\n', paragraph)
    sentences = re.split(r'[\n]\s?', intermediate_para)

    # Remove last sentence if blank
    # Happens when paragraph ends with a proper delimiter
    if sentences[-1] == '':
        sentences.pop()
    
    return sentences

def tokens_from(sentences):
    all_tokens = []
    for i, sentence in enumerate(sentences):
        # Add spaces before punctuation symbols
        intermediate_text = re.sub(r"([!\"#$%&()*+,\-./:;<=>?@[\]^_`{|}~])", r' \1', sentence)
        
        # Tokenise the paragraph
        tokens = intermediate_text.split()
        all_tokens.append(tokens)
        print('Sentence #{} has {} tokens'.format(i+1, len(tokens)))
    
    return all_tokens
  
# Take the paragraph as input
print('Enter Paragraph:\n')
user_paragraph = input()
extracted_sentences = sentences_from(user_paragraph)
extracted_tokens = tokens_from(extracted_sentences)
