# 인하대학교 미래융합대학교 스승의날 홈페이지

안녕하세요 이 저장소를 관리하고 있는 마루입니다.  
[인하 GDSC 스승의날 홈페이지](https://github.com/gdscinha/2023_teacher-s_day/)에서 제작하고 있는걸 보는데 도움이 되고자 만든 홈페이지입니다.

## 개발 환경 설정

이 프로젝트는 Flask 웹 프레임워크를 사용하여 웹 애플리케이션을 개발하는 데 필요한 환경을 구축하는 방법에 대해 안내합니다.

1. Python 설치

   - Python 3.x 버전을 다운로드하여 설치합니다. (https://www.python.org/downloads/)
   - 설치 과정 중 "Add Python to PATH" 옵션을 선택합니다.

2. 가상 환경(Virtual Environment) 설정

   - 터미널에서 프로젝트 디렉토리로 이동합니다.
   - 가상 환경을 생성합니다:
     ```
     python -m venv venv
     ```
   - 가상 환경을 활성화합니다:

     - Windows:
       ```
       venv\Scripts\activate
       ```

     - macOS/Linux:
       ```
       source venv/bin/activate
       ```

3. 필수 라이브러리 설치

   - 가상 환경이 활성화된 상태에서 다음 명령을 실행하여 의존성 라이브러리를 설치합니다:
     ```
     pip install -r requirements.txt
     ```

4. 개발 서버 실행

   - 터미널에서 다음 명령을 실행하여 개발 서버를 실행합니다:
     ```
     flask run
     ```
   - 개발 서버가 성공적으로 실행되면 웹 브라우저에서 `http://localhost:8000`으로 접속하여 애플리케이션을 확인할 수 있습니다.

## 디렉토리 구조

``` txt
professor_appreciation/
├── static/
│ ├── css/
│ ├── js/
│ ├── svgs/
│ ├── audio/
│ ├── lib/
│ └── images/
├── templates/
│ └── ...
├── app.py
├── requirements.txt
└── README.md
```

- `static/`: 정적 파일 (CSS, JavaScript, 이미지 등)을 저장하는 디렉토리
- `templates/`: Flask 템플릿 파일을 저장하는 디렉토리
- `app.py`: Flask 애플리케이션의 진입점 (메인) 파일
- `requirements.txt`: 프로젝트에 대한 설명과 개발 환경 설정 안내가 포함된 문서
- `README.md`: 프로젝트에 대한 설명과 개발 환경 설정 안내가 포함된 문서

## 환경변수 설정

데이터베이스 또는 배포 작업에 관련된 중요한 정보들은 `.env` 파일에서 관리됩니다. 아래는 `.env` 파일을 작성하는 방법에 대한 예시입니다:

``` .env
# 개발 모드 설정 (development, production, testing 중 하나 선택)
FLASK_ENV=development

# 시크릿 키 (보안을 위해 랜덤한 값으로 설정)
SECRET_KEY=your_secret_key_here

# 데이터베이스 연결 설정
DB_HOST=localhost
DB_PORT=5432
DB_NAME=mydatabase
DB_USER=dbuser
DB_PASSWORD=dbpassword
```

## 소스코드 기여하기

- 이 프로젝트는 개방된 오픈 소스 프로젝트입니다. 기여를 환영합니다. 버그 리포트, 기능 제안, 코드 개선 등 어떠한 형태로든 기여해주시면 감사하겠습니다.
