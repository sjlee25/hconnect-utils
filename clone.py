'''
    코드설명: HConnect에서 생성한 그룹 내 프로젝트들을 한번에 clone 하도록 도와주는 코드입니다.
    사용방법: 하단 주석을 참고해 올바른 정보를 입력 후 "python3 clone.py" 명령어를 입력하신 뒤, 모두 내려 받은 것 같으면 Enter를 한 번 입력합니다.
            GitLab 토큰은 Settings 내 Access Token 카테고리에서 모든 scopes에 체크 후 생성하실 수 있습니다.
    유의사항: 실행했을 때 HTTP Unauthorized 401 에러 발생 시, 해당 오류가 발생하지 않을 때까지 2~3번 정도 재실행 부탁드립니다.

    코드작성: 2021190101 이성주 (lsj1213m@hanyang.ac.kr)
'''

import json
import os
import shlex
import subprocess
from urllib.request import urlopen

class Cloner:
    def __init__(self):
        self.user_name = ''  # GitLab 아이디
        self.password = ''  # GitLab 비밀번호
        self.private_token = ''  # GitLab 설정 페이지에서 발급받은 토큰 값 입력
        self.group_id = '1011'  # Clone 하고자 하는 그룹 ID (ex: 1011)
        self.root_dir = ''  # 프로젝트들을 clone 할 디렉토리 위치
       
        self.group_url = f'https://hconnect.hanyang.ac.kr/api/v4/projects?private_token={self.private_token}&per_page=1000'
        self.projects = urlopen(self.group_url)
        self.projects_dict = json.loads(self.projects.read().decode())

        os.chdir(self.root_dir)

    def clone(self):
        for project in self.projects_dict:
            if int(project['namespace']['id']) != int(self.group_id):
                continue

            try:
                project_url = project['http_url_to_repo']
                domain_idx = project_url.find('hconnect')
                project_url = project_url[:domain_idx] + f'{self.user_name}:{self.password}@' + project_url[domain_idx:]
                
                command     = shlex.split(f'git clone {project_url}')
                resultCode  = subprocess.Popen(command)  # non-blocking 방식으로 clone 수행

            except Exception as e:
                main_url = 'hconnect.hanyang.ac.kr/'
                url_idx = project_url.find(main_url)
                print(f'Error on {project_url[url_idx + len(main_url):]}: {e.strerror}')

if __name__ == '__main__':
    cloner = Cloner()
    cloner.clone()
