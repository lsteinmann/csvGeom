from enum import Enum

class OutputType(Enum):
    POINT = "Point"
    LINE = "LineString"
    POLYGON = "Polygon"
    MULTI_POINT = "MultiPoint"
    MULTI_LINE = "MultiLineString"
    MULTI_POLYGON = "MultiPolygon"

    def getGeoJSONCase(self):
        return self.value

    def getUpperCase(self):
        return self.value.upper()
    
    def getLowerCase(self):
        return self.value.lower()
    
    def getTitleCase(self):
        return self.value.title()
    
    def getAsSuffix(self):
        return "_" + self.getLowerCase()
    