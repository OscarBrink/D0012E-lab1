import testPivot
import AlgorithmicRun

from multiprocessing import Process

#compls = testPivot.read_file("out.bin")

compls = [(500000, [[1,4],[5,2],[6,3]]), (250000, [[1,2],[5,6],[8,5]])]

def f(lst, index, res_lst):
    complexity = 1.0 - AlgorithmicRun.calculate_inversion(lst)
    res_lst.append("index" + str(index) \
            + "len list: " + str(len(lst)) \
            + "complexity: " + str(complexity)
    )


tot_list = [["nom compl: " + str(tup[0]) + " len lists: " + str(len(tup[1]))] for tup in compls]
procs = []

for i in range(len(compls)):

    for lst in compls[i][1]:
        tot_list[i].append(["len list: " + str(len(lst))])
        process = Process(target=f, args=(lst, i, tot_list[i][-1]))
        process.start()
        procs.append(process)
        

for p in procs:
    p.join()

print(*tot_list, sep="\n")

#with open("list-complexities.txt", "w") as f:
#    f.write(tot_str)

