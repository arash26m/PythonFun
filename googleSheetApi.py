from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Replace these with your own Google Sheets document ID and the path to your credentials file
DOCUMENT_ID = 'YOUR_DOCUMENT_ID'
CREDS_FILE = 'PATH_TO_YOUR_CREDS_FILE'

# Load the credentials from the file
creds = Credentials.from_authorized_user_info(info=None, scopes=['https://www.googleapis.com/auth/spreadsheets'])

try:
    # Create a Google Sheets API client
    service = build('sheets', 'v4', credentials=creds)

    # Define the range for the cell to update
    range_name = 'Sheet1!B2'

    # Define the value to insert
    value_input_option = 'USER_ENTERED'
    value = 'hello'

    # Create the value range body for the request
    value_range_body = {
        "range": range_name,
        "values": [[value]],
        "majorDimension": "ROWS"
    }

    # Call the Sheets API to update the cell value
    request = service.spreadsheets().values().update(
        spreadsheetId=DOCUMENT_ID, range=range_name, valueInputOption=value_input_option, body=value_range_body
    )
    response = request.execute()

    print(f'Updated value in {range_name} with {value}')

except HttpError as error:
    print(f'An error occurred: {error}')
    return
