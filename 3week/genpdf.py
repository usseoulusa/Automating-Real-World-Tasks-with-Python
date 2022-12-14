'''
#!/usr/bin/env python3
'''

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.piecharts import Pie
from reportlab.lib.pagesizes import inch


path = "C:\\temp\\"

fruit = {
  "elderberries": 1,
  "figs": 1,
  "apples": 2,
  "durians": 3,
  "bananas": 5,
  "cherries": 8,
  "grapes": 13
}

# Generate a pdf document
report = SimpleDocTemplate("c:\\temp\\report.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])
report.build([report_title])

# A list of listss
table_data = []
for k, v in fruit.items():
    table_data.append([k, v])

print(table_data)

# Generate a pdf report
#report_table = Table(data=table_data)
#report.build([report_title, report_table])

# Generate a pdf report in style
# The top left cell is (0, 0) the bottom right is (-1, -1)
# (0,0), (-1,-1) means a whole table
table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
report_table = Table(data=table_data, style=table_style, hAlign="LEFT")

# Another table, different style
table_style = [('GRID', (0,0), (-1,-1), 3, colors.red)]
anoter_report_table = Table(data=table_data, style=table_style, hAlign="CENTER")

# Generate a pdf file
#report.build([report_title, report_table,anoter_report_table])

report_pie = Pie(width=3*inch, height=3*inch)
report_pie.data = []
report_pie.labels = []

for fruit_name in sorted(fruit):
    report_pie.data.append(fruit[fruit_name])
    report_pie.labels.append(fruit_name)

print(report_pie.data)
print(report_pie.labels)

report_chart = Drawing()
report_chart.add(report_pie)

# Generate a pdf file
#report.build([report_title, report_table, report_chart])
report.build([report_title, report_table, anoter_report_table, report_chart])
