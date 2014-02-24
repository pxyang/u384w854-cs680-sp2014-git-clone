#   Peiran Yang
#   u384w854
#   Program:: pgm56.py
#   sum the value of name
#
#   Psuedo Code
#   Algorthim main
#       name entered by user
#   Pre - None
#   Post - Prints out sum
#
#   Get name from user
#   lower all name's letter
#   split input name
#   sum = 0
#   for loop in length of namelist
#      iname = array of namelist
#       for loop in length of iname
#          sum = sum + value of letter
#   print sum
def main():
   name = input("Enter your name: ")
   name = name.lower()  # make all letter to lower case 
   namelist = name.split() # split the names if theres middle and last
   sum = 0
   for i in range(len(namelist)):
      iname = namelist[i]
      for index in range(len(iname)):
      	if iname[index] == 'a':
      	   sum = sum + 1
      	elif iname[index] == 'b':
      	   sum = sum + 2
      	elif iname[index] == 'c':
      	   sum = sum + 3
      	elif iname[index] == 'd':
      	   sum = sum + 4
      	elif iname[index] == 'e':
      	   sum = sum + 5
      	elif iname[index] == 'f':
      	   sum = sum + 6
      	elif iname[index] == 'g':
      	   sum = sum + 7
      	elif iname[index] == 'h':
      	   sum = sum + 8
      	elif iname[index] == 'i':
      	   sum = sum + 9
      	elif iname[index] == 'j':
      	   sum = sum + 10
      	elif iname[index] == 'k':
      	   sum = sum + 11
      	elif iname[index] == 'l':
      	   sum = sum + 12
      	elif iname[index] == 'm':
      	   sum = sum + 13
      	elif iname[index] == 'n':
      	   sum = sum + 14
      	elif iname[index] == 'o':
      	   sum = sum + 15
      	elif iname[index] == 'p':
      	   sum = sum + 16
      	elif iname[index] == 'q':
      	   sum = sum + 17
      	elif iname[index] == 'r':
      	   sum = sum + 18
      	elif iname[index] == 's':
      	   sum = sum + 19
      	elif iname[index] == 't':
      	   sum = sum + 20
      	elif iname[index] == 'u':
      	   sum = sum + 21
      	elif iname[index] == 'v':
      	   sum = sum + 22
      	elif iname[index] == 'w':
      	   sum = sum + 23
      	elif iname[index] == 'x':
      	   sum = sum + 24
      	elif iname[index] == 'y':
      	   sum = sum + 25
      	elif iname[index] == 'z':
      	   sum = sum + 26
      print("The total numeric value is ", sum)
    
main()  
         	   
