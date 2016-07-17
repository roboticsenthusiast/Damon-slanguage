import argparse
import string 
parser=argparse.ArgumentParser(description="Compile a target file into LaTeX.")

parser.add_argument("Input FileName", metavar="File", default="E1", help="The path to the input file for this compiler")
parser.add_argument("-o", metavar="OutputFile", nargs='?', const="E2", default="None", help="Use this option to specify an output file to write to.")
print parser.parse_args()

#target= open(str(sys.argv[1]),"r")
#target.close()