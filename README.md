# Gmail Trollhunter (Python 3.9.x)
<figure>
  <img src="/example/gmail_th_example.png">
  <figcaption><em>Screenshot of program results after analyzing 1000 emails. (Senders' addresses blurred for privacy)</em></figcaption>
</figure>

# Brief Description

Gmail Trollhunter is a desktop application built with Python which uses the gmail API to search through recent emails and tell you which email addresses are sending you the most mail.

# Running the Application

## Installation Instructions

To run the application locally first clone the repository to your personal machine. From the project folder open CMD/Terminal and run the command below:

`pip install --upgrade --user -r requirements.txt`

To open the preconfigured application built with PyQt enter:

'python gmail_trollhunter_pyqt.py' | 'python3 gmail_trollhunter_pyqt.py' | double click `gmail_trollhunter_pyqt.py`

## Program Description

The first time you boot up the program and try to enter a value for number of emails to search, your computer will open a browser window asking you to log into your gmail account and allow the application to connect. This will save a token on your computer and the application will appear to crash. Just close out and reopen the application and everything should work.

###### What's Happening Under the Hood?

> The Gmail API needs to request access to your Gmail account in order to read email information. After authorization, a token is retrieved by the program and saved in the working directory under a folder named '.usersettings'. 

Essentially just enter the number of emails you want the program to search through (counting from the most recent email received) and then press the button or hit enter. The script will run (time varying on number of emails checked) and when the program has completed a graph will appear listing up to 30 of your BIGGEST TROLLS!!! The y-axis will give how many emails this account sent you and the email addresses themselves are listed accross the x-axis. You can run this as many times as you want, changing the value for emails checked.

## Repository Description

This program is an application made to search through recent emails and tell you which email addresses are sending you the most mail. This was created since there was no easy way to do this natively since Google doesn't give you any statistics on your emails anymore so I decided to code it up as a project and ended up packaging it neatly with a GUI into a desktop app.

This could be packaged as a .exe for even easier use but then would require seperate compiled executables for each operating system while the python script should work on most modern computers. 

The script which generates the application (using PyQt) is called gmail_trollhunter_pyqt.py. This script uses the helper_funcs.py file to interact with the API itself. This interaction with the API also requires the authorization information contained in the 'credentials.JSON' file so this must be kept in the same folder as the python scripts.

 ?? More Features TBD ?? - 2/10/23
 
 
 # Troubleshooting
 
**"When I go to authenticate my Google account, I recieve a message saying Access blocked: Gmail TrollHunter has not completed the Google verification process!"**
 
 Ah yes! Thank you for showing interest in the program. Since the program is still in development I have to approve email addresses before they can be connected to the application. Please just shoot me a message and I will add you as a verified tester ASAP. This will give you access to the application.
 
 Alternatively, if you are more tech-savy you can create a credentials.json file with Google Cloud which gives you access to the API. With your own project credentials you would be able to add any Google accounts you want as authorized users. This method is just much more complicated as it requires understanding how to interface with the Google Cloud platform and their API OAuth procedure. More information can be found [here](https://cloud.google.com/docs/authentication).
 
 **If you get an error that says the following:**
 
 'google.auth.exceptions.RefreshError: ('invalid_grant: Bad Request', {'error': 'invalid_grant', 'error_description': 'Bad Request'})'
 
 Try going into the .usersettings folder (contained within the project folder) and delete the token.pickle file. You will have to reauthenticate your Google account the next time you run the application but it should fix the issue. This happens because the token times out after a certain ammount of time.
 
 **"I wanna try to look at another email account..."**
 
 Again, go into the .usersettings folder (contained within the project folder) and delete the token.pickle file. The next time you run the application, you will be able ot authenticate a different Google account.
 

