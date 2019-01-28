try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

PDB_URL = 'http://www.rcsb.org/pdb/cgi/export.cgi/' \
          '%s.pdb?format=PDB&compression=None'


def downloadPDB(pdbId, fileName=None):
    if not fileName:
        fileName = '%s.pdb' % pdbId


    response = urlopen(PDB_URL % pdbId)
    data = response.read().decode('utf-8')

    fileObj = open(fileName, 'w')
    fileObj.write(data)
    fileObj.close()

downloadPDB('1A12')

from Modelling import getStructuresFromFile
strucObjs = getStructuresFromFile(fileName)