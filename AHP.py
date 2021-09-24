import math
import matplotlib.pyplot as plt
import numpy as np

def prior_matrix(criteria):
    n_comparisons = len(criteria) * (len(criteria) - 1) / 2
    print(n_comparisons)
    prior = []
    for i in range(int(n_comparisons) - 1):
        
        for j in range(i + 1, len(criteria)):
            
            print('Dimmi quanto il criterio ' + criteria[i] + ' è più importante rispetto al criterio ' + criteria[j] + ': ')
            x = int(input())
            if x < 0:
                x = - 1 / x
            prior.append(x)
            
    matrix = []
    count = 0
    for i in range(len(criteria)):
        matrix.append([])
        for j in range(len(criteria) - i - 1):
            matrix[i].insert(len(criteria) - len(criteria) - j - 1, prior[count])
            count += 1
    count = 0
    for i in range(len(criteria)):
        for j in range(i):
            matrix[i].insert(j, 1 / prior[count])
            count += 1
    for i in range(len(criteria)):
        matrix[i].insert(i, 1)
    return [matrix, (np.linalg.eig(matrix))]
    

def alternative_weights(criteria, alternatives):
    min_scale = min(criteria)
    max_scale = max(criteria)
    for value in alternatives.values():
        maximum = max(value)
        for i in range(len(value)):
            value[i] = maximum / value[i]

    vector_dict = {}
    for key, value in alternatives.items():
        maximum = max(value)
        minimum = min(value)
        S_value = (max_scale - min_scale) / (maximum - minimum)
        vector_dict[key] = []
        row = []
        for i in range(len(value)):
            row.append(round(((value[i] - minimum) * S_value + min_scale), 0))
        vector_dict[key].append(row)
    
    matrix_dict = {}
    for key, value in vector_dict.items():
        matrix_dict[key] = []
        
        for el in value:
            
            for i in range(len(el)):
                row = []
                for j in range(len(el)):
                    difference = el[i] - el[j]
                    row.append(difference)
                matrix_dict[key].append(row)
    
    for value in matrix_dict.values():
        for i in range(len(value)):
            for j in range(len(value)):
                if value[i][j] >= 0:
                    value[i][j] += 1
                else:
                    value[i][j] = -1 * (1 / (value[i][j] - 1))

    eigval_dict = {}
    
    for key, values in matrix_dict.items():
        
        eigval_dict[key] = (np.linalg.eig(values))

    return eigval_dict
                    
def criteria_weights(alternatives_matrix):
    return (np.linalg.eig(alternatives_matrix))

def scores(eigval_weights, eigval_prior, lakes):
    scores_dict = {}
    for j in range(len(list(eigval_weights.values())[0][0])):
        score = 0
        count = 0
        for value in eigval_weights.values():
            score += value[0][j] * eigval_prior[count]
            count += 1
        scores_dict[lakes[j]] = score

    return scores_dict


alternatives = {
    'Costi': [395024082,129395197,105442549,133649159,244770581,162229616,49619038,66527441,85672140,96861794,54939294],
    'Distanza': [5257,3530,1016,5403,3350,2826,8344,15223,6578,9864,3130],
    'Potenza': [0.0003781862,0.0018516461,0.0014149475,0.0297391628,0.023400936,0.0352104066,0.075598488,0.0539912264,0.0547799292,0.0597113949,0.1037538728]
}
lakes = ['Poma','Rubino','Baiata','Trinita','Arancio','Giovanni','Comunelli','Disueri','Dirillo','Nicoletti','Villarossa']
criteria = list(alternatives.keys())
results = prior_matrix(criteria)
criteria_matrix = results[0]
eigs_prior = results[1][0]
scales = []
for i in range(len(criteria)):
    for j in range(len(criteria)):
        if criteria_matrix[i][j] >= 1:
            scales.append(criteria_matrix[i][j])
output = scores(alternative_weights(scales, alternatives), eigs_prior, lakes)
print(output)
f = open('output_AHP.csv', 'w')
f.write('Lake,Score_RE,Score_IMG\n')
for key, value in output.items():
    f.write(key)
    f.write(',' + str(round(np.real(value), 2)))
    f.write(',' + str(round(np.imag(value), 2)) + '\n')
f.close()
