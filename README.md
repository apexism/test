<<<<<<< HEAD
=======
# beta_code에서 작업후 확정시 master에 업로드


# 협업 하는 법
invite collaboraors > add people > 친구 검색 후 추가
master는 되도록 건드리지 않도록 한다. 확정된 변경사항만 추가

# 내 브렌치 만드는 법
git checkout -b [branch 이름] # 내 브렌치 만들기
git push --set-upstream origin [branch 이름] #git 에 브렌치 추가


# 내 브렌치에 소스코드 업로드 하기
git add .
git commit -m "first commit"
git push origin beta_code
# 마스터 브렌치에 소스 가져오기(완전 확정되기 전까지 입력하지 않는다)
git pull origin master 
# 브렌치끼리 이동하는 법
git checkout [브렌치 이름]
>>>>>>> 693e8511dad7fddd1011e8e512d550188004105d

