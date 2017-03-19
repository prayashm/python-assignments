import re

# Take the paragraph as input
paragraph = input()

# Extract Sentences
# Check for delimiters: .?!
intermediate_para = re.sub(r'([.!?])', r'\1\n', paragraph)
sentences = re.split(r'[\n]\s?', intermediate_para)

# Remove last sentence if blank
# Happens when paragraph ends with a proper delimiter
if sentences[-1] == '':
  sentences.pop()

for i, sentence in enumerate(sentences):
  # Add spaces before punctuation symbols
  intermediate_text = re.sub(r"([!\"#$%&()*+,\-./:;<=>?@[\]^_`{|}~])", r' \1', sentence)

  # Tokenise the paragraph
  tokens = intermediate_text.split()
  print('Sentence #{} has {} tokens'.format(i+1, len(tokens)))
