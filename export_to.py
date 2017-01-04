#!/usr/bin/env python3
def export_to(archivo_fuente):
    import subprocess as sub
    #archivo_fuente = "py3o_example.docx"
    formato_destino = "pdf"
    #https://help.libreoffice.org/Common/Starting_the_Software_With_Parameters
    #http://dag.wiee.rs/home-made/unoconv/
    p = sub.Popen(["soffice", "--convert-to", formato_destino, archivo_fuente],stdout=sub.PIPE,stderr=sub.PIPE)
    output, errors = p.communicate()
    if errors != b"":
        return str(errors)
    else:
        import re
        output = str(output)
        start = '-> '
        end = ' using'
        nombre_archivo = re.search('%s(.*)%s' % (start, end), output).group(1)
        print(nombre_archivo)
        return nombre_archivo
