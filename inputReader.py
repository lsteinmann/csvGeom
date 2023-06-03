import csv
import io

from utils.logger import Logger

DELIMITER = ','

class InputReader():

    def __init__(self):
        self.logger = Logger()

    def createDictionary(self, inpFileName):
        with io.open(inpFileName) as impFile:
            dict = []

            reader = csv.DictReader(impFile, delimiter=DELIMITER)
            
            for row in reader:
                dict.append(row)

            return dict
        
    def createDropDownList(self, dict):
        list = []

        for obj in dict:
            if obj['Code'] not in list:
                list.append(obj['Code'])

        return list
        
    def filterByCode(self, dict, code):
        list = []

        for obj in dict:
            if obj['Code'] == code:
                list.append(obj)

        return list
    
    def getAllUniqueIdentifiers(self, lists):
        identifiers = []

        for list in lists:
            identifier = list[0]['Attribut1']

            if identifier not in identifiers:
                identifiers.append(identifier)

        self.logger.info(f"Found {len(identifiers)} unique identifiers: {identifiers}")

        return identifiers
    
    def aggregateByIdentifier(self, inputlists):
        identifiers = self.getAllUniqueIdentifiers(inputlists)

        listMitte = []
        listGanzOben = []

        '''
        ListganzOben
            listMitte1
                listUntenA
                listUntenB
            listMitte2
                listUntenC
            listMitte3
                listuntenD
                listuntenE
        
        '''


        for identifier in identifiers:
            for listUnten in inputlists:
                if identifier == listUnten[0]['Attribut1']:
                    listMitte.append(listUnten)
            listGanzOben.append(listMitte)
            listMitte = []        

        self.logger.info(f"Aggregated geometries: {listGanzOben}")

        return listGanzOben
    
    def splitByIdentifier(self, dict):
        if len(dict) == 0:
            return []
        
        lists = []
        list = []
        lists.append(list)
        
        identifier = dict[0]['Attribut1']

        for obj in dict:
            if obj['Attribut1'] == identifier:
                list.append(obj)
            else:
                identifier = obj['Attribut1']
                list = []
                list.append(obj)
                lists.append(list)

        return lists
