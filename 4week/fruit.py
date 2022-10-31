
#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails
import os
from datetime import date


def load_data(filename = None):
    data = [{'name':'mango', 'weight':500, 'description':'delicious', 'image_name':'010.jpeg'},
            {'name':'apple', 'weight':100, 'description':'red', 'image_name':'001.jpeg'},
            {'name':'apple', 'weight':200, 'description':'green', 'image_name':'001.jpeg'}]
    return data



def process_data(data):
    """Analyzes the data, looking for total weight.
    Returns a list of lines that summarize the information.
    """
    # TODO: total weight dictionary {'name': 'total_weight'}
    total_weight = {}
    for item in data:
    # TODO: total_weight

    # Final thought
    # There was no total weight - no need to add up
    # Each item has weight and no multiple items, so no need to add up
        fruit = item["name"]
        if fruit not in total_weight:
            total_weight[fruit] = item["weight"]
        else:
            value = item["weight"]
            #print(value)
            new_value = total_weight[fruit] + value
            #print("sales by year:", sales_by_year[car_year], "new_value:",new_value)
            # #print("value:{} and new_value:{}".format(value, new_value))
            total_weight[fruit] = new_value
            #print(sales_by_year)
    
    summary = []
    for fruit, total_weight in total_weight.items():
        summary.append("name: {}".format(fruit))
        summary.append("weight: {} lbs".format(total_weight))
        summary.append("")

    #return total_weight
    return summary

newline = '\n'
#summary = process_data(data)
#summary = list(''.join(l + 'x' * (n % 3 == 2) for n, l in enumerate(summary)))
#content = "\n".join(summary)
#print(summary)
#print(content)



def main(argv = None):
  """Process the data"""
  data = load_data()
  summary = process_data(data)
  print(summary)

  # TODO: turn this into a PDF report
  
  today = date.today().strftime("%B %d, %Y") # October 30, 2022
  #report = "/tmp/processed.pdf"
  report = "c:\\temp\\processed.pdf"
  report_title = "Processed Update on {}".format(today)
  # Email newline is \n
  #content = "\n".join(summary) : this is for email newline
  
  # reportlab pdf new line is <br/>
  content = "<br/>".join(summary)

  # reports: def generate(filename, title, additional_info, table_data):
  reports.generate(report, report_title, content)


  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Upload Completed - Online Fruit Store"
  #body: The same summary from the PDF, but using \n between the lines
  body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
  #Attachment: Attach the PDF path i.e. generated in the previous step
  attachment = "/tmp/processed.pdf"
  #attachment = "c:\\temp\cars.pdf"

  # emails: def generate(sender, recipient, subject, body, attachment_path):
  message = emails.generate(sender, receiver, subject, body, attachment)
  emails.send(message)


if __name__ == "__main__":
  main(sys.argv)
