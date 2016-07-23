#!/usr/bin/python2
import argparse
import string 
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

#Attempt to convert TargetString into an abstract syntax tree


#target.close()
