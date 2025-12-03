# pip3 install lxml --break-system-packages
from lxml import etree

xml_doc = etree.parse("C:/Users/BryanAlejandroAvilaC/OneDrive - INSTITUTO SUPERIOR DE FORMACION PROFESIONAL CEAC FP/Escritorio/Lenguajes_de_marcas_2do_T/004-Definicion_de_esquemas_y_vocabularios/003-Asociacion_de_descripciones/01-documento_de_referencia.xml")
xsd_doc = etree.parse(r"C:\Users\BryanAlejandroAvilaC\OneDrive - INSTITUTO SUPERIOR DE FORMACION PROFESIONAL CEAC FP\Escritorio\Lenguajes_de_marcas_2do_T\004-Definicion_de_esquemas_y_vocabularios\003-Asociacion_de_descripciones\02-esquemas.xsd")

schema = etree.XMLSchema(xsd_doc)

print(schema.validate(xml_doc))