import numpy as np
import librosa, librosa.display 
import matplotlib.pyplot as plt

#피에조부저
import RPi.GPIO as GPIO
import time

# 문자전송
import datetime
from twilio.rest import Client

FIG_SIZE = (15,10)

file = "p4.wav"

sig, sr = librosa.load(file, sr=22050)

print(sig,sig.shape)

plt.figure(figsize=FIG_SIZE)
librosa.display.waveshow(sig, sr, alpha=0.5)
plt.xlabel("Time (s)")  # 시간
plt.ylabel("Amplitude") # 진폭
plt.title("Waveform")
plt.xlim(0,4)
plt.ylim(-0.075, 0.06)

# 신체 이상 감지
if sr>= 0.04:
  print("warning")
  # 경고음
  buzzer = 18
  GPIO.setmode(GPIO.BCM)
  GPIO.setup(buzzer, GPIO.OUT)
  GPIO.setwarnings(False)
  
  pwn=GPIO.PWM(buzzer, 262)
  pwn.start(50.0)
  time.sleep(1.5)
  
  pwn.stop()
  GPIO.cleanup()

  # 문자 전송
  account_sid = 'AC119bdb4229d503ede749ebff8cbfe2f6'
  auth_token = '8955b71ac558117ba5d57832cc3cc1bb'
  client = Client(account_sid, auth_token)
      
  message = client.messages.create(
      to="+8201036233002",
      from_="+12183044999",
      body="\n[WNIC]\n Driver's body abnormality detected!!\n")

  print(message.sid, datetime.datetime.now())

fft = np.fft.fft(sig)

# 복소공간 값 절댓갑 취해서, magnitude 구하기
magnitude = np.abs(fft) 

# Frequency 값 만들기
f = np.linspace(0,sr,len(magnitude))

# 푸리에 변환을 통과한 specturm은 대칭구조로 나와서 high frequency 부분 절반을 날려고 앞쪽 절반만 사용한다.
left_spectrum = magnitude[:int(len(magnitude)/2)]
left_f = f[:int(len(magnitude)/2)]

plt.figure(figsize=FIG_SIZE)
plt.plot(left_f, left_spectrum)
plt.xlabel("Frequency")
plt.ylabel("Magnitude")
plt.title("Power spectrum")
plt.ylim([0, 150])
#plt.xlim([])

# STFT -> spectrogram
hop_length = 512  # 전체 frame 수
n_fft = 2048  # frame 하나당 sample 수

# calculate duration hop length and window in seconds
hop_length_duration = float(hop_length)/sr
n_fft_duration = float(n_fft)/sr

# STFT
stft = librosa.stft(sig, n_fft=n_fft, hop_length=hop_length)

# 복소공간 값 절댓값 취하기
magnitude = np.abs(stft)

# magnitude > Decibels 
log_spectrogram = librosa.amplitude_to_db(magnitude)

# display spectrogram
plt.figure(figsize=FIG_SIZE)
librosa.display.specshow(log_spectrogram, sr=sr, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("Frequency")
plt.colorbar(format="%+2.0f dB")
plt.title("Spectrogram (dB)")
#plt.xlim([0,3])

# MFCCs
# extract 13 MFCCs
MFCCs = librosa.feature.mfcc(sig, sr, n_fft=n_fft, hop_length=hop_length, n_mfcc=13)

# display MFCCs
plt.figure(figsize=FIG_SIZE)
librosa.display.specshow(MFCCs, sr=sr, hop_length=hop_length)
plt.xlabel("Time")
plt.ylabel("MFCC coefficients")
plt.colorbar()
plt.title("MFCCs")

# show plots
plt.show()
