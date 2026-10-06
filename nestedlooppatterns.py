
# *****
# 12345
# *****
# 12345
# *****


# for j in range(1,6,1):
#         for i in range(1,6,1):
#              if (j==1 or j==3 or  j==5):
#                     print("*", end="")
#              else :
#                     print(i, end="")
                    
#         print()



# * * *
# * * *
# * * *
# * * *
# * * *


# for j in range(1,6,1):
#             for i in range(1,6,1):
#                   if (i==1 or i==3 or i==5):
#                         print("*",end="")
#                   else:
#                         print(" ",end="")
              
#             print()




#   *  
#   *  
# *****
#   *  
#   *   

# for  j in range(1,6,1):
#         for i in range(1,6,1):
#                 if(j==3 or i==3):
#                    print("*",end="")
#                 else:
#                    print(" ", end="")
#         print()


# *******
# *     *
# *     *
# *     *
# *     *
# *     *
# *******

# for  j in range(1,8,1):
#     for i  in range(1,8,1):
#                 if(j==1 or j==7 or i==1 or i==7):
#                      print("*", end="")
#                 else:
#                        print(" ",end="")
#     print()


# *  *  *
# *  *  *
# *******
# *  *  *
# *  *  *
# *******


# for j in range(1,8,1):
#     for i in range(1,8,1):
#         if (j==1 or j==4 or j==7 or i==1 or i==4 or i==7):
#                 print("*",end="")
#         else:
#              print(" ", end="")
#     print()


# ****  *
#    *  *
#    *  *
# *  *  *
# *  *   
# *  *   
# *  ****   

# for j in range(1,8,1):
#         for i in range(1,8,1):
#                 if ( i==4 or j==1 and  i<=4 or  j==7  and i>=4 or  i==1 and j>=4 or i==7 and j <=4):
#                      print("*",end="")
#                 else:
#                     print(" ", end="")
#         print()


# *    
#  *   
#   *  
#    * 
#     *

for j in range(1,6,1):
    for i in range(1,6,1):
                if(i==j):
                   print("*", end="")

                else:
                      print(" ", end="")
                
    print()

for j in range(1,6,1):
    for i in range(1,6,1):
                if(j+i==6):
                   print("*", end="")

                else:
                      print(" ", end="")
                
    print()
             

           