import sys
import xml.sax
sys.path.append ('.\Mysax.py')
from Mysax import ManejadorCatalago
parser=xml.sax.make_parser()
parser.setFeature(xml.sax.handler.feature_namespaces,0)            
Handler=ManejadorCatalago()
parser.setContentHandler(Handler)
parser.parse("catalogos.xml")