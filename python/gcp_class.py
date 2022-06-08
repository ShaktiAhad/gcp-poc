from google.cloud import dialogflowcx_v3beta1, storage
from google.oauth2 import service_account
import python.arg as arg

class starting():
  def __init__(self):
    self.credFile = arg.credFile
    self.credentials = service_account.Credentials.from_service_account_file(f'{self.credFile}')
    self.client_options = {"api_endpoint": "asia-northeast1-dialogflow.googleapis.com"}
    self.client = dialogflowcx_v3beta1.AgentsClient(credentials=self.credentials, client_options=self.client_options)
    self.dialogflowcx=dialogflowcx_v3beta1
    self.storage_client = storage.Client(credentials=self.credentials)