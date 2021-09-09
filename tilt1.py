import math
import matplotlib.pyplot as plt

pi = math.pi

def deg_to_rad(theta):
    return theta * (2 * pi) / 360

def rad_to_deg(theta):
    return theta * 360 / (2 * pi)

input = [31,13.1,37.989,18,1800,3,28,13.1,37.989,18,1800,3,31,13.1,37.989,18,1800,4,30,13.1,37.989,18,1800,4,31,13.1,37.989,18,1800,4,30,13.1,37.989,18,1900,5,31,13.1,37.989,18,1900,5,31,13.1,37.989,18,1900,5,30,13.1,37.989,18,1800,4,31,13.1,37.989,18,1800,4,30,13.1,37.989,18,1800,4,31,13.1,37.989,18,1800,3]

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
        #print('Per il mese di ' + mese + ' l\'irradianza per il valore di angolo di tilt pari a ' + str(tilt) + ' vale Ht (kWh / m2) ' + str(ht))
    return risultati

angoli_tilt = []
mesi = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
risultati = {}
angoli = {}
for i in range(12):
    risultati[mesi[i]] = []
    angoli[mesi[i]] = []
for j in range(90):
    angoli_tilt.append(j)
    for k in range(0, len(input), 6):
        input[k + 3] = j
    report = calcolo_irradianza(input)
    for i in range(12):
        risultati[mesi[i]].append(report[i])
        angoli[mesi[i]].append(j)

for i in range(12):
    massimo = 0
    for j in range(len(risultati[mesi[i]])):
        #print('Per il mese di ' + mesi[i] + ' l\'irradianza vale ' + str(risultati[mesi[i]][j]) + ' ad un angolo di tilt di ' + str(angoli[mesi[i]][j]))
        if massimo < risultati[mesi[i]][j]:
            angolo = angoli[mesi[i]][j]
            massimo = risultati[mesi[i]][j]
        
    #print('Per il mese di ' + mesi[i] + ' il massimo dell\'irradianza di tilt avviene per un angolo pari a ' + str(angolo) + ' e la corrispondente irradianza di tilt vale ' + str(round(massimo, 2)))
    plt.subplot(4, 3, int(i + 1))
    plt.plot(list(range(90)), risultati[mesi[i]])
    plt.xlabel('Tilt angles on degrees')
    h = plt.ylabel('GHI tilted (kWh / m2)')
    #h.set_rotation(0)
    plt.title(str(mesi[i]))
    plt.subplots_adjust(wspace = 2, hspace = 2)
plt.show()

    
    
#plt.scatter(x = angoli_tilt, y = medie)
#plt.show()
