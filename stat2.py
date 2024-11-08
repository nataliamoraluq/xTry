import math
import csv
import matplotlib.pyplot as plt
#
#
# tabla array vacio para los nuevos datos a guardar
tabla = []
#------------------------------------------------------------------
#arrays 
modas = [] #array modas
mediaTot = [] #array media aritmetica
medidasTC = [] #resultados medidas de tendencia central
medidasDV = [] #resultados medidas de variabilidad
#------------------------------------------------------------------      
#muestra con los datos agrupados
datos = [
    30,46,71,66,34,95,50,69,31,55,42,65,75,77,32,87,75,89,31,54,
    63,95,35,86,80,47,90,82,53,58,48,66,78,78,38,82,75,31,80,79,
    48,94,77,64,38,95,46,70,30,60,50,68,34,73,98,98,33,84,98,92,
    65,44,76,96,97,37,81,85,48,61,52,47,77,50,50,49,96,97,82,49,
    33,78,70,48,96,82,40,68,34,62,54,58,54,70,35,69,98,30,88,94,
    35,51,46,92,37,38,80,54,40,39,38,54,77,62,90,39,55,50,67,31,
    68,42,48,62,40,56,94,66,39,45,33,59,78,64,50,35,45,56,69,80,
    69,39,78,65,42,55,95,78,45,56,36,58,80,68,56,36,54,65,96,76,
    74,67,93,66,44,55,82,72,54,80,94,48,34,73,61,46,76,82,64,64,
    89,89,75,66,45,59,71,89,76,74,86,56,44,91,62,79,89,87,79,69
]
#------------------------------------------------------------------
#
# ______________________ TABLA DE DISTRIBUCION DE FRECUENCIA (MAIN FUNCTION)___________________________
def tabla_frecuencia(datos):
    # 1) Se define n (200 datos de la muestra dada) y encontramos el rango
    # 1.a) definimos cals iniciales y variables tales como n. k. xmin ...
    n = len(datos)
    #print(f" muestra de n = {n}")
    # determinamos xmax y xmin
    xMax = max(datos) 
    xMin = min(datos)
    #print(f" Xmin = {xMin} & Xmax = {xMax}")
    #calculamos rango
    rango = max(datos) - min(datos)
    #print(f" Rango R = {rango}")
    #print(rango)
    # 2) Determinamos el número de clases (k) usando la regla de Sturges: k = 1 + 3.33 * log(n)
    k = int(round(1 + 3.33* math.log10(n)))
    #print(f" k = {k}")
    #print(k)
    # 3) Calculamos el ancho de clase (h) ---> h = A (amplitud)
    hAmplitud = math.ceil(rango / k)
    #redondeado al entero mas proximo
    """
    print("-----------------------")
    print(f" A = {hAmplitud}")
    print("-----------------------")"""

    # 4) Se crean los límites de clase

    # límites de clase con intervalos cerrados a la derecha
    # (es decir, el límite superior de cada clase está incluido)
    limites_clase = [xMin + i * hAmplitud for i in range(k+1)]
    # 5) Se llena y genera la tabla de distribuc. de frecuencia
    datosTabla = []
    #aqui tenemos algunas variables inicializadas para los valores a llenar y calc en la tabla
    facum = 0 #frec acumulada
    media = 0 #media
    #
    sumfixi2 = 0 # suma de fi * xi2
    #
    for i in range(k): 
        # frec absoluta / simple
        fi = len([x for x in datos if limites_clase[i] <= x < limites_clase[i + 1]])
        #frec acum
        facum += fi
        # punto medio
        xi = calcPuntoMedio(limites_clase[i], limites_clase[i + 1])
        #media por intervalo
        mediaPerInt = medAritmetica(fi, xi)
        #media
        media += mediaPerInt
        # para la varianza
        sumfixi2 += ((fi * xi) * xi)
        # se llena el espacio donde estaran los datos y calcs de la tabla
        datosTabla.append((limites_clase[i], limites_clase[i + 1], fi, facum, xi, mediaPerInt))
    #print(f"media sumada sin dividir{media}")
    #media aritmetica
    xArit = media / n
    medidasTC.append(xArit) #se agrega a un arreglo de MTC
    """
    print("-----------------------")
    print(f"media arit: {xArit}")"""
    #mediana
    mediana = calcMediana(datosTabla, n, hAmplitud, k)
    medidasTC.append(mediana)
    """
    print("-----------------------")
    print(f"mediana: {mediana}")"""
    #
    calcModas(datosTabla, k, hAmplitud)
    #
    medidasTC.append(modas)
    #
    #
    """
    print("-----------------------")
    print(f" suma de fi * xi2: {sumfixi2}")
    print("-----------------------")"""
    #fixi2 para calc varianza
    fixi2 = sumfixi2
    # varianza y desviac estandar
    s2 = varianza(n, fixi2, xArit)
    s = desvicEstandar(s2)
    #
    """
    print("-----------------------")
    print(f"varianza: {s2} y desviac. estandar: {s}")"""
    medidasDV.append(s2)
    medidasDV.append(s)
    #coeficiente de variacion
    cVariac = coefVariac(s, xArit)
    #percentiles prueba
    """
    p50 = quantiles(datosTabla, 50, 100, n, hAmplitud)
    print(f"P50: {p50}")"""
    #---------------------------------------------------
    # percentil 65
    p65 = quantiles(datosTabla, 65, 100, n, hAmplitud)
    #
    medidasDV.append(p65)
    # cuartiles 1, 2, 3, 4
    q1 = quantiles(datosTabla, 1, 4, n, hAmplitud)
    q2 = quantiles(datosTabla, 2, 4, n, hAmplitud)
    
    q3 = quantiles(datosTabla, 3, 4, n, hAmplitud)
    q4 = quantiles(datosTabla, 4, 4, n, hAmplitud)
    #
    medidasDV.append(q1)
    medidasDV.append(q2)
    medidasDV.append(q3)
    medidasDV.append(q4)
    #deciles 3 y 8
    d3 = quantiles(datosTabla, 3, 10, n, hAmplitud)
    d8 = quantiles(datosTabla, 8, 10, n, hAmplitud)
    medidasDV.append(d3)
    medidasDV.append(d8)
    #rango intercuartil
    rI = calcRangoInterq(q3, q1)
    #print(f"Rango Intercuartil: {rI}")
    medidasDV.append(rI)
    #percentiles para calcular curtosis
    #
    p90 = quantiles(datosTabla, 90, 100, n, hAmplitud)
    p75 = quantiles(datosTabla, 75, 100, n, hAmplitud)
    #
    p25 = quantiles(datosTabla, 25, 100, n, hAmplitud)
    p10 = quantiles(datosTabla, 10, 100, n, hAmplitud)
    #curtosis
    cKurtosis = curtosis(p90, p75, p25, p10)
    #print(f"Curtosis: {cKurtosis}")
    medidasDV.append(cKurtosis)
    #print(f"Coeficiente de Variacion: {cVariac}")
    medidasDV.append(cVariac)
    #indice de asimetria
    aS = indiceAsime(xArit, mediana, s)
    #print(f"Indice de Asimetria: {aS}")
    medidasDV.append(aS)
    #
    #
    return datosTabla
# ==============================================================================
# ______________________________________ MEDIDAS DE TENDENCIA CENTRAL ______________________________________
# ----- MET. CALCULO PUNTO MEDIO(xi = mi)- ------
def calcPuntoMedio(li, ls): 
    mi = round(li + ls) / 2
    return mi
    #se recibe por parametro el li, el ls y se divide entre 2
    #el met retorna el valor de mi que llamamos en el met tabla_frecuencia, y se agrega a la
    #tabla junto con los demas valores
#
#------------------------------------------------------------------
# ----- MET. CALCULO - MEDIA ARITMETICA (x)------
def medAritmetica(fi, xi):
    return fi * xi
def calcMediana(tabla, n, a, k):
    #n = len(datos)
    #por posic
    temp = n/2
    index = 0
    for i in range(k):
        if tabla[i][3] >= temp:
            index = i
            break
    #lista datos mediana
    li = tabla[index][0]
    fi = tabla[index][2]
    Fi = 0 if index < 0 else tabla[index - 1][3]
    #calc mediana
    return li + (((temp - Fi) / fi) * a)
##------------------------------------------------------------------
#
# ----- MET. CALCULO - MODA ------
def calcModas(tabla, k, a):
    moda = 0
    for i in range(k):
        if tabla[i][2] > moda:
            moda = tabla[i][2]
    #
    for i in range(k):
        if tabla[i][2] == moda:
            d1 = tabla[i][2] - (0 if (i<=0) else tabla[i-1][2])
            d2 = tabla[i][2] - (0 if (i>=(len(tabla)-1)) else tabla[i+1][2])
            print(f" d1: {d1}, d2: {d2}")
            if d1== 0 and d2 == 0:
                modas.append(tabla[i][0] + a)
                print(f"Alerta! como d1 y d2 = 0, (0/0+0) el valor de esta op. sera: 1")
            else:
                modas.append(tabla[i][0] + ((d1 / (d1+d2)) * a))
#------------------------------------------------------------------
# ______________________________________ MEDIDAS DE DISPERSION / VARIABILIDAD ____________________________________
# ----- MET. CALCULO - RANGO INTERCUARTIL------
def calcRangoInterq(q3, q1):
    return q3 - q1
#
#------------------------------------------------------------------
# ----- MET. CALCULO - INDICE DE ASIMETRIA------
def indiceAsime(xArit, Med, S):
    #Índice de asimetría; 
    #((3 * (xArit - Med)) / S ) 
    # Si As = 0, {o Si As !=0 then Si As > 0, Si As < 0
    aS = ((3 * (xArit - Med)) / S ) 
    """if aS==0:
        print(f"Indice de Asimetria: {aS}; Presenta distribuc. simetrica de los datos")
    elif aS>0:
        print(f"Indice de Asimetria: {aS}; Presenta distribuc. asimetrica de los datos; sesgo a la der")
    elif aS<0:
        print(f"Indice de Asimetria: {aS}; Presenta distribuc. simetrica de los datos; sesgo a la izq")
    else:
        print("hola")"""
    return aS
#------------------------------------------------------------------
#
# ----- MET. CALCULO - COEFICIENTE DE VARIACION------
def coefVariac(s, xArit):
    return s / xArit
#
#------------------------------------------------------------------
# ----- MET. CALCULO - VARIANZA ------
def varianza(n, fixi2, xAritmetica):
    if fixi2!=0 and n!=0 and xAritmetica!=0:
        s2 =  ((fixi2 / n) - (math.pow(xAritmetica, 2)))
        return s2
    else:
        print('Error! Datos vacios, revisar')
#------------------------------------------------------------------
# ----- MET. CALCULO - DESVIACION ESTANDAR------
def desvicEstandar(s2):
    return math.sqrt(s2)
#
# ----- MET. CALCULO - CUARTILES, DECILES Y PERCENTILES------
def quantiles(tablaDatos, tempk, denom, n,a):
    #sea denom = divisor de nk
    # tempk = k del quantil a calcular
    result = 0
    #
    nk = ((n * tempk)/ denom)
    #print(f"n: {n} + k: {tempk}, nk: {nk}, denom: {denom}")
    for posic, i in enumerate(tablaDatos):
        if i[3] >= nk:
            #print(i[3])
            lik = i[0]
            fi = i[2]
            Fik = 0 if posic==0 else tablaDatos[posic-1][3]
            result = lik + (((nk-Fik) / fi) * a)
            break
    #print(f" I [3]: {i[3]} , lik: {lik}, fi: {fi}, Fi - 1: {Fik}, A: {a}")
    return result
#
# ----- MET. CALCULO - CURTOSIS ------
def curtosis(p90, p75, p25, p10):
    return ((p75 - p25) /(p90 - p10)) * 0.5
#
# ______________________________________ METODOS PARA IMPRIMIR - MOSTRAR ____________________________________
# ----- MET. IMPRIMIR - MUESTRA ------
def printMuestra():
    print("Muestra con datos agrupados (200) no ordenados")
    print(datos)
#
# ----- MET. IMPRIMIR - MODAS------
def printModas(medidasTC):
    for i, mod in enumerate(medidasTC[2]):
        print(f"moda nro {i+1}: {mod}")
#
# ----- MET. IMPRIMIR - MTC------
#
def printMTC(medidasTC):
    print("----------------------------------------")
    print(f"Media aritmetica: {medidasTC[0]}")
    print(f"Mediana: {medidasTC[1]}")
    print(f"Modas:")
    printModas(medidasTC)
#
#
# ----- MET. IMPRIMIR - MDD------
def printMDD(medidasDV):
    print(f"Varianza: {medidasDV[0]}")
    print(f"Desviacion Estandar: {medidasDV[1]}")
    print("----------------------------------------")
    print(f"P65: {medidasDV[2]}")
    print("----------------------------------------")
    print(f"Q1: {medidasDV[3]}")
    print(f"Q2: {medidasDV[4]}")
    """"""
    print(f"Q3: {medidasDV[5]}")
    print(f"Q4: {medidasDV[6]}")
    print("----------------------------------------")
    print(f"D3: {medidasDV[7]}")
    print(f"D8: {medidasDV[8]}")
    print("----------------------------------------")
    print(f"Rango Intercuartil: {medidasDV[9]}")
    print(f"Coeficiente de variacion: {medidasDV[11]}")
    print("----------------------------------------")
    print(f"Indice de Asimetria: {medidasDV[12]}")
    print("----------------------------------------")
    print(f"Curtosis: {medidasDV[10]}")
    print("----------------------------------------")

#
#
def printTable(datos):
    # Calc tabla de distribuc. frecuencia
    tabla = tabla_frecuencia(datos)
    # Mostrar la tabla
    """
    print("tabla posic")
    print(tabla[0][0])"""
    print('-----------------------------------------')
    print('   TABLA DE DISTRIBUC. DE FRECUENCIAS ')
    print("----------------------------------------")
    print("Intervalos| fi | fa | xi | fi * xi |")
    print("----------------------------------------")
    
    for limInf, limSup, frecSim, frecAcum, puntoMedio, mediaPorInt in tabla:
        print(f"[{limInf} - {limSup}) | {frecSim} | {frecAcum} | {puntoMedio}| {mediaPorInt} |")
    print(' ')
    #printMTC()
    """
    print("----------------------------------------")
    print(f"Media aritmetica: {medidasTC[0]}")
    print(f"Mediana: {medidasTC[1]}")
    print(f"Modas:")
    printModas()"""

def menuFreqOpc():
    #menu de opciones
    print(' ')
    print(' [------------------------------------------------------------]')
    print(' ')
    print(' [------------ MENU - DISTRIBUC. DE FRECUENCIAS --------------]')
    print(' [------------------------------------------------------------]')
    print(' ')
    print(' Bienvenido! Elija una de las sig. opciones: ')
    print(' --------------------------------------------')
    print('0.) Mostrar la muestra dada')
    print('1.) Generar tabla de frecuencia con los datos de la muestra')
    print('2.) Mostrar las Medidas de Tendencia Central')
    print('3.) Mostrar las Medidas de Dispersion/Variabilidad')
    print(' ---------------------------------------')
    resp = input('4.) Salir de este menu(volver al MAIN MENU)\n')
    if resp == '0':
        printMuestra()
        print(' --------------------------------------------------------------------')
        opc = input('Desea volver al menu de distribuc. de frecuencias? 1)Si 2)No\n')
        if (opc=='1'):
            menuFreqOpc()
        else:
            print('Cerrando...')
    elif resp == '1':
        printTable(datos)
        print(' --------------------------------------------------------------------')
        opc = input('Desea volver al menu? 1)Si 2)No\n')
        if (opc=='1'):
            menuFreqOpc()
        else:
            print('Cerrando...')
    elif resp == '2': 
        #se llama al met principal para q cargue los datos y calcule las MTC
        modas.clear()
        tabla = tabla_frecuencia(datos)
        #
        print('-----------------------------------------')
        print('   MTC - MEDIDAS DE TENDENCIA CENTRAL ')
        printMTC(medidasTC)
        print(' --------------------------------------------------------------------')
        opc = input('Desea volver al menu? 1)Si 2)No\n')
        if (opc=='1'):
            menuFreqOpc()
        else:
            print('Cerrando...')
    elif resp == '3': 
        #varianza()
        tabla = tabla_frecuencia(datos)
        print('-----------------------------------------')
        print('      MDV - MEDIDAS DE VARIABILIDAD    ')
        printMDD(medidasDV)
        opc = input('Desea volver al menu? 1)Si 2)No\n')
        if (opc=='1'):
            menuFreqOpc()
        else:
            print('Cerrando...')
    elif resp == '4': 
        print('Cerrando...')
    else: print('Err0r')
#

#
"""
main:
    menuFrec
    menuProp:
        vars cuantitav
        vars cualitativas
        probabilidades de las cuantitav
        resultados 

"""
#
def menuPropOpc(age, income, hours):
    #menu de opciones
    print(' ')
    print(' [------------------------------------------------------------]')
    print(' ')
    print(' [------------ MENU - PROBABILIDAD E HIPOTESIS ---------------]')
    print(' [------------------------------------------------------------]')
    print(' ')
    print('0.) Mostrar x')
    print('1.) Generar calcs. por EDAD con los datos de la BD ')
    print('2.) Generar calcs. por SALARIO con los datos de la BD ')
    print('3.) Generar calcs. por HORAS DE TRABAJO con los datos de la BD ')
    print(' ---------------------------------------')
    resp = input('4.) Salir de este menu(volver al MAIN MENU)\n')
    if resp == '0':
        #printMuestra()
        print(' --------------------------------------------------------------------')
        opc = input('Desea volver al menu de probab.? 1)Si 2)No\n')
        if (opc=='1'):
            menuPropOpc(age, income, hours)
        else:
            print('Cerrando...')
    elif resp == '1':
        #tabla_frecuencia(age),
        printTable(age) 
        print(' --------------------------------------------------------------------')
        #NOTA!! agregar un menu para mostrar las MTC y MDD para c/u de estas
        opc = input('Desea volver al menu? 1)Si 2)No\n')
        if (opc=='1'):
            menuPropOpc(age, income, hours)
        else:
            print('Cerrando...')
    elif resp == '2': 
        #se llama al met principal para q cargue los datos y calcule las MTC
        printTable(income)
        #
        print(' --------------------------------------------------------------------')
        opc = input('Desea volver al menu? 1)Si 2)No\n')
        if (opc=='1'):
            menuPropOpc(age, income, hours)
        else:
            print('Cerrando...')
    elif resp == '3': 
        #varianza()
        printTable(hours)
        print('-----------------------------------------')
        opc = input('Desea volver al menu? 1)Si 2)No\n')
        if (opc=='1'):
            menuPropOpc(age, income, hours)
        else:
            print('Cerrando...')
    elif resp == '4': 
        print('Cerrando...')
    else: print('Err0r')
#-------------------------------------------------------------
#main
def main(ageList, incomeList, hoursWkList):
    print(' ')
    print(' _____________________________________________________________')
    print('[                                                             ]')
    print('[_______________ --- STATISTICS II PROGRAM --- _______________]')
    print('[             --- (PROGRAMA DE ESTADIST. II) ---              ]')
    print('[________________________(MAIN MENU)__________________________]')
    print('   Bienvenido! Para comenzar, elija una de las sig. opciones: ')
    print(' --------------------------------------------')
    print('1.) Menu de distribucion de frecuencias ')
    print('2.) Menu de probabilidad e hipotesis ')
    resp = input('3.) Salir del menu\n')
    if resp == '1':
        #printMuestra()
        menuFreqOpc()
        print(' --------------------------------------------------------------------')
        opc = input('Desea volver al menu? 1)Si 2)No\n')
        if (opc=='1'):
            main(ageList, incomeList, hoursWkList)
        else:
            print('Cerrando...')
    elif resp == '2':
        menuPropOpc(ageList, incomeList, hoursWkList)
        print(' --------------------------------------------------------------------')
        opc = input('Desea volver al menu? 1)Si 2)No\n')
        if (opc=='1'):
            main(ageList, incomeList, hoursWkList)
        else:
            print('Cerrando...')
    elif resp == '3':
        print(' ---------------------------------------')
        print('Cerrando...')
    else: print('Err0r')
    
#
# VARS CUANTITATIVAS ----------------------
ageList = []
incomeList = []
hoursWkList = []
# VARS CUALITATIVAS ----------------------
sexList = []
marriedList = []
raceList = []
citizenUSList = []
healthInsuranceList = []
languageList = []
#------------_-------------------------_-----------------
# list(map(smt, smt2))


"""
For the record and the sanity of my mental health, for a piece of mind
im gonna follow the structure in word, and go through
1 to 4 steps of the second menu
Now, for rn
before those 4 step pf the secont Fase (Statis. II - Prob)
im gonna do and end first the graphics AND THEEEEN 
just then, gonna fix up all the mess with the menues? and stuff
and do the rest of em
so id be done with the Fase I and finally
be starting the Fase II
"""
# ------------_-------------------------_-----------------
if __name__ == '__main__': 
    with open("DBdatosProyecto2024.csv", newline='') as csvFile:
        spamreader = csv.reader(csvFile, delimiter=' ', quotechar=' ')
        i = 0
        for row in spamreader:
            if i > 0:
                data = row[0].split(',')
                sexList.append(int(data[0]))
                ageList.append(int(data[1]))
                marriedList.append(data[2])
                incomeList.append(float(data[3]))
                hoursWkList.append(float(data[4]))
                raceList.append(data[5])
                citizenUSList.append(int(data[6]))
                healthInsuranceList.append(int(data[7]))
                languageList.append(int(data[8]))
            i += 1
    #
    """
    tableAge = tabla_frecuencia(ageList)
    tableHoursOW = tabla_frecuencia(hoursWkList)
    tableIncome = tabla_frecuencia(incomeList)"""
    main(ageList, incomeList, hoursWkList)

#