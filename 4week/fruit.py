
#!/usr/bin/env python3

import json
import locale
import sys
#import reports
#import emails
import os


data = [{'name':'mango', 'weight':500, 'description':'delicious', 'image_name':'010.jpeg'},
        {'name':'apple', 'weight':100, 'description':'red', 'image_name':'001.jpeg'},
        {'name':'apple', 'weight':200, 'description':'green', 'image_name':'001.jpeg'}]


def process_data(data):
    """Analyzes the data, looking for total weight.
    Returns a list of lines that summarize the information.
    """
    # TODO: total weight dictionary {'name': 'total_weight'}
    total_weight = {}
    for item in data:
    # TODO: total_weight

    #if item["total_sales"] > total_sales["total_sales"]:
    #  item["max_sales"] = item["total_sales"]
    #  total_sales = item
    # TODO: also handle most popular car_year
    # generate {"car_year", "total_sales"} dictionary
    # and find max year and max sales
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
        summary.append("weight: {}".format(total_weight))
        summary.append("")

    #return total_weight
    return summary

newline = '\n'
summary = process_data(data)
#summary = list(''.join(l + 'x' * (n % 3 == 2) for n, l in enumerate(summary)))
content = "\n".join(summary)
print(summary)
print(content)
'''
    if item["car"]["car_year"] not in sales_by_year:
      #sales_by_year["car_year"] = item["car"]["car_year"]
      #sales_by_year["car_year"] = item["total_sales"]
      #car_year = item["car"]["car_year"]
      sales_by_year[car_year] = item["total_sales"]
      #print(sales_by_year)
    else:
      value = item["total_sales"]
      #print(value)
      new_value = sales_by_year[car_year] + value
      #print("sales by year:", sales_by_year[car_year], "new_value:",new_value)
      #print("value:{} and new_value:{}".format(value, new_value))
      sales_by_year[car_year] = new_value
      #print(sales_by_year)

  #print(sales_by_year)
  max_sales_year = (max(sales_by_year, key=sales_by_year.get))
  max_sales_of_year = sales_by_year[max_sales_year]
  #print(max_sales_year, max_sales_of_year)

  summary = [
    "The {} generated the most revenue: ${}".format(
      format_car(max_revenue["car"]), max_revenue["revenue"]),
  ]

  summary.append("The {} generated the most sales: {}".format(format_car(total_sales["car"]), total_sales["max_sales"]))
  summary.append("The most popular year was {} with {} sales".format(max_sales_year, max_sales_of_year))

  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("car_sales.json")
  #print(data)
  summary = process_data(data)
  print(summary)

  # TODO: turn this into a PDF report

  report = "/tmp/cars.pdf"
  #report = "c:\\temp\\cars.pdf"
  report_title = "Sales summary for last month"
  #content = "\n".join(summary)
  content = "<br/>".join(summary)
  table = cars_dict_to_table(data)

  # reports: def generate(filename, title, additional_info, table_data):
  reports.generate(report, report_title, content, table)

  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"
  #body: The same summary from the PDF, but using \n between the lines
  body = "\n".join(summary)
  #Attachment: Attach the PDF path i.e. generated in the previous step
  attachment = "/tmp/cars.pdf"
  #attachment = "c:\\temp\cars.pdf"

  # emails: def generate(sender, recipient, subject, body, attachment_path):
  message = emails.generate(sender, receiver, subject, body, attachment)
  emails.send(message)

if __name__ == "__main__":
  main(sys.argv)
'''