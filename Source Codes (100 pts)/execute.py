#EXAMPLE: "@LOGIN TWEET A # TWEET ( 4 + 4 ) # @LOGOUT"


LineList = ["@LOGIN", "TWEET", "A", "#", "TWEET", "(", "4", "+", "4", ")", "#", "@LOGOUT"]
for a in range(len(LineList)):
  if LineList[a] == "@LOGIN" or term == "@LOGOUT"
    del LineList[a]
  elif LineList[a] == "TWEET":
    Terms = LineList[a+1:]
    output = ""
    for a in Terms:
      output+=a
    print output
    
elif LineList[a] == "(":
