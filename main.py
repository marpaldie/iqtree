import os
import subprocess


def ejecutar_iqtree(directorio_bin, fichero1, fichero2,numero_replicas,modo = "TESTMERGE"):
    result = []

    # C:/Users/maria/Downloads/iqtree-1.6.12-Windows/bin/iqtree -s Lithobates_concat.txt - q Lithobates_part.txt -m MF+MERGE -alrt 1000
    comando = [directorio_bin,
               '-s',
               fichero1,
               '-q',
               fichero2,
               '-m',
               modo,
               '-alrt',
               str(numero_replicas)
               ]
    print("Esto debe de coincidir con lo que metias tu a mano",' '.join(comando))
    process = subprocess.Popen(comando,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    for line in process.stdout:
        result.append(line)
    errcode = process.returncode
    for line in result:
        print(line.decode('utf-8'))
    if errcode is not None:
        raise Exception('cmd %s failed, see above for details', errcode)


if __name__ == '__main__': #Esto se utiliza formalmente para la parte de ejecución, para que este código no se ejecute si se importa este fichero

    ruta_comando = "C:/Users/maria/Downloads/iqtree-1.6.12-Windows/bin/iqtree" #mete aqui la ruta entera, así no tienes que hacer el cd.
    # directorio_ficheros= 'C:/blabla' #donde tienes los datos

    #mejora los nombres
    fichero1 = "Lithobates_concat.txt"
    fichero2 = "Lithobates_part.txt"

    #alomejor tienes que meter la ruta entera. Utiliza os.path.join para formar las rutas.
    # path_fichero_1 = os.path.join(directorio_ficheros, fichero1)
    # path_fichero_2 = os.path.join(directorio_ficheros, fichero2)

    numero_replicas = 1000

    ejecutar_iqtree(ruta_comando, fichero1,fichero2,numero_replicas)


