@echo off
REM DonDont Setup Script for Windows

echo 🎯 Setting up DonDont...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ❌ Python is not installed. Please install Python 3.8 or higher.
    exit /b 1
)

echo ✓ Python found

REM Create virtual environment if it doesn't exist
if not exist "venv" (
    echo 📦 Creating virtual environment...
    python -m venv venv
    echo ✓ Virtual environment created
) else (
    echo ✓ Virtual environment already exists
)

REM Activate virtual environment
echo 🔧 Activating virtual environment...
call venv\Scripts\activate.bat

REM Install dependencies
echo 📥 Installing dependencies...
pip install -q -r requirements.txt
echo ✓ Dependencies installed

REM Run migrations
echo 🗄️  Setting up database...
python manage.py makemigrations
python manage.py migrate
echo ✓ Database ready

echo.
echo ✅ Setup complete!
echo.
echo To start using DonDont:
echo   1. Activate the virtual environment: venv\Scripts\activate
echo   2. Start the server: python manage.py runserver
echo   3. Open your browser to: http://localhost:8000
echo.
echo Optional: Create a superuser for admin access
echo   python manage.py createsuperuser
echo.
echo Happy habit tracking! 🚀

