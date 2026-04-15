@echo off
title Hate Speech Detector - Startup
echo ========================================
echo 🚀 Starting Hate Speech Detector Servers
echo ========================================
echo.

:: Check Python
python --version >nul 2>&1
if errorlevel 1 (
  echo ❌ Python not found. Install from python.org
  pause
  exit /b 1
)
echo ✅ Python OK

:: Check Node.js
node --version >nul 2>&1
if errorlevel 1 (
  echo ❌ Node.js not found. Install from nodejs.org
  pause
  exit /b 1
)
echo ✅ Node.js OK

:: Backend deps check/install
echo.
echo [0/4] Installing backend dependencies...
cd /d "c:\Users\sonu9\OneDrive\Desktop\mlproject\backend"
if not exist node_modules (
  echo Installing npm packages...
  npm install
  if errorlevel 1 (
    echo ❌ NPM install failed
    pause
    exit /b 1
  )
)
echo ✅ Backend ready

:: Check and kill old processes on ports
echo.
echo [Prep] Checking and cleaning old server processes...
echo.

:: Kill on port 5000 (ML Flask/Python)
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :5000 ^| findstr LISTENING') do (
  echo Killing old ML server PID %%a on port 5000
  taskkill /PID %%a /F >nul 2>&1
)

:: Kill on port 3000 (Backend/Node)
for /f "tokens=5" %%a in ('netstat -aon ^| findstr :3000 ^| findstr LISTENING') do (
  echo Killing old Backend PID %%a on port 3000
  taskkill /PID %%a /F >nul 2>&1
)

timeout /t 2 /nobreak >nul

:: Verify ports free
netstat -an | findstr :5000 >nul && echo ✅ Port 5000 free
netstat -an | findstr :3000 >nul && echo ✅ Port 3000 free

:: Start ML
echo.
echo [1/4] Starting ML Server (Flask :5000)...
cd /d "c:\Users\sonu9\OneDrive\Desktop\mlproject\ml"
start "ML Server :5000" cmd /k "call venv\Scripts\activate.bat & pip install -r requirements.txt & title ML Server & python app.py"

timeout /t 10 /nobreak >nul

:: Start Backend
echo [2/4] Starting Backend (Node :3000)...
cd /d "c:\Users\sonu9\OneDrive\Desktop\mlproject\backend"
start "Backend :3000" cmd /k "title Backend && npm start"

timeout /t 3 /nobreak >nul

echo.
echo ✅ Servers Started Successfully! 🚀
echo.
echo 📱 URLs:
echo    ML Health: http://localhost:5000/health
echo    Backend API: http://localhost:3000/check  
echo    Frontend: file:///c:/Users/sonu9/OneDrive/Desktop/mlproject/frontend/index.html
echo.
echo 💡 Test in new tab: Open frontend/index.html in browser
echo 💡 Analyze some text to test!
echo.
echo Press any key to close...
pause >nul







