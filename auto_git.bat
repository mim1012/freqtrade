@echo off
echo Git 자동 커밋 및 푸시 시작

:: 현재 날짜와 시간을 변수에 저장
for /f "tokens=2 delims==" %%I in ('wmic os get localdatetime /value') do set datetime=%%I
set datetime=%datetime:~0,8%-%datetime:~8,6%

:: 변경된 파일 스테이징
git add .

:: 커밋 메시지와 함께 커밋
git commit -m "자동 커밋: %datetime%"

:: 원격 저장소로 푸시
git push origin master

echo 완료되었습니다!
pause 