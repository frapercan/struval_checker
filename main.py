import os
import subprocess
import sys
import glob

sys.stdout.reconfigure(encoding='utf-8')

dsds_directorios = glob.glob("C:/Users/index/PycharmProjects/struval_checker/DSD/PENCONT/*.xml")
cubos_directorios = glob.glob("C:/Users/index/PycharmProjects/struval_checker/datos/PENCONT/*.xml")
dsds_directorios = [directorio_dsd.replace('\\', '/') for directorio_dsd in dsds_directorios]
cubos_directorios = [directorio_cubo.replace('\\', '/') for directorio_cubo in cubos_directorios]

dsd = dsds_directorios[0]
cubo = cubos_directorios

for cubo in  cubos_directorios:
    result = []
    win_cmd = f'cd C:/Users/index/OneDrive/Documentos/struval_v3_externalaccesstutorial/ExternalAccessTutorial/ & runClient.cmd {cubo} {dsd} SDMX_ML '
    process = subprocess.Popen(win_cmd,
                               shell=True,
                               stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)
    directorio = os.path.join("validation",cubo.split('/')[-2])
    if not os.path.exists(directorio):
        os.makedirs(directorio)
    fichero_dir = os.path.join(directorio,cubo.split('/')[-1].split('+')[0])
    with open(fichero_dir+'.txt', 'w') as file:
        for line in process.stdout:
            # print(line)
            file.write(line.decode("utf-8"))


# for dsd, cubo in zip(dsds_directorios, cubos_directorios):
#     print(dsd)
#     print(cubo)
#     result = []
#     win_cmd = f'cd C:/Users/index/OneDrive/Documentos/struval_v3_externalaccesstutorial/ExternalAccessTutorial/ & runClient.cmd {cubo} {dsd} SDMX_ML '
#     process = subprocess.Popen(win_cmd,
#                                shell=True,
#                                stdout=subprocess.PIPE,
#                                stderr=subprocess.PIPE)
#     directorio = os.path.join("validation",cubo.split('/')[-2])
#     if not os.path.exists(directorio):
#         os.makedirs(directorio)
#     fichero_dir = os.path.join(directorio,cubo.split('/')[-1].split('+')[0])
#     with open(fichero_dir+'.txt', 'w') as file:
#         for line in process.stdout:
#             # print(line)
#             file.write(line.decode("utf-8"))
