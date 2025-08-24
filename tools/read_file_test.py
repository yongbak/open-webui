from pydantic import BaseModel, Field
import requests

def upload_file(token, file_path):
    url = 'http://localhost:3000/api/v1/files/'
    headers = {
        'Authorization': f'Bearer {token}',
        'Accept': 'application/json'
    }
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, headers=headers, files=files)
    return response.json()

class Tools:
    class Valves(BaseModel):
        pass

    class UserValves(BaseModel):
        pass

    def __init__(self):
        self.valves = self.Valves()
        self.user_valves = self.UserValves()

    def read_recent_file_info(self,   __files__: Optional[List[Dict[str, Any]]] = None) -> dict:
        """
        최근 업로드된 파일의 정보를 반환하는 함수
        Dict field:
        id, user_id, hash, filename, data, meta

        data: content,
        meta: name, content_type

        Returns:
            dict: 최근 업로드된 파일 정보
        """
        

        return recent_file_info

# Usage
# tools = Tools()
# print("Today's date:", tools.get_current_date())
# print("Current Time:", tools.get_current_time())
