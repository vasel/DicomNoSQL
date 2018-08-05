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
    for de in dataset:
        if type(de.value) is str and de.VR != "OW":
            tags += '{"tag": "%s", "keyword": "%s", "valor":"%s"},' % (str(de.tag), de.keyword, str(de.value))
        # print ('{"tag": "%s", "keyword": "%s", "valor":"%s"},' % (str(de.tag), de.keyword, str(de.value)))
    # print(tags);

    insereCouch(str(dataset.SOPInstanceUID), '{"tags": [ ' + tags[:-1] + ']}')
    return dataset.SOPInstanceUID
