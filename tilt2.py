import math
import matplotlib.pyplot as plt
import numpy as np

pi = math.pi

def deg_to_rad(theta):
    return theta * (2 * pi) / 360

def rad_to_deg(theta):
    return theta * 360 / (2 * pi)

lake_poma = [31,13.1,37.989,18,1800,3,28,13.1,37.989,18,1800,3,31,13.1,37.989,18,1800,4,30,13.1,37.989,18,1800,4,31,13.1,37.989,18,1800,4,30,13.1,37.989,18,1900,5,31,13.1,37.989,18,1900,5,31,13.1,37.989,18,1900,5,30,13.1,37.989,18,1800,4,31,13.1,37.989,18,1800,4,30,13.1,37.989,18,1800,4,31,13.1,37.989,18,1800,3]
lake_rubino = [31,12.72,37.89,18,1800,3,28,12.72,37.89,18,1800,3,31,12.72,37.89,18,1800,4,30,12.72,37.89,18,1800,4,31,12.72,37.89,18,1800,4,30,12.72,37.89,18,1900,5,31,12.72,37.89,18,1900,5,31,12.72,37.89,18,1900,5,30,12.72,37.89,18,1800,4,31,12.72,37.89,18,1800,4,30,12.72,37.89,18,1800,4,31,12.72,37.89,18,1800,3]
lake_trinita = [31,12.75,37.70,18,1800,3,28,12.75,37.70,18,1800,3,31,12.75,37.70,18,1800,4,30,12.75,37.70,18,1800,4,31,12.75,37.70,18,1800,4,30,12.75,37.70,18,1900,5,31,12.75,37.70,18,1900,5,31,12.75,37.70,18,1900,5,30,12.75,37.70,18,1800,4,31,12.75,37.70,18,1800,4,30,12.75,37.70,18,1800,4,31,12.75,37.70,18,1800,3]
lake_arancio = [31,13.06,37.63,18,1800,3,28,13.06,37.63,18,1800,3,31,13.06,37.63,18,1800,4,30,13.06,37.63,18,1800,4,31,13.06,37.63,18,1800,4,30,13.06,37.63,18,1900,5,31,13.06,37.63,18,1900,5,31,13.06,37.63,18,1900,5,30,13.06,37.63,18,1800,4,31,13.06,37.63,18,1800,4,30,13.06,37.63,18,1800,4,31,13.06,37.63,18,1800,3]
lake_giovanni = [31,13.77,37.31,18,1800,3,28,13.77,37.31,18,1800,3,31,13.77,37.31,18,1800,4,30,13.77,37.31,18,1800,4,31,13.77,37.31,18,1800,4,30,13.77,37.31,18,1900,5,31,13.77,37.31,18,1900,5,31,13.77,37.31,18,1900,5,30,13.77,37.31,18,1800,4,31,13.77,37.31,18,1800,4,30,13.77,37.31,18,1800,4,31,13.77,37.31,18,1800,3]
lake_villarosa = [31,14.21,37.58,18,1800,3,28,14.21,37.58,18,1800,3,31,14.21,37.58,18,1800,4,30,14.21,37.58,18,1800,4,31,14.21,37.58,18,1800,4,30,14.21,37.58,18,1900,5,31,14.21,37.58,18,1900,5,31,14.21,37.58,18,1900,5,30,14.21,37.58,18,1800,4,31,14.21,37.58,18,1800,4,30,14.21,37.58,18,1800,4,31,14.21,37.58,18,1800,3]
lake_nicoletti = [31,14.34,37.61,18,1800,3,28,14.34,37.61,18,1800,3,31,14.34,37.61,18,1800,4,30,14.34,37.61,18,1800,4,31,14.34,37.61,18,1800,4,30,14.34,37.61,18,1900,5,31,14.34,37.61,18,1900,5,31,14.34,37.61,18,1900,5,30,14.34,37.61,18,1800,4,31,14.34,37.61,18,1800,4,30,14.34,37.61,18,1800,4,31,14.34,37.61,18,1800,3]
lake_comunelli = [31,14.16,37.16,18,1800,3,28,14.16,37.16,18,1800,3,31,14.16,37.16,18,1800,4,30,14.16,37.16,18,1800,4,31,14.16,37.16,18,1800,4,30,14.16,37.16,18,1900,5,31,14.16,37.16,18,1900,5,31,14.16,37.16,18,1900,5,30,14.16,37.16,18,1800,4,31,14.16,37.16,18,1800,4,30,14.16,37.16,18,1800,4,31,14.16,37.16,18,1800,3]
lake_disueri = [31,14.29,37.20,18,1800,3,28,14.29,37.20,18,1800,3,31,14.29,37.20,18,1800,4,30,14.29,37.20,18,1800,4,31,14.29,37.20,18,1800,4,30,14.29,37.20,18,1900,5,31,14.29,37.20,18,1900,5,31,14.29,37.20,18,1900,5,30,14.29,37.20,18,1800,4,31,14.29,37.20,18,1800,4,30,14.29,37.20,18,1800,4,31,14.29,37.20,18,1800,3]
lake_baiata = [31,12.58,37.99,18,1800,3,28,12.58,37.99,18,1800,3,31,12.58,37.99,18,1800,4,30,12.58,37.99,18,1800,4,31,12.58,37.99,18,1800,4,30,12.58,37.99,18,1900,5,31,12.58,37.99,18,1900,5,31,12.58,37.99,18,1900,5,30,12.58,37.99,18,1800,4,31,12.58,37.99,18,1800,4,30,12.58,37.99,18,1800,4,31,12.58,37.99,18,1800,3]
lake_dirillo = [31,14.69,37.12,18,1800,3,28,14.69,37.12,18,1800,3,31,14.69,37.12,18,1800,4,30,14.69,37.12,18,1800,4,31,14.69,37.12,18,1800,4,30,14.69,37.12,18,1900,5,31,14.69,37.12,18,1900,5,31,14.69,37.12,18,1900,5,30,14.69,37.12,18,1800,4,31,14.69,37.12,18,1800,4,30,14.69,37.12,18,1800,4,31,14.69,37.12,18,1800,3]

efficienza_modulo = 0.15 * 0.78

lakes_info = {
'lake_poma': lake_poma,
'lake_rubino': lake_rubino,
'lake_trinita': lake_trinita,
'lake_arancio': lake_arancio,
'lake_giovanni': lake_giovanni,
'lake_villarosa': lake_villarosa,
'lake_nicoletti': lake_nicoletti,
'lake_comunelli': lake_comunelli,
'lake_disueri': lake_disueri,
'lake_baiata': lake_baiata,
'lake_dirillo': lake_dirillo
}

lakes_surfaces = {
'lake_poma': 2852946,
'lake_rubino': 934519,
'lake_trinita': 965242,
'lake_arancio': 1767784,
'lake_giovanni': 1171656,
'lake_villarosa': 396783,
'lake_nicoletti': 699556,
'lake_comunelli': 358359,
'lake_disueri': 480475,
'lake_baiata': 761528,
'lake_dirillo': 618742
}

lakes_results = {
'lake_poma': {},
'lake_rubino': {},
'lake_trinita': {},
'lake_arancio': {},
'lake_giovanni': {},
'lake_villarosa': {},
'lake_nicoletti': {},
'lake_comunelli': {},
'lake_disueri': {},
'lake_baiata': {},
'lake_dirillo': {}
}

lakes_max_irradiances = {
'lake_poma': {},
'lake_rubino': {},
'lake_trinita': {},
'lake_arancio': {},
'lake_giovanni': {},
'lake_villarosa': {},
'lake_nicoletti': {},
'lake_comunelli': {},
'lake_disueri': {},
'lake_baiata': {},
'lake_dirillo': {}
}


hsc = 1.353

def calcolo_irradianza(lst):
    risultati = []
    length = len(lst)
    for i in range(0, length, 6):
        n = lst[i]
        latitudine = lst[i + 2]
        longitudine = lst[i + 1]
        tilt = lst[i + 3]
        Irradianza = lst[i + 4]
        GHI = lst[i + 5]
        delta = 23.45 * math.sin(deg_to_rad(360 * (284 + n) / 365))
        rb = (math.sin(deg_to_rad(latitudine - tilt)) * math.sin(deg_to_rad(delta))) + math.cos(deg_to_rad(latitudine - tilt)) * math.cos(deg_to_rad(delta)) * math.cos(deg_to_rad(longitudine)) / (math.sin(deg_to_rad(latitudine)) * math.sin(deg_to_rad(delta)) + math.cos(deg_to_rad(latitudine)) * math.cos(deg_to_rad(longitudine)) * math.cos(deg_to_rad(delta)))
        rd = (1 + math.cos(deg_to_rad(tilt))) / 2
        rr = (1 - math.cos(deg_to_rad(tilt))) / 2
        hs = rad_to_deg(math.acos(-1 * math.tan(deg_to_rad(latitudine)) * math.tan(deg_to_rad(delta))))
        ho = ((hsc / pi) * 24) * (1 + 0.033 * math.cos(deg_to_rad(360 * n) / 365)) * ((math.cos(deg_to_rad(latitudine)) * math.cos(deg_to_rad(delta)) * math.sin(deg_to_rad(hs))) + ((((2 * pi) / 360) * hs) * math.sin(deg_to_rad(latitudine)) * math.sin(deg_to_rad(delta))))
        kt = Irradianza / ho
        hd = GHI * ((0.775 + (0.00653 * (hs - 90))) - (0.505 + (0.00455 * (hs - 90))) * (math.cos(deg_to_rad(115 * kt - 103))))
        hdif = GHI * (1 - (1.13 * kt))
        hb = (GHI - hd)
        roh = 0.5
        hr = GHI * roh
        ht = hr * rr + hb * rb + hd * rd
        risultati.append(ht)
        #print('Per il mese di ' + mese + ' l\'irradianza per il valore di angle_max di tilt pari a ' + str(tilt) + ' vale Ht (kWh / m2) ' + str(ht))
    return risultati


mesi = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']



def resulting_irradiance(string):
    input = lakes_info[string]
    angoli_tilt = []
    risultati = {}
    angoli = {}
    for i in range(12):
        risultati[mesi[i]] = []
        angoli[mesi[i]] = []
        lakes_results[string][mesi[i]] = []
    for j in range(90):
        angoli_tilt.append(j)
        for k in range(0, len(input), 6):
            input[k + 3] = j
        report = calcolo_irradianza(input)
        for i in range(12):
            risultati[mesi[i]].append(report[i])
            lakes_results[string][mesi[i]].append(report[i])
            angoli[mesi[i]].append(j)

    for i in range(12):
        maximum = 0
        for j in range(len(risultati[mesi[i]])):
            #print('Per il mese di ' + mesi[i] + ' l\'irradianza vale ' + str(risultati[mesi[i]][j]) + ' ad un angle_max di tilt di ' + str(angoli[mesi[i]][j]))
            if maximum < risultati[mesi[i]][j]:
                angle_max = angoli[mesi[i]][j]
                maximum = risultati[mesi[i]][j]
        
        lakes_max_irradiances[string][mesi[i]] = (angle_max, maximum)
        
    
def print_results(string):

    for i in range(12):
        
        print('The maximum value of tilted solar irradiance on the ' + string + ' for the month ' + mesi[i] + ' happens at a tilt angle ' + str(lakes_max_irradiances[mesi[i]][0]) + ' degrees and the corresponding solar irradiance is ' + str(round(lakes_max_irradiances[mesi[i]][1], 2)))
        
        plt.subplot(4, 3, int(i + 1))
        plt.plot(list(range(90)), lakes_results[string][mesi[i]])
        plt.xlabel('Tilt angles on degrees')
        h = plt.ylabel('GHI tilted (kWh / m2)')
        h.set_rotation(90)
        plt.title(str(mesi[i]))
        plt.subplots_adjust(wspace = 2, hspace = 2)
    plt.show()

lakes = ['lake_poma', 'lake_rubino', 'lake_trinita', 'lake_arancio', 'lake_giovanni', 'lake_villarosa', 'lake_nicoletti', 'lake_comunelli', 'lake_disueri', 'lake_baiata', 'lake_dirillo']
lakes_labels = ['poma', 'rubino', 'trinita', 'arancio', 'giovanni', 'villarosa', 'nicoletti', 'comunelli', 'disueri', 'baiata', 'dirillo']
#print_results(string)
for lake in lakes:
    resulting_irradiance(lake)

for i in range(len(mesi)):
    ax = plt.subplot(4, 3, i + 1)
    y_values = []
    for j in lakes_max_irradiances.values():
        y_values.append(j[mesi[i]][0])
    plt.bar(range(len(lakes)), y_values)
    #plt.xlabel('lakes')
    h = plt.ylabel('Max Tilt angles\n' + mesi[i])
    h.set_rotation(90)
    #plt.title('Maximum tilt angles for ' + mesi[i])
    ax.set_xticks(range(len(list(lakes_max_irradiances.keys()))))
    ax.set_xticklabels(lakes_labels, rotation = 'vertical')
    
    plt.subplots_adjust(hspace = 5.3, wspace = 1)

for key, value in lakes_max_irradiances.items():
    print(key + ':')
    for i in range(len(mesi)):
        print('     Month ' + mesi[i] + ', angle max: ' + str(value[mesi[i]][0]) + ', tilted GHI: ' + str(round(value[mesi[i]][1], 2)))

plt.show()

f = open('output.csv', 'w')
f.write('lake,Month,tilt_max,surface(m2),tilted_ghi_max(kWh/m2),Power(MW)\n')
for key, value in lakes_max_irradiances.items():
    for month, values in value.items():
        f.write(key)
        f.write(',' + month)
        f.write(',' + str(values[0]))
        f.write(',' + str(lakes_surfaces[key]))
        f.write(',' + str(round(values[1], 2)))
        f.write(',' + str(round(lakes_surfaces[key] * efficienza_modulo * values[1] * 0.001, 2)) + '\n')
f.close()
