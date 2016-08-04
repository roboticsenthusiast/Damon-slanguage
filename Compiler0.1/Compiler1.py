#!/usr/bin/python2
import re
import argparse
import string 
#Define enum type (Enums aren't in python 2.7, only in python 3)
def enum(**enums):
    return type('Enum', (), enums)

#Compiler input
parser=argparse.ArgumentParser(description="Compile a target file into LaTeX.")
parser.add_argument("InputFileName", metavar="File", default="E1", help="The path to the input file for this compiler")
parser.add_argument("-o", metavar="OutputFile", nargs='?', const="E2", default="None", help="Use this option to specify an output file to write to.")
args=parser.parse_args()
print "Target file to be compiled: "+str(args.InputFileName)
print "Output file: "+str(args.o)

#InputFile processing
OutputLines=[]
target= open(str(args.InputFileName),"r")
Alllines=target.readlines()
for line in Alllines:
	if not str.split(str(line)):
		OutputLines.append(";")
	else:
		OutputLines.append(line.rstrip('\n'))
TargetString="".join(OutputLines)		
print "String to be parsed: {string}".format(string=TargetString)

#Lexer section

#Define tokens with regex
#Review regex later for enhancements

#Contents of Tokens: 'TAG':'(/def|/v|/eg|/!|//|=|==|===|;|/-)','TEXT':'(\w*\s*)+'
#Numbers is a test regex
#Current regex may not work
Tokens={'Numbers':'-?[0-9]+'}
    
#Recursive regex searcher    
def reSearcher(compiledRegex,targetString,startindex,foundList):
    matchString=compiledRegex.search(targetString,startindex)
    if (matchString is None):
        print "No remaining matches"
        print "Results found: {stuff}".format(stuff=foundList)
        return foundList
    else:
        print "1 found!"
        foundList.append(matchString.groupdict().items()[0])
        reSearcher(compiledRegex,targetString,matchString.end(),foundList)
    

#Main lexer function
def lex(inputString):    
    tokens=[]
    tokenRegex=[]
    for key in Tokens:
        tokenRegex.append("|(?P<{groupName}>{actualRegex})".format(groupName=key,actualRegex=Tokens[key]))
    tokenRegexstr=("".join(tokenRegex))[1:]
    looker=re.compile(tokenRegexstr)
    reSearcher(looker,inputString,0,tokens)
    return tokens


new=lex("34-2")

target.close()
