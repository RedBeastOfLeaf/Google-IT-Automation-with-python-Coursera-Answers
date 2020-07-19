#!/usr/bin/env python3

import reports
import emails
import os 
from datetime import date


BASEPATH_SUPPLIER_TEXT_DES = os.path.expanduser('~') + '/supplier-data/descriptions/'
list_text_files = os.listdir(BASEPATH_SUPPLIER_TEXT_DES)

report = []

def process_data(data):
	for item in data:
		report.append("name: {}<br/>weight: {}\n".format(item[0], item[1]))
	return report

text_data = []
for text_file in list_text_files:
	with open(BASEPATH_SUPPLIER_TEXT_DES + text_file, 'r') as f:
		text_data.append([line.strip() for line in f.readlines()])
		f.close()

if __name__ == "__main__":

	summary = process_data(text_data)

	# Generate a paragraph that contains the necessary summary
	paragraph = "<br/><br/>".join(summary)

	# Generate the PDF report
	title = "Processed Update on {}\n".format(date.today().strftime("%B %d, %Y"))
	attachment = "/tmp/processed.pdf"

	reports.generate_report(attachment, title, paragraph)

	# Send the email
	subject = "Upload Completed - Online Fruit Store"
	sender = "automation@example.com"
	receiver = "{}@example.com".format(os.environ.get('USER'))
	body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
	message = emails.generate_email(sender, receiver, subject, body, attachment)
	emails.send_email(message)

