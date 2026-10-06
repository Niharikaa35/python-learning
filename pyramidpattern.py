
#   1
#    121
#   12321
#  1234321
# 123454321



# for j in range(1,6,1):
#         for s in range(5,j,-1):
#                 print(" ", end="")
#         for i in range(1,j+1,1):
#                 print(i,end="")
#         for k in range(j-1,0,-1):
#                 print(k, end="")
#         print()



# for j in range(1,6,1):
#     for s in range(5,j,-1):
#             print(" ", end="")

#     for i in range(5,j-1,-1):
#                 print(i, end="")
#     for k in range(5,j-1,-1):
#             print(k-1,end="")
#     print()




for j in range(1,6,1):
            for s in range(1,j,1):
                    print(" ", end="")
            for i in range(5,j-1,-1):
                    print(i,end="")
                    for k in range(j+1,6,1):
                        print(k,end="")
            print()