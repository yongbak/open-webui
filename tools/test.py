import requests

token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6ImQ1MTRkODU3LWNiZDctNDM4OS1hNjFlLWIwODI1MDFkZjk3YSJ9.40YjWoS775GK3EHaq4nHOLiLEN5PwYdNmdVmk1lcdNE"
def upload_file(token, file_path):
    url = 'http://localhost:8080/api/v1/files/'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, headers=headers, files=files)
    return response.json()

def list_files(token):
    url = 'http://localhost:8080/api/v1/files/'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")

if __name__ == "__main__":   
    files = list_files(token)
    for f in files:
        print(f"ID: {f.get('id')}, Name: {f.get('meta', {}).get('name')}, Size: {f.get('meta', {}).get('size')} bytes, Timestamp: {f.get('created_at')}")
