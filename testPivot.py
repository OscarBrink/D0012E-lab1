
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


    
