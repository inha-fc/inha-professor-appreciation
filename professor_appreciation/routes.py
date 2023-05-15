from flask import Flask, render_template
from professor_appreciation import app

# 임시로 테스트를 위해 잠시 작성한 교수 정보입니다.
# TODO: 데이터베이스이나 .env 파일에서 가져오게 구현하세요
professors_data = [
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'},
    {'name': '교수님', 'department': '소속학과'}
]

@app.route('/')
def index():
    return render_template('index.html', professors=professors_data)

@app.route('/professors')
def professors_page():
    return render_template('professors.html', professors=professors_data)

@app.route('/professor/<int:professor_id>')
def professor(professor_id):
    if professor_id < len(professors_data):
        professor = professors_data[professor_id]
        return f"Information for professor {professor['name']}, Department: {professor['department']}"
    else:
        return "Invalid professor ID"