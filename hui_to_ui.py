#!/usr/bin/env python3
"""A script to convert .hui file to .ui file.

A .hui file is an xml file containing Human-readable UI definitions.  A .ui
file is an xml file containing Glade generated UI definitions.  In general, a
.hui will looks like an Android UI definition xml file.

The conversion, or more precisely, xml to xml transformation, is done by using
XSLT.
"""

from lxml import etree


def main():
    """Main function

    Test lxml module and first try of XSLT.
    """
    xslt_root = etree.parse('hui_to_ui.xsl')
    transform = etree.XSLT(xslt_root)

    input_ = etree.parse('input.hui')
    result = transform(input_)

    # get bytes object with xml declaration and xml encoding attribute
    result_b = etree.tostring(result, encoding="utf-8", xml_declaration=True)
    # get unicode str
    result_str = str(result_b, encoding="utf-8") if result_b else ''
    with open('output.ui', 'w') as f:
        f.write(result_str)


if __name__ == '__main__':
    main()
