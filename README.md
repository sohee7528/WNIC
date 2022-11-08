# WNIC
* wav2csv.py로 변환한 파일들은 github에 업로드할 수 없는 파일크기로 업로드 하지 못하였습니다. 

1. GNU Radio를 사용하여 HackRF one(전파 송수신기) 2대를 연결
https://github.com/gnuradio
2. HackRF one 2대 사이에서 이상 행동(고개를 끄덕이는 행동) 반복 후 .wav 파일 추출
3. Audacity을 사용하여 .wav 파일 분석
https://github.com/audacity
4. wav2csv.py를 사용하여 .wav 파일을 .csv 파일로 변환 후 분석
5. Colab을 사용하여 Python으로 .wav 파일 분석
6. 분석 결과를 기반으로 이상 행동 탐지 코드 작성
7. 아두이노 피에조부저로 경고음 발생, twilio를 사용하여 문자 송신 구현
https://www.twilio.com/
