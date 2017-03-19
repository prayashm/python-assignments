# Initialise variables
delimiters = 0
user_text = ''

# Continuously Prompt User for Input
while True:
  lines = input()
  
  # Concatenate User input
  user_text += lines
  
  # Count delimiters: . ? !
  periods = lines.count('.')
  question_marks = lines.count('?')
  exclamatory_marks = lines.count('!')
  
  # Store total number of delimiters in global delimiters count
  delimiters += periods + question_marks + exclamatory_marks
  
  # Check the total number of delimiters
  if delimiters >= 5:
    break

# Display output in terminal as a paragraph
print(user_text)
