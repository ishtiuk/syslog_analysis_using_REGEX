# syslog_analysis_using_REGEX
This project's "syslog_analyzer.py" analyzes the "syslog.log" file and generates reports based on Errors and Success messages as a CSV file. Then the automated "csv_to_html.py" script generated an HTML table overview based on those CSV files.

# Introduction
Imagine a company uses a server that runs a service called syslog_analyzer.py, an internal ticketing system. The service logs events to syslog, both when it runs successfully and when it encounters errors.

The service's developers need our help getting some information from those logs so that they can better understand how their software is used and how to improve it. So, we have coded this automation scripts that will process the system log and generate reports based on the information extracted from the log files.

# What does it do?
1. Uses regex to parse a log file

2. Appends and modify values in a dictionary

3. Writes to a file in CSV format

4. Move files to the appropriate directory for use with the CSV->HTML converter


# Using process
1. First of all you need to pass the "syslog.log" or the log file location to the script as command line argument. Like this:
   | "python3 syslog_analyzer.py syslog.log"  or "./syslog_analyzer.py syslog.log" |
   then it'll generate to differnt CSV files named "user_statistics.csv" and "error_message.csv".
 
2. Then pass the CSV files and HTML file names to the "csv_to_html.py" script one by one. Like this:
   | ./csv_to_html.py error_message.csv /var/www/error_message.html |
   | ./csv_to_html.py user_statistics.csv /var/www/error_message.html |      (any HTML file name or path can the passed)
   
   It will make HTML table according to CSV file's datas.
   
3. Then two HTML files will be generated on the given Path as the given named file.

4. Then you can open the HTML files using your browser and visualize the HTML data or table.
