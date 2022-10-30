'''
#!/usr/bin/env python3
'''

# Requirement
# A PDF with the name of the fruit and its total weight (in lbs).
# No table
# In the format
'''
name: Apple
weight: 500 lbs

[blank line]

name: Avocado
weight: 200 lbs

[blank line]
'''


from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  report_info = Paragraph(additional_info, styles["BodyText"])
  empty_line = Spacer(1,20)
  report.build([report_title, empty_line, report_info, empty_line])
