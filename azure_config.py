import os
from openai import AzureOpenAI
api_key=os.getenv("AZURE_API_KEY")
endpoint=os.getenv("AZURE_ENDPOINT")
deployment=os.getenv("AZURE_DEPLOYMENT_NAME")
api_version= os.getenv("AZURE_API_VERSION")
client= AzureOpenAI(api_key=api_key,azure_endpoint=endpoint,api_version=api_version)