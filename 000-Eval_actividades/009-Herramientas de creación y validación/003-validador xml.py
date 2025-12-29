from lxml import etree

xml_doc = etree.parse("/home/bryan/Documents/Lenguajes_de_marcas_2do_T/000-Eval_actividades/009-Herramientas de creación y validación/001-CV.xml")
xsd_doc = etree.parse("/home/bryan/Documents/Lenguajes_de_marcas_2do_T/000-Eval_actividades/009-Herramientas de creación y validación/002-CV.xsd")

schema = etree.XMLSchema(xsd_doc)

print(schema.validate(xml_doc))