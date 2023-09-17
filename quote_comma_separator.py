#!/usr/bin/env python3

# Required parameters:
# @raycast.schemaVersion 1
# @raycast.title quote_comma_separator
# @raycast.mode fullOutput

# Optional parameters:
# @raycast.icon 
# @raycast.packageName Custom Scripts
# @raycast.argument1 { "type": "text", "placeholder": "Input String", "acceptsMultilineText": true }
# @raycast.argument2  { "type": "text", "placeholder": "Quote type", "optional": true }
# @raycast.argument3  { "type": "text", "placeholder": "Separator", "optional": true }

# Documentation:
# @raycast.description Adds Quotes and Commas
# @raycast.author Nikhil
# @raycast.authorURL technikhil.com

import sys

def quote_and_separate(input,quote,separator):
    s = format_separator(separator)
    inputs = cleanup_input(input)
    print(s.join([quote+line.strip()+quote for line in inputs]))
    
def format_separator(separator):
    if separator == "":
        return ","
    elif separator == "\\n":
        return "\n"
    elif separator == "\\t":
        return "\t"    
    return separator
    
def cleanup_input(str):
    lines = str.split('\n')
    return [item for line in lines for item in line.split()]
    
if __name__ == "__main__":
    input = sys.argv[1]
    quote_type = sys.argv[2] if len(sys.argv) > 2 else "'"
    separator = sys.argv[3] if len(sys.argv) > 3 else ","
    quote_and_separate(input, quote_type, separator)

