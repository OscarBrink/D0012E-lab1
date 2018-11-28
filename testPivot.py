from AlgorithmicRun import run_algorithm_nopr
from quicksort import quicksort
from quicksort import random_pivot
from quicksort import middle_pivot
from quicksort import n_median_pivot
from quicksort import med_3
pivot_function_to_run = None



def runTest(slumped_lists):
    global pivot_function_to_run
    #Low Complexity
    complex_list = []
    #Chose random pivot
    pivot_function_to_run = random_pivot
    for lst in slumped_lists[1]:
        complex_list.append(("random_pivot", run_algorithm_nopr(runTestFunction,lst)) )

    #Choose middle pivot
    pivot_function_to_run = middle_pivot;
                            
    for lst in slumped_lists[1]:
        complex_list.append(("middle_pivot", run_algorithm_nopr(runTestFunction,lst)) )

    #Choose n median pivot
    print("n_median_pivot")
    pivot_function_to_run = med_3
    for lst in slumped_lists[1]:
        complex_list.append(("n_median_pivot", run_algorithm_nopr(runTestFunction,lst)) )
    return complex_list

def runTestFunction(l):
    return quicksort(l,pivot_function_to_run)
        

#Lst is the list, x is the number of element
def test_lists():
   
    list_file = read_file("out2.bin")
    
    list00 = runTest(list_file[0])

    list25 = runTest(list_file[1])

    list50 = runTest(list_file[2])

    list75 = runTest(list_file[3])

    list95 = runTest(list_file[4])

    list1 = runTest(list_file[5])
    
    return [low_complex_list,medium_complex_list,high_complex_list]
    #return {"low_complex_list":low_complex_list,
    #        "medium_complex_list":medium_complex_list,
     #       "high_complex_list":high_complex_list}

def read_file(file_name):
    compls = []
    with open(file_name, "rb") as f:
        len_compls = int.from_bytes(f.read(4), "little")
        for i in range(len_compls):
            nominal_compl = int.from_bytes(f.read(4), "little")
            len_lists = int.from_bytes(f.read(4), "little")
            lists = []
            for j in range(len_lists):
                real_compl = int.from_bytes(f.read(4), "little")
                len_list = int.from_bytes(f.read(4), "little")
                l = []
                for k in range(len_list):
                    l.append(int.from_bytes(f.read(4), "little"))
                lists.append(l)
            compls.append((nominal_compl, lists))

    return compls

def showDick(dick):
    print("-----------------------------------------")
    print("0 % complexity ")
    
    for l in dick[0]:
        print(l[0],"&  $" + str(l[1][0]), "$ & $" + str(l[1][1]),"$ ",end="")
        print(r'\\')
              

    print("-----------------------------------------")
    print("25 % complexity")
    
    for l in dick[1]:
        print(l[0],"&  $" + str(l[1][0]), "$ & $" + str(l[1][1]),"$ ",end="")
        print(r'\\')
              
    print("-----------------------------------------")
    print("50 %")
    
    for l in dick[2]:
        print(l[0],"&  $" + str(l[1][0]), "$ & $" + str(l[1][1]),"$ ",end="")
        print(r'\\')
        
    print("-----------------------------------------")
    print("75 %")
    
    for l in dick[3]:
        print(l[0],"&  $" + str(l[1][0]), "$ & $" + str(l[1][1]),"$ ",end="")
        print(r'\\')

         
    print("-----------------------------------------")
    print("95 %")
    
    for l in dick[4]:
        print(l[0],"&  $" + str(l[1][0]), "$ & $" + str(l[1][1]),"$ ",end="")
        print(r'\\')

    print("-----------------------------------------")
    print("100 %")
    
    for l in dick[5]:
        print(l[0],"&  $" + str(l[1][0]), "$ & $" + str(l[1][1]),"$ ",end="")
        print(r'\\')

showDick(test_lists())
    



        
