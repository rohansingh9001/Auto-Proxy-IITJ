@echo off
pip install --user --requirement requirements.txt
copy "RUN.bat" "C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"
python register.py
python auto_proxy.py

