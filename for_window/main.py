# main.py
import build_data
import Draw_graph

# 사용자에게 과목명 입력받기
user_choice = input("성적 분포를 알고 싶은 과목명을 입력하세요: ")

# 데이터를 불러오기
data = build_data.build_data()  # build_data 파일에 정의된 함수 build_data() 사용
subjects = data.keys()  # 과목명 추출 (겉 딕셔너리의 key)

# 과목 찾기
draw_subject = None
for subject in subjects:
    if user_choice == subject:
        draw_subject = subject
        break

if draw_subject is None:
    print("입력한 과목명이 데이터에 없습니다.")
    exit()

# draw_subject의 데이터 확인
if not isinstance(data[draw_subject], dict):
    print(f"오류: {draw_subject} 데이터 형식이 잘못되었습니다.")
    exit()

# 점수 리스트 추출
scores = list(data[draw_subject].keys())

# 남자 점수 딕셔너리
male = {}
for score in scores:
    if isinstance(data[draw_subject][score], list) and len(data[draw_subject][score]) == 2:
        male[score] = data[draw_subject][score][0]
    else:
        print(f"오류: 점수 {score}의 데이터 형식이 잘못되었습니다.")
        exit()

# 여자 점수 딕셔너리
female = {}
for score in scores:
    if isinstance(data[draw_subject][score], list) and len(data[draw_subject][score]) == 2:
        female[score] = data[draw_subject][score][1]
    else:
        print(f"오류: 점수 {score}의 데이터 형식이 잘못되었습니다.")
        exit()

# 결과 출력 (확인용)
#print(f"선택한 과목: {draw_subject}")
#print("남자 점수 분포:", male)
#print("여자 점수 분포:", female)

# 그래프 그리기
Draw_graph.DrawG(draw_subject, male, female)  # Draw_graph 파일에 정의된 함수 DrawG 사용
