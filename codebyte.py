import re
def BracketMatcher(strParam):
  opening = re.findall("\(", strParam)
  closing = re.findall("\)", strParam)
  print(opening)
  print(closing)
  if len(opening)==len(closing):
    strParam = 1
  else:
    strParam = 0
  return strParam

# keep this function call here 
print(BracketMatcher("(coder)(byte))"))

print(0.008*125)