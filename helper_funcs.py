from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import numpy as np
import pickle
import os
import os.path
import email
import matplotlib.pyplot as plt
import sys


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("./data"), relative_path)
  
def getEmails(sortedcounts=None, max_results=500):
    # Define the SCOPES. If modifying it, delete the token.pickle file.
    SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']
    # Variable creds will store the user access token.
    # If no valid token found, we will create one.
    creds = None
  
    # The file token.pickle contains the user access token.
    # Check if it exists
    if os.path.exists('.usersettings/token.pickle'):
  
        # Read the token from the file and store it in the variable creds
        with open('.usersettings/token.pickle', 'rb') as token:
            creds = pickle.load(token)
  
    # If credentials are not available or are invalid, ask the user to log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            print(os.getcwd())
            flow = InstalledAppFlow.from_client_secrets_file(resource_path('credentials.json'), SCOPES)
            creds = flow.run_local_server(port=0)
  
        # Save the access token in token.pickle file for the next run
        if os.path.exists('.usersettings'):
            with open('.usersettings/token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        else:
            os.mkdir('.usersettings')
            with open('.usersettings/token.pickle', 'wb') as token:
                pickle.dump(creds, token)
  
    # Connect to the Gmail API
    service = build('gmail', 'v1', credentials=creds, static_discovery=False)
    if sortedcounts == None:
            # request a list of all the messages
        if max_results <= 500:
            result = service.users().messages().list(maxResults=max_results, userId='me').execute()
            # We can also pass maxResults to get any number of emails. Like this:
            # result = service.users().messages().list(maxResults=200, userId='me').execute()
            messages = result.get('messages')
    
        # messages is a list of dictionaries where each dictionary contains a message id.
        elif max_results > 500:
            result = service.users().messages().list(maxResults=max_results, userId='me').execute()
            messages = result.get('messages')

            while max_results > 500:
                result = service.users().messages().list(maxResults=(max_results-500), userId='me', pageToken=result['nextPageToken']).execute()
                messages = np.append(messages, result.get('messages'))
                max_results -= 500

            # We can also pass maxResults to get any number of emails. Like this:
            # result = service.users().messages().list(maxResults=200, userId='me').execute()


        senders = np.array([])

        # iterate through all the messages
        for msg in messages:
            # Get the message from its id
            txt = service.users().messages().get(userId='me', id=msg['id']).execute()
    
            # Use try-except to avoid any Errors
            try:
                # Get value of 'payload' from dictionary 'txt'
                payload = txt['payload']
                headers = payload['headers']
    
                # Look for Subject and Sender Email in the headers
                for d in headers:
                    if d['name'] == 'From':
                        sender = d['value']
                        sender_short = sender.split()[-1]
    
                # Printing the subject, sender's email and message
                
                #OPTIONAL LINE FOR PROGRESS
                # print("From: ", sender)
                
                senders = np.append(senders, sender_short)
                if np.size(senders) % 100 == 0:
                    print(np.size(senders))

            except:
                pass

            # get unique values and their counts
        unique_vals, counts = np.unique(senders, return_counts=True)
        counts = np.array(counts, dtype=int)
        result = np.rec.fromarrays((unique_vals, counts))
        sortedcounts = result[result['f1'].argsort()]
        sortedcounts = np.flip(sortedcounts, axis=0)
        return sortedcounts
    
    else:
        if np.sum(sortedcounts['f1']) != max_results:
            # request a list of all the messages
            if max_results <= 500:
                result = service.users().messages().list(maxResults=max_results, userId='me').execute()
                # We can also pass maxResults to get any number of emails. Like this:
                # result = service.users().messages().list(maxResults=200, userId='me').execute()
                messages = result.get('messages')
        
            # messages is a list of dictionaries where each dictionary contains a message id.
            elif max_results > 500:
                result = service.users().messages().list(maxResults=max_results, userId='me').execute()
                messages = result.get('messages')

                while max_results > 500:
                    result = service.users().messages().list(maxResults=(max_results-500), userId='me', pageToken=result['nextPageToken']).execute()
                    messages = np.append(messages, result.get('messages'))
                    max_results -= 500

                # We can also pass maxResults to get any number of emails. Like this:
                # result = service.users().messages().list(maxResults=200, userId='me').execute()

            senders = np.array([])

            # iterate through all the messages
            for msg in messages:
                # Get the message from its id
                txt = service.users().messages().get(userId='me', id=msg['id']).execute()
        
                # Use try-except to avoid any Errors
                try:
                    # Get value of 'payload' from dictionary 'txt'
                    payload = txt['payload']
                    headers = payload['headers']
        
                    # Look for Subject and Sender Email in the headers
                    for d in headers:
                        if d['name'] == 'From':
                            sender = d['value']
                            sender_short = sender.split()[-1]
        
                    # Printing the subject, sender's email and message
                    
                    #OPTIONAL LINE FOR PROGRESS
                    # print("From: ", sender)
                    
                    senders = np.append(senders, sender_short)
                    if np.size(senders) % 100 == 0:
                        print(np.size(senders))

                except:
                    pass

                # get unique values and their counts
            unique_vals, counts = np.unique(senders, return_counts=True)
            counts = np.array(counts, dtype=int)
            result = np.rec.fromarrays((unique_vals, counts))
            sortedcounts = result[result['f1'].argsort()]
            sortedcounts = np.flip(sortedcounts, axis=0)
    
            return sortedcounts

        else:
            return sortedcounts

def plot_sorted_counts(x):
    fig, ax = plt.subplots()
    ax.set_title('Your Biggest Trolls!')
    fig.set_size_inches((20,8));
    ax.plot(x['f0'][:30],x['f1'][:30]);
    ax.set_xticklabels(x['f0'][:30],rotation=90);
    fig.subplots_adjust(bottom=0.4)
    # plt.show();
    plt.savefig('sortedcounts.png')
    return fig, ax

# sortedcounts = getEmails(sortedcounts, max_results=300)

# plot_sorted_counts(sortedcounts)