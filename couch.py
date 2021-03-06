import couchdb
import pydicom


user = "admin"
password = "admin"
couchserver = couchdb.Server("http://%s:%s@localhost:5984/" % (user, password))
dbname = "dicom"
db = couchserver[dbname]


# db = couchserver.create(dbname)
# del couchserver[dbname]

def insereCouch(id, tags):
    db[id] = eval(tags)



def insereArquivo(arquivo):
    dataset = pydicom.dcmread(arquivo, stop_before_pixels=False)  # .values()
    tags = ''
    valor = ''
    for de in dataset:
        if de.VR != "OB":
            if de.VR != "OW" and de.VR != 'SQ':
                # modelo anterior tags += '{"tag": "%s", "keyword": "%s", "valor":"%s"},' % (str(de.tag), de.keyword, str(de.value))
                valor = str(de.value).replace("[", "", ).replace("]", "", ).replace("'", "", )

                if (len(de.keyword) > 0):
                    tags += '"%s": "%s",' % (de.keyword, valor)
                else:
                    tags += '"%s": "%s",' % (de.name, valor)
        # print ('{"tag": "%s", "keyword": "%s", "valor":"%s"},' % (str(de.tag), de.keyword, str(de.value)))
    # print(tags);

    insereCouch(str(dataset.SOPInstanceUID), '{' + tags[:-1] + "}")
    #'{"tags": [ ' + tags[:-1] + ']}')


    return dataset.SOPInstanceUID
