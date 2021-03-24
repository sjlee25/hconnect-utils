# hconnect-utils

한양대학교에서 이용하는 [GitLab](https://gitlab.com/)인 [HConnect](https://hconnect.hanyang.ac.kr/)의 그룹 내 프로젝트들을 관리하기 위한 스크립트들입니다.

<br>

## 코드 구성

---

- **clone.py**: 특정 그룹 내 모든 프로젝트 레포지토리를 로컬 디렉토리로 clone 합니다.
- **checkout.py**: Clone 받은 각 레포지토리에서 지정한 시점 이전의 최신 버전으로 checkout 합니다.

<br>

## 사용 방법

---

- 코드 편집기를 실행한 뒤, 주석 설명이 되어 있는 다음 멤버 값들을 목적 및 환경에 알맞게 수정합니다.

- **clone.py**

  - Private token은 HConnect에 로그인 후 Settings 페이지의 Access Tokens 항목에서 모든 scopes에 체크해 발급 받을 수 있습니다.

  ```bash
  self.user_name     = ''                     # GitLab 아이디
  self.password      = ''                     # GitLab 비밀번호
  self.private_token = ''                     # GitLab 설정 페이지에서 발급받은 토큰 값 입력
  self.group_id      = '1011'                 # Clone 하고자 하는 그룹 ID (ex: 1011)
  self.root_dir      = ''                     # 프로젝트들을 clone 할 디렉토리 위치
  ```

  ```bash
  python3 clone.py
  ```

<br>

- **checkout.py**

  - self.deadline에서 지정한 시각 이전에 완료된 커밋/푸시 내역만 고려됩니다.

  ```bash
  self.class_year = '2021'                    # 수업 연도     (ex: 2021)
  self.class_num  = 'ite1014'                 # 수업 학수번호  (ex: ite1014)
  self.deadline   = '2021-03-24 00:00 UTC+9'  # 해당 시각 이전 버전들 중에서 최신으로 체크아웃
  self.root_dir   = ''                        # Clone 받은 프로젝트들이 저장된 로컬 디렉토리
  ```

  ```bash
  python3 checkout.py
  ```

<br>

## 이슈

---

- **clone.py**
  - 스크립트 실행 시 높은 확률로 HTTP Unauthorized 401 에러가 발생해 중단됩니다.
  - 현재로서는 2~3번 정도 반복해 재실행 함으로써 해당 오류 없이 수행 가능합니다.

<br>

- **checkout.py**
  - 지정한 시각 이전에 수행된 커밋/푸시 내역이 없는 경우엔 checkout이 수행되지 않으므로, 로컬 상의 디렉토리 내 파일들이 서버의 해당 시점 이후의 최신 버전으로 남아 있을 수 있습니다.
  - 이와 관련해 " HEAD의 현재 위치는 ..." 메시지가 나타나지 않은 디렉토리는 별도 확인이 필요할 수 있습니다.

