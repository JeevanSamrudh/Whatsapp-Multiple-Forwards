echo on
cls
title Opening the Required Files
cd "C:\current-working-directory"
start "" chrome.exe --remote-debugging-port=9014 --user-data-dir="C:\Users\91807\Desktop\Project\DOTD\New\Chrome_Profile" "https://web.whatsapp.com/"
pause
py -3 prog1.py

