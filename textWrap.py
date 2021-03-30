

import textwrap 
  
value = """This function wraps the input paragraph such that each line 
in the paragraph is at most width characters long. The wrap method 
returns a list of output lines. The returned list 
is empty if the wrapped 
output has no content."""
  
# Wrap this text. 
wrapper = textwrap.TextWrapper(width=100000) 
  
word_list = wrapper.wrap(text=value) 
  
# Print each line. 
for element in word_list: 
    print(element)