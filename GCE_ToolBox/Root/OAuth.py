from flask import Flask, jsonify
from azure.identity import ClientSecretCredential
from azure.keyvault.secrets import SecretClient

app = Flask(__name__)

# Set up the ClientSecretCredential using your Azure details
credential = ClientSecretCredential(
    tenant_id="YOUR_TENANT_ID",  
    client_id="YOUR_APP_ID",  # From Service Principal setup
    client_secret="YOUR_CLIENT_SECRET"  # From Service Principal setup
)

# Connect to the Azure Key Vault client. Placeholder vault url
vault_url = "https://myKeyVaultName.vault.azure.net/"
secret_client = SecretClient(vault_url=vault_url, credential=credential)

# Stores user token
@app.route('/store_token/<user_id>/<token>')
def store_token(user_id, token):
    secret_name = f"token_for_{user_id}"  # Make a unique secret name based on user_id
    secret_client.set_secret(secret_name, token)

    # Log the action (in this example, to console)
    print(f"Stored token for user: {user_id} in Azure Key Vault")
    return jsonify(status='success'), 200

@app.route('/retrieve_token/<user_id>')
def retrieve_token(user_id):
    secret_name = f"token_for_{user_id}"
    try:
        retrieved_secret = secret_client.get_secret(secret_name)
        # For security, we won't display the actual token in production logs.
        print(f"Retrieved token for user: {user_id} from Azure Key Vault")
        return jsonify(token=retrieved_secret.value), 200
    except Exception as e:
        return jsonify(error=str(e)), 404

if __name__ == '__main__':
    app.run(debug=True)
