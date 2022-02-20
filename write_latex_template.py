from typing import List


m_list = [256, 512, 1024, 2048, 4096]
stdv1_list = [30, 10, 20, 50, 9]
stdv2_list = [42, 15, 24, 63, 7]

def write_latex_tabular(ms: List[int],
                        res1: List[float],
                        res2: List[float],
                        filename: str):
    with open(filename ,'w') as f:
        f.write(r'\begin{tabular }{rrr}' + '\n')
        f.write(r'$m$& 1 stdv & 2 stdv')
        f.write(r'\\\ hline' + '\n')
        for i in range(len(ms)):
            fields = [str(ms[i]),
                '{:.6f}'.format(res1[i]),
                '{:.6f}'.format(res2[i])]
            f.write('&'.join(fields) + r'\\' + '\n')
        f.write(r'\end{tabular}' + '\n')

# write_latex_tabular(ns,res_classic10,"classic_quicksort_equal.tex")
write_latex_tabular(m_list, stdv1_list, stdv2_list,"estimation_error.tex")