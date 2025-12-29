from lxml import etree

xml_doc = etree.parse("/home/bryan/Documents/Lenguajes_de_marcas_2do_T/000-Eval_actividades/008-Asociación de descripciones con documentos/001-documento_de_referencia.xml")
xsd_doc = etree.parse("/home/bryan/Documents/Lenguajes_de_marcas_2do_T/000-Eval_actividades/008-Asociación de descripciones con documentos/002-esquema.xsd")

schema = etree.XMLSchema(xsd_doc)

print(schema.validate(xml_doc))