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
TargetStringIntermediate="".join(OutputLines)		
TargetString=TargetStringIntermediate.replace("	","/t")

#Lexer section

#Define tokens with regex
#Review regex later for enhancements

Tokens={'TAG':'(/def|/v|/eg|/!|//|=|==|===|;|/-)','TEXT':'(\w*\s*)+'}

def lex(inputstr):
    tokens=[]
    tokenRegex=[]
    for key in Tokens:
        tokenRegex.append("|(?P<{groupName}>{actualRegex})".format(groupName=key,actualRegex=Tokens[key]))
    tokenRegexstr=("".join(tokenRegex))[1:]
    looker=re.compile(tokenRegexstr)
    while (re.search(
    print tokenRegexstr
    return tokens

new=lex()
#target.close()
