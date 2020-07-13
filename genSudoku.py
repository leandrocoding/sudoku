# Standalone Generator

import sys, getopt

from solver import generateSudoku
def cmdArgs(argv):
   baseSize=3
   difficulty=2
   amount=1
   outfilename="Sudokus.txt"



   try:
      opts, _ =getopt.getopt(args= argv, shortopts= "hib:d:a:o:")

   except getopt.GetoptError:
      print(f"{sys.argv[0]} -b <baseSize> -d <difficuly> -a <amount>")

   
   for opt,arg in opts:
      if opt == "-h":
         print(f"{sys.argv[0]} -b <baseSize> -d <difficuly> -a <amount>")

         sys.exit()
         
      elif opt=="-b":
         baseSize=int(arg)
      elif opt=="d":
         difficulty=int(arg)
      elif opt=="-a":
         amount=int(arg)
   generator(baseSize,difficulty, amount, outfilename)
      

def askExeptSet(ask,name,deffValue):
   temp=input(ask)
   try:
      value= int(temp)
      
   except:
      print(f"Invalid Input: {temp} using {name} = {deffValue}")
      return deffValue
   return value


def interactiveArgs():
   baseSize=askExeptSet("Please input the disired baseSize.\n Basesize:","BaseSize",3)
   difficulty= askExeptSet("Please input the disired difficulty. Higher Value higher less given Fields \n Difficulty:", "Difficulty",2)
   amount=askExeptSet("Please input the disired amount of fields generated. \n Amount:","Amount",1)
   outfilename=askExeptSet("Please input the disired Filename for the outputfile. Default Sudokus.txt \n Filename:","Filename","Sudokus.txt")
   generator(baseSize,difficulty, amount, outfilename)



def generator(baseSize,difficulty, amount, outfilename):
   count=difficulty*baseSize**2

   with open(outfilename, 'a') as txtfile:

      for _ in range(amount):
         txtfile.write(f"{generateSudoku(baseSize=baseSize, count=count)}\n \n")
   



      
   
         
      




if __name__ == "__main__": 
   if len(sys.argv)>1:
      cmdArgs(sys.argv[1:])
   else:
      interactiveArgs()
