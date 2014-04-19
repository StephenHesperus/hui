<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

  <xsl:output method="xml" encoding="utf-8" indent="yes" />

  <!-- Create interface-requires comment node
       and interface element -->
  <xsl:template match="/">
    <xsl:comment>
      <xsl:text>interface-requires </xsl:text>
      <xsl:value-of select="/*[position()=1]/@interface-requires" />
      <xsl:text> </xsl:text>
    </xsl:comment>
    <interface>
      <xsl:variable name="domain" select="/*[position()=1]/@domain" />
      <xsl:if test="$domain">
        <xsl:attribute name="domain">
          <xsl:value-of select="$domain" />
        </xsl:attribute>
      </xsl:if>
    </interface>
  </xsl:template>

</xsl:stylesheet>
