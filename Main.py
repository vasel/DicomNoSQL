import os
import os.path
import shutil

import couch


# grava o arquivo em outra pasta, pronto para ser importado no hbase
def copiaArquivo(pastaAntiga, arquivoAntigo, pastaNova, arquivoNovo):
    shutil.copy(os.path.join(pastaAntiga, arquivoAntigo), os.path.join(pastaNova, arquivoNovo))
    # os.rename(os.path.join(pastaNova, arquivoAntigo), os.path.join(pastaNova, arquivoNovo))

# Le os dicoms em C:\Users\Rafael\Documents\POS-DATA-SCIENCE\NoSql\DICOMdataset
pasta = 'C:/Users/Rafael/Documents/POS-DATA-SCIENCE/NoSql/DICOMdataset/'
for dirpath, dirnames, filenames in os.walk(pasta):
    for filename in [f for f in filenames if f.endswith(".dcm")]:
        arquivo = os.path.join(dirpath, filename)
        # Insere os arquivos binarios no HBASE com o retorno da funcao no couch . Campo: SOPInstanceUID
        copiaArquivo(dirpath, filename, 'C:/Users/Rafael/Documents/POS-DATA-SCIENCE/NoSql/hbase-files/',
                     couch.insereArquivo(arquivo))
