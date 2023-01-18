# gmail_trollhunter

## Repository Description

This program is a desktop application which uses the gmail API to search through recent emails and tell you which email addresses are sending you the most mail. There was no easy way to do this natively since Google doesn't give you any statistics on your emails anymore so I decided to code it up as a project and ended up packaging it neatly into an executable app.

gmail_trollhunter.exe is the main application and can be downloaded and run on its own. The script which generated the application (using PyQt) is called gmail_trollhunter_pyqt.py. This script uses the helper_funcs.py file to interact with the API itself. 

If intending to run locally without using the .exe application using code, download the data folder to the same location as the python scripts to ensure functionality.

## Program Description

The first time you boot up the program and try to enter a value for number of emails to search, your computer will open a browser window asking you to log into your gmail account and allow the application to connect. This will save a token on your computer and the application will appear to crash. Just close out and reopen the application and everything should work.

Essentially just enter the number of emails you want the program to search through (counting from the most recent email received) and then press the button or hit enter. The script will run (time varying on number of emails checked) and when the program has completed a graph will appear listing up to 30 of your BIGGEST TROLLS!!! The y-axis will give how many emails this account sent you and the email addresses themselves are listed accross the x-axis. You can run this as many times as you want, changing the value for emails checked.

 ?? More Features TBD ??

