import os.path

import couch
import hbase

# Le os dicoms em C:\Users\Rafael\Documents\POS-DATA-SCIENCE\NoSql\DICOMdataset
pasta = 'C:/Users/Rafael/Documents/POS-DATA-SCIENCE/NoSql/DICOMdataset/'
for dirpath, dirnames, filenames in os.walk(pasta):
    for filename in [f for f in filenames if f.endswith(".dcm")]:
        arquivo = os.path.join(dirpath, filename)
        # Insere os arquivos binarios no HBASE com o retorno da funcao no couch . Campo: SOPInstanceUID
        hbase.insereHbase(couch.insereArquivo(arquivo), arquivo)
