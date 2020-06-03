import googleapiclient.discovery
from google.oauth2 import service_account


def G_Service(SERVICE_ACCOUNT_FILE, API_SERVICE_NAME, API_VERSION, *SCOPES):
    # ADD THE  creds/private_key.json{client_email} TO THE FOLDER OR SHEET TO BE APPROVE DBY API
    GSCOPES = [scope for scope in SCOPES[0]]
    print(SCOPES)
    creds = None

    try:
        creds = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=GSCOPES)
        service = googleapiclient.discovery.build(
            API_SERVICE_NAME,
            API_VERSION,
            credentials=creds
        )
        print(API_SERVICE_NAME, 'service created successfully')
        return service
    except Exception as e:
        print(e)
    return None
