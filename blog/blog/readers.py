# -*- coding: utf-8 -*-
from utilities import read_file

try:
    import markdown
except ImportError:
    print "Markdown seems to be absent on your\
    system"


class MarkdownReader:
    """Markdown parser"""

    
    def read(self, filePath):
        """Return metadatas and content of a markdown file"""
        
        mdContent=read_file(filePath)
        md = markdown.Markdown(extensions = ['meta', 'codehilite'])
        htmlContent=md.convert(mdContent)
        return htmlContent,md.Meta
