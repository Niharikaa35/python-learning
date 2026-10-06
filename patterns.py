

# for i in range(1,6,1):
#     print(i,end="")

# for j in range(1,4,1):
#     for i in range(1,6,1):
#         print(i,end="")
#     print()



# for j in range(1,5,1):
#     for i in range(1,6,1):
#         print(i,end="")
#     print()

# 54321,54324,54321,54321

# for j in range(1,4,1):
#     for i in range(5,0,-1):
#         print(i,end="")
#     print()


# for j in range(1,4,1):
#     for i in range(1,6,1):
#         print(i)
#     print()


# 1111,2222,3333,4444,5555

# for j in range(1,6,1):
#     for i in range(1,6,1):
#         print(j,end="")
#     print()

# 54321
# 54321
# 54321
# for j in range(1,6,1):
#     for i in range(5,0,-1):
#         print(i,end="")
#     print()

for j in range(1,6,1):
    for i in range(1,6,1):
        print(i%2==0,end="")
    print()

for j in range(1,6,1):
    for i in range(1,6,1):
        if(j%2==0):{
            print(j,end="")
        }
    print()


# 1
# 12
# 123
# 1234
# 12345

    for j in range(1,6,1):
        for  i in range(1,j+1,1):
            print(i, end="")
        print()

# 1
# 21
# 321
# 4321
# 54321

for j in range(1,6,1):
    for i in range(j,0,-1):
        print("*",end="")
    print()


# 5
# 54
# 543
# 5432
# 54321

for j in range(5,0,-1):
    for i in range(5,j-1,-1):
        print(i,end="")
    print()

for j in range(5,0,-1):
    for i in range(j,5+1,1):
        print(i,end="")
    print()


# 12345
# 12345
# 1234
# 123
# 12
# 1

# for j in range(5,0,-1):
#     for i in range(1,j+1,1):
#         print(i, end="")
#     print()


# for j in range(5,0,1):
#     for i in range(j,j-1,-11):
#         print(i,end="")
#     print()


# 5
# 45
# 345
# 2345
# 12345

# for j in range(1,6,-1):
#      for s in range(5,j-1,-1):
#         print(" " ,end="")
#         for i in range(1,j+1,1):
#             print(i,end="")
#         print()


#  5
#    54
#   543
#  5432
# 54321

# for j in range(5, 0, -1):
#     for s in range(1, j , 1):
#         print(" ", end="")
#     for i in range(5, j-1, -1):
#         print(i, end="")
#     print()


# 12345
# 12345
#  1234
#   123
#    12
#     1
    for j in range(5,0,-1):
        for s in range(5, j, -1):
            print(" " ,end="")
        for i in range(1,j+1,1):
            print(i, end="")
        print()


    for j in range(1,6,1):
        for s in range(1,j,1):
            print(" ", end="")
        for i in range(j,0,-1):
            print("*", end="")
            for k in range(4,j+1,1):
                    print("*", end="")
        print()