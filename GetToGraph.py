
def read_rad(l):
        
        
    #Find first $
    startOp = 0
    for c in l:
        startOp = startOp +1
        if(c == "$"):
            break

    #Find start of size
    startSize = 0
    dollarCount = 0
    for c in l:
        startSize = startSize + 1
        if(c == "$"):
            dollarCount = dollarCount + 1
        if(dollarCount == 4):
            startSize = startSize + 2
            break
                    
    #Get num of Op
    op = ""
    for c in l[startOp:]:
        if(c == " "):
            break
        op = op + c
    #Get Size
    size = ""
    slash = "\\"
    for c in l[startSize:]:
        if(c == slash):
            break
        size = size + c
    
    intOp = int(op)
    intSize = int(size)
    #print("intOp: ", intOp,"intSize: " , intSize)
    return (intOp,intSize)

def printCord(l1,l2):
    i = 0
    outString = ""
    while True:
        
        outString = outString + "(" + str(l1[i])+","+str(l2[i])+")"
    
        i = i + 1
        if(i >= len(l1)):
            break
    return outString

    

def printTable(l1,l2,l3):
    
    print("$100$ & $" + str(l1[0]) + "$ & $" + str(l2[0]) + "$ & $" +str(l3[0])+"$\\\\")
    print("$1000$ & $" + str(l1[1]) + "$ & $" + str(l2[1]) + "$ & $" +str(l3[1])+"$\\\\")
    print("$10000$ & $" + str(l1[2]) + "$ & $" + str(l2[2]) + "$ & $" +str(l3[2])+"$\\\\")
    print("$100000$ & $" + str(l1[3]) + "$ & $" + str(l2[3]) + "$ & $" +str(l3[3])+"$\\\\")
    print("$1000000$ & $" + str(l1[4]) + "$ & $" + str(l2[4]) + "$ & $" +str(l3[4])+"$\\\\")
    
def avrageList(l1,l2):
    
    p2 = 0
    p3 = 0
    p4 = 0
    p5 = 0
    p6 = 0
    i = i +1
    while True:
        if(l2[i] == 100):
            p2 = p2 + l1[i]
        if(l2[i] == 1000):
            p3 = p3 + l1[i]
        if(l2[i] == 10000):
            p4 = p4 + l1[i]
        if(l2[i] == 100000):
            p5 = p5 + l1[i]
        if(l2[i] == 1000000):
            p6 = p6 + l1[i]
        if(i>= 50):
            break
    p2 = p2/5
    p3 = p3/5
    p4 = p4/5
    p5 = p5/5
    p6 = p6/5
    return [p2,p3,p4,p5,p6]
    
def readData(file_name):
    random_0_pivot_op = []
    random_0_pivot_size = []

    middle_0_pivot_op = []
    middle_0_pivot_size = []

    n_median_0_pivot_op = []
    n_median_0_pivot_size = []
#---------------------------------
    random_25_pivot_op = []
    random_25_pivot_size = []

    middle_25_pivot_op = []
    middle_25_pivot_size = []

    n_median_25_pivot_op = []
    n_median_25_pivot_size = []
#---------------------------------
    random_50_pivot_op = []
    random_50_pivot_size = []

    middle_50_pivot_op = []
    middle_50_pivot_size = []

    n_median_50_pivot_op = []
    n_median_50_pivot_size = []
#---------------------------------
    random_75_pivot_op = []
    random_75_pivot_size = []

    middle_75_pivot_op = []
    middle_75_pivot_size = []

    n_median_75_pivot_op = []
    n_median_75_pivot_size = []
#---------------------------------
    random_95_pivot_op = []
    random_95_pivot_size = []

    middle_95_pivot_op = []
    middle_95_pivot_size = []

    n_median_95_pivot_op = []
    n_median_95_pivot_size = []

#---------------------------------
    random_100_pivot_op = []
    random_100_pivot_size = []

    middle_100_pivot_op = []
    middle_100_pivot_size = []

    n_median_100_pivot_op = []
    n_median_100_pivot_size = []
    

    with open(file_name,"r") as f:
        
        line = f.readline()
        while line:
            print(line)
            if "0 % c" in line:
                
                line = f.readline()
                #print("line[:12]",line[:12])
                while "random_pivot" in line:
                    
                    #Får en touple av 
                    op_and_size = read_rad(line)
                    random_0_pivot_op.append(op_and_size[0])
                    random_0_pivot_size.append(op_and_size[1])
                    line = f.readline()
                while "middle_pivot" in line:
                    
                    op_and_size = read_rad(line)
                    middle_0_pivot_op.append(op_and_size[0])
                    middle_0_pivot_size.append(op_and_size[1])
                    line = f.readline()

                while "n_median_pivot" in line:

                    op_and_size = read_rad(line)
                    n_median_0_pivot_op.append(op_and_size[0])
                    n_median_0_pivot_size.append(op_and_size[1])
                    line = f.readline()
            #print("r0op",random_0_pivot_op)
            

            if "25 %" in line:

                line = f.readline()
                while "random_pivot" in line:
                    #Får en touple av 
                    op_and_size = read_rad(line)
                    random_25_pivot_op.append(op_and_size[0])
                    random_25_pivot_size.append(op_and_size[1])
                    line = f.readline()
                while "middle_pivot" in line:
                    
                    op_and_size = read_rad(line)
                    middle_25_pivot_op.append(op_and_size[0])
                    middle_25_pivot_size.append(op_and_size[1])
                    line = f.readline()

                while "n_median_pivot" in line:

                    op_and_size = read_rad(line)
                    n_median_25_pivot_op.append(op_and_size[0])
                    n_median_25_pivot_size.append(op_and_size[1])
                    line = f.readline()

            if "50 %" in line:

                line = f.readline()
                while "random_pivot" in line:
                    #Får en touple av 
                    op_and_size = read_rad(line)
                    random_50_pivot_op.append(op_and_size[0])
                    random_50_pivot_size.append(op_and_size[1])
                    line = f.readline()
                while "middle_pivot" in line:
                    
                    op_and_size = read_rad(line)
                    middle_50_pivot_op.append(op_and_size[0])
                    middle_50_pivot_size.append(op_and_size[1])
                    line = f.readline()

                while "n_median_pivot" in line:

                    op_and_size = read_rad(line)
                    n_median_50_pivot_op.append(op_and_size[0])
                    n_median_50_pivot_size.append(op_and_size[1])
                    line = f.readline()

            if "50 %" in line:

                line = f.readline()
                while "random_pivot" in line:
                    #Får en touple av 
                    op_and_size = read_rad(line)
                    random_50_pivot_op.append(op_and_size[0])
                    random_50_pivot_size.append(op_and_size[1])
                    line = f.readline()
                while "middle_pivot" in line:
                    
                    op_and_size = read_rad(line)
                    middle_50_pivot_op.append(op_and_size[0])
                    middle_50_pivot_size.append(op_and_size[1])
                    line = f.readline()

                while "n_median_pivot" in line:

                    op_and_size = read_rad(line)
                    n_median_50_pivot_op.append(op_and_size[0])
                    n_median_50_pivot_size.append(op_and_size[1])
                    line = f.readline()
            if "75 %" in line:

                line = f.readline()
                while "random_pivot" in line:
                    #Får en touple av 
                    op_and_size = read_rad(line)
                    random_75_pivot_op.append(op_and_size[0])
                    random_75_pivot_size.append(op_and_size[1])
                    line = f.readline()
                while "middle_pivot" in line:
                    
                    op_and_size = read_rad(line)
                    middle_75_pivot_op.append(op_and_size[0])
                    middle_75_pivot_size.append(op_and_size[1])
                    line = f.readline()

                while "n_median_pivot" in line:

                    op_and_size = read_rad(line)
                    n_median_75_pivot_op.append(op_and_size[0])
                    n_median_75_pivot_size.append(op_and_size[1])
                    line = f.readline()
            if "95 %" in line:

                line = f.readline()
                while "random_pivot" in line:
                    #Får en touple av 
                    op_and_size = read_rad(line)
                    random_95_pivot_op.append(op_and_size[0])
                    random_95_pivot_size.append(op_and_size[1])
                    line = f.readline()
                while "middle_pivot" in line:
                    
                    op_and_size = read_rad(line)
                    middle_95_pivot_op.append(op_and_size[0])
                    middle_95_pivot_size.append(op_and_size[1])
                    line = f.readline()

                while "n_median_pivot" in line:

                    op_and_size = read_rad(line)
                    n_median_95_pivot_op.append(op_and_size[0])
                    n_median_95_pivot_size.append(op_and_size[1])
                    line = f.readline()
            if "100 %" in line:

                line = f.readline()
                while "random_pivot" in line:
                    #Får en touple av 
                    op_and_size = read_rad(line)
                    random_100_pivot_op.append(op_and_size[0])
                    random_100_pivot_size.append(op_and_size[1])
                    line = f.readline()
                while "middle_pivot" in line:
                    
                    op_and_size = read_rad(line)
                    middle_100_pivot_op.append(op_and_size[0])
                    middle_100_pivot_size.append(op_and_size[1])
                    line = f.readline()

                while "n_median_pivot" in line:

                    op_and_size = read_rad(line)
                    n_median_100_pivot_op.append(op_and_size[0])
                    n_median_100_pivot_size.append(op_and_size[1])
                    line = f.readline()
                    
            line = f.readline() 
    #random_0_pivot_op = []
    #random_0_pivot_size = []

    #middle_0_pivot_op = []
   # middle_0_pivot_size = []
#
 #   n_median_0_pivot_op = []
  #  n_median_0_pivot_size = []
    #print(len(random_0_pivot_op), len(random_0_pivot_size))
    
    
    printTable(random_100_pivot_op,middle_100_pivot_op,n_median_100_pivot_op)

    
