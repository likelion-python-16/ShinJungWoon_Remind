from django.test import TestCase

# Create your tests here.
#   <!-- // 문서가 로드되면 리스트 항목을 불러와라
#   document.addEventListener("DOMContentLoaded", function(){
#     console.log("list loading")
#   });

#   // 버튼을 클릭하면 서버에 접속해라
#   document.getElementById("createBtn").addEventListener("click", () => {
#     console.log("createBtn click")
#   }); -->
#   {% for todo in todos %}
#     <div class = "todo-item">
#       <p>{{todo.description}}</p>
#       <p><{{todo.name}}</p>
#       <p><{{todo.complete}}</p>
#       <p><{{todo.complete_at}}</p>
#       <p>{{todo.exp}}</p>
#     </div>
#   {% empty %}
#     <p>등록된 할일이 없습니다.</p>
  
#   {% endfor %}


# 처리해야할 기능
# 1. 문서 로드후 초기화:
# 2. 생성버튼 이벤트 바인딩: 클릭이벤트등 UI요소와 연결하는 작업
# 3. 버튼 클릭시 동작실행:
# 4. 폼 데이터 수집:
# 5. 비어있는 숫자 처리:
# 6. 서버에 post
# 7. 요청 성공처리
# 8. 요청 실패처리 
# 빈공백으로 데이터 넘길때
# 입력값 검증
# UI 피드백 로딩중 저장중  성공했습니다.
# 날짜 유혀성 검사:
