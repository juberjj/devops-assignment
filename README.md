#DevOps - Assignment

##Core assignment specification

###The overall objective of this assignment is to automate using Python 3 the process of
creating, launching and monitoring a public-facing web server in the Amazon cloud. The web
server will run on an EC2 instance and display some static content that is stored in S3. The
program that does this must be called run_newwebserver.py
More detailed specification:
..*Firstly, your Python program should create and launch a new Amazon EC2 micro
instance. You must use the boto3 API library to launch from a free tier Amazon Linux
AMI. You will need to have your Amazon credentials in a configuration file
(~/.aws/credentials) and not in the Python code.
..*Ensure your program launches the instance into an appropriate security group (you can
optionally create one programmatically) and is accessible using your SSH key.
..*You should provide a “User Data” start-up script when creating the instance. This
start-up script should apply any required patches to the operating system and then
install the web server (e.g. nginx or Apache).
..*Next, your program should use scp to copy a check_webserver.py script from your
machine to the new instance and then execute this script (using ssh remote command
execution, for example) to check if the webserver process is running. You will need to
use the public IP address or DNS name assigned to your instance to connect to it using
scp or ssh. If check_webserver script indicates that the webserver is not running, then it
should be started up.
..*Another core requirement is that you write Python 3 code to create an S3 bucket and copy
an image up to this bucket. Your webserver main (home) page should then be configured
so that this image will be visible by a browser visiting the website.
..*Your code should perform appropriate error handling (using exceptions) and output
meaningful messages to the user. Implement logging functionality so that details of
what is happening (whether normal or errors) can be written to the console or a file.