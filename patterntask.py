# 1
# 22
# 333
# 4444
# 55555

# for j in range(1,6,1):
#     for i in range(1,j+1,1):
#         print(j,end="")
#     print()

# 5
# 44
# 333
# 2222
# 11111

# for j in range(6,0,-1):
#     for i in range(5,j-1,-1):
#         print(j, end="")
#     print()



#       1
#    22
#   333
#  4444
# 55555






#     55555
#  4444
#   333
#    22
#     1

# for j in range(1,6,1):
#     for s in range(5,j,-1):
#         print(" ",end="")
#     for i in range(1,j+1,1):
#         print(j,end="")
#     print()

# 55555
# 55555
# 4444
# 333
# 22
# 1

# for j in range(5,0,-1):
#     for s in range(5,j,1):
#         print(" ",end="")
#     for i in range(1,j+1,1):
#         print(j,end="")
#     print()


#     1
#    222
#   33333
#  4444444
# 555555555


# for j in range(1,6,1):
#     for s in range(5,j,-1):
#         print(" ",end="")
#     for i in range(1,j*2):
#         print(j,end="")
#     print()



# 555555555
#  4444444
#   33333
#    222
#     1


# for j in range(5,0,-1):
#     for s in range(2,j,-1):
#         print(" ",end="")
#     for i in range(1,j*2):
#         print(j,end="")
#     print()


#     5
#    444
#   33333
#  2222222
# 111111111


for j in range(5,0,-1):
    for s in range(5,j,-1):
        print(" ",end="")
        for i in range(1,j-1,1):
            print(j, end="")
        print()

        