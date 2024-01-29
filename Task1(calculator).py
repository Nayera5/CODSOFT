while True:
 n1=float(input(""" Welcome to my simple calc ^^
,please enter the first number:  """))
 n2=float(input("Enter the second number:  "))
 op=input("\nChoose the operator you want : [+   -   *   /]  ➡  ")
 if op=='+' :
   print("\n THE RESULT IS :",n1+n2)
 elif op=='-' : 
  print("\n THE RESULT IS :",n1-n2)
 elif op=='*' :
  print("\n THE RESULT IS :",n1*n2)
 elif op=='/' :
   print("\n THE RESULT IS :",n1/n2)
 else:
  print("sorry, invalid choice!")

 x=input("\npress 'enter' to continue or type 'exit' to end \n").lower()
 if x=='exit':
  break