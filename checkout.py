'''
    코드설명: HConnect에서 clone 받은 프로젝트들을 특정 시점 이전의 버전으로 체크아웃 하도록 도와주는 코드입니다.
    사용방법: 하단 주석을 참고해 올바른 정보를 입력 후, "python3 checkout.py" 명령어를 입력해 주시면 됩니다.
    유의사항: 지정한 시점 이전에 수행된 커밋이 없는 레포지토리에서는 체크아웃이 의도대로 새로 수행되지 않습니다.
            (이 경우 "HEAD의 현재 위치는 ..." 메시지가 출력되지 않으므로,
            해당 시점 이전에 커밋 내역이 없었거나 레포지토리가 비어있는지 별도로 확인해 주셔야 합니다.)
    
    코드작성: 2021190101 이성주 (lsj1213m@hanyang.ac.kr)
'''

import os
import subprocess

class Checkouter():
    def __init__(self):
        self.class_year = '2021'                        # 수업 연도     (ex: 2021)
        self.class_num = 'ite1014'                      # 수업 학수번호  (ex: ite1014)
        self.deadline = '2021-03-24 00:00 UTC+9'        # 해당 시각 이전 버전들 중에서 최신으로 체크아웃
        self.root_dir = ''  # Clone 받은 프로젝트들이 저장된 로컬 디렉토리
        
        self.class_num = self.class_num.lower()
        if self.root_dir[-1] != '/':
            self.root_dir += '/'
        self.directories = os.listdir(self.root_dir)

    def checkout(self):
        for dir in self.directories:
            # 각 프로젝트 디렉토리명 포맷은 '{연도}_{학수번호}_{학생 학번}'
            if dir.find(f'{self.class_year}_{self.class_num}_') < 0:
                continue

            cur_dir = self.root_dir + dir
            print(cur_dir)

            try:
                os.chdir(cur_dir)
                subprocess.call(f'git checkout `git rev-list -n 1 --before="{self.deadline}" origin/HEAD`', shell=True)

            except Exception as e:
                print(f'Error on {dir}: {e.strerror}')

            print()


if __name__ == '__main__':
    checkouter = Checkouter()
    checkouter.checkout()
