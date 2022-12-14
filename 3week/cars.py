
#!/usr/bin/env python3

import json
import locale
import sys
import reports
import emails
import os

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  max_revenue = {"revenue": 0}
  # for # TODO: also handle max sales
  total_sales = {"total_sales": 0}
  # for # TODO: also handle most popular car_year
  sales_by_year = {}


  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    #print(item["total_sales"])
    if item["total_sales"] > total_sales["total_sales"]:
      item["max_sales"] = item["total_sales"]
      total_sales = item
    # TODO: also handle most popular car_year
    # generate {"car_year", "total_sales"} dictionary
    # and find max year and max sales
    car_year = item["car"]["car_year"]
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
