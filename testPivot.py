
def gen_complex_list(complexity):
    list_size = 100000
    slumped_lists = []
    #Low Complexity
    for i in range(1,10):
        slumped_lists.append(generate_list(0,list_size,list_size,complexity))
    #Test the lists with different pivotChoice
    complex_lists = []
    #Chose random pivot
    for lst in slumped_lists:
        complex_list.append("random_pivot",(quicksort(lst,random_pivot)) )

    #Choose middle pivot
    for lst in slumped_lists:
        complex_list.append("middle_pivot",(quicksort(lst,middle_pivot)) )

    #Choose n median pivot
    for lst in slumped_lists:
        complex_list.append("n_median_pivot",(quicksort(lst,n_median_pivot)) )
    return complex_lists
    

#Lst is the list, x is the number of element
def test_lists():
   
    

    low_complex_lists = gen_complex_list(0)

    medium_complex_list = gen_complex_list(0.5)

    high_compled_list = gen_complex_list(0.95)

    
   
    #medium complexity
    slumped_lists = []
    for i in range(1,10):
        slumped_lists.append(generate_list(0,list_size,list_size,0.5))
    #

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
            compls.append((nominal_comp, lists))

    return compls

 
