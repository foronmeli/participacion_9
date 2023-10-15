class DatosMeteorologicos:
    def __init__(self, nombre_archivo:str):
        self.nombre_archivo:str=nombre_archivo

    def procesar_datos(self):
        temperaturas=[]
        humedades=[]
        presiones=[]
        viento=[]
        velocidades=[]
        direcciones=[]
        grados=[]
        with open("datos.txt","r") as archivo:
            for linea in archivo:
                if "Temperatura" in linea:
                    temperaturas.append(float(linea.split(":")[1].strip()))
                    t_pro=sum(temperaturas) / len(temperaturas)
                    return "La temperatura promedio es: ",t_pro
                if "Humedad" in linea:
                    humedades.append(float(linea.split(":")[1].strip()))
                    h_pro=sum(humedades) / len(humedades)
                    return "La humedad promedio es: ",h_pro
                if "Presion" in linea:
                    presiones.append(float(linea.split(":")[1].strip()))
                    p_pro=sum(presiones) / len(presiones)
                    return "La presion promedio es: ",p_pro
                if "Viento" in linea:
                    viento.append(linea.split(":")[1].strip())
                    velocidades.append(float(viento[0].split(",")[0].strip()))
                    v_pro=sum(velocidades) / len(velocidades)
                    direcciones.append(float(viento[0].split(",")[0].strip()))
                    for i in direcciones:
                        if i=="N":
                            grados.append(0)
                        if i=="NNE":
                            grados.append(22.5)
                        if i=="NE":
                            grados.append(45)
                        if i=="ENE":
                            grados.append(67.5)
                        if i=="E":
                            grados.append(90)
                        if i=="ESE":
                            grados.append(112.5)
                        if i=="SE":
                            grados.append(135)
                        if i=="SSE":
                            grados.append(157.5)
                        if i=="S":
                            grados.append(180)
                        if i=="SSW":
                            grados.append(202.5)
                        if i=="SW":
                            grados.append(225)
                        if i=="WSW":
                            grados.append(247.5)
                        if i=="W":
                            grados.append(270)
                        if i=="WNW":
                            grados.append(292.5)
                        if i=="NW":
                            grados.append(315)
                        if i=="NNW":
                            grados.append(337.5)
                        g_pro=sum(grados) / len(grados)
                    for j in direcciones:
                        valor=j-g_pro
                        if valor>mayor:
                            mayor=valor
                        return "La direccion predominante es: ",mayor
                    return "La velocidad promedio es: ",v_pro