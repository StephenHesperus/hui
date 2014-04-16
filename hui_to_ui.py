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

    # Here we use f.write(str(xslt(doc))) instead of xslt(doc).write()
    # because str() will respect the XSLT xsl:output method, while write()
    # doesn't.
    with open('output.ui', 'w') as f:
        f.write(str(result))


if __name__ == '__main__':
    main()
