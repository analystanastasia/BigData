import xml.sax
class ManejadorCatalago (xml.sax.ContentHandler):
    def __init__(self):
        self.Datos = ""
        self.titulo = ""
        self.fecha = ""
        self.autor = ""
        
    def startElement(self,etiqueta,atributos):
        self.Datos = etiqueta
        if etiqueta == "Libro":
            print("*** LIBRO ***")
            isbn=atributos["isbn"]
            print("isbn:",isbn)
    
    def endElement(self,etiqueta):
        if self.Datos == "titulo":
            print("Titulo:",self.titulo)
        elif self.Datos == "fecha":
            print("Fecha:", self.fecha)
        elif self.Datos == "autor":
            print("Autor:", self.autor)
        self.Datos=""
    
    def characters(self, contenido):
        if self.Datos == "titulo":
            self.titulo = contenido
        elif self.Datos == "fecha":
            self.fecha = contenido
        elif self.Datos == "autor":
            self.autor = contenido

