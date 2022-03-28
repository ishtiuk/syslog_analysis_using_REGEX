#!/usr/bin/env python3
import sys
import os
import csv

def read_csv_data(file_location):
    file = open(file_location, mode="r", encoding="utf-8")
    csv_read = csv.reader(file)    
    csv_to_data = tuple(data for data in csv_read if len(data) > 0)
    h2 = os.path.basename(file_location)[:-4].replace("_", " ").upper()

    return csv_to_data, h2

def html_data():
    html_format = """
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title></title>
    <style>
        body{
            font-family: arial, sans-serif;
        }
        h2{
            text-align: left
        }
        table{
            text-align: center;
            width: 500px ;
            padding: 3px;
        }
        thead{
            background-color: rgb(241, 241, 241);
        }
        tbody{
            background-color: rgb(209, 209, 209);
        }
        th, td{
            padding: 7px;
        }
    </style>
</head>
<body>"""

    return html_format

def html_generating_algo(csv_location):
    csv_to_data, h2 = read_csv_data(csv_location)
    html_format = html_data() + f"<h2>{h2}</h2>" + '<table border="2">'
    
    for i, data in enumerate(csv_to_data):
        if i == 0:
            html_format += '<thead><tr>'
            for d in data:
                html_format += "<th>" + d + "</th>"
            html_format += "</tr></thead><tbody>"

        elif i > 0:
            html_format += "<tr>"
            for d in data:
                html_format += "<td>" + d + "</td>"
            html_format += "</tr>"
    html_format += "</tbody></table></body>"

    return html_format

def writter_html(csv_location, html_location):
    html_format = html_generating_algo(csv_location)

    with open(html_location, "w", encoding="utf-8") as html_file:
        html_file.write(html_format)

def main(arguments):
    if len(arguments) < 3:
        print("ERROR, missing 3 arguments.\nExiting program...")
        sys.exit(1)
    if arguments[1][-4:] != ".csv":
        print("ERROR. Provide the CSV file as the 3rd argument.\nExiting program...")
        sys.exit(1)
    if arguments[2][-5:] != ".html":
        print("ERROR. Provide the HTML file as the 2nd argument.\nExiting program...")
        sys.exit(1)

    writter_html(arguments[1], arguments[2])
    print("HTML file generated successfully. location: [{}]".format(os.path.abspath(arguments[2])))

main(sys.argv)
