#!/bin/bash
# DonDont Setup Script

echo "🎯 Setting up DonDont..."
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.8 or higher."
    exit 1
fi

echo "✓ Python 3 found"

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
    echo "✓ Virtual environment created"
else
    echo "✓ Virtual environment already exists"
fi

# Activate virtual environment
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Install dependencies
echo "📥 Installing dependencies..."
pip install -q -r requirements.txt
echo "✓ Dependencies installed"

# Run migrations
echo "🗄️  Setting up database..."
python manage.py makemigrations
python manage.py migrate
echo "✓ Database ready"

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start using DonDont:"
echo "  1. Activate the virtual environment: source venv/bin/activate"
echo "  2. Start the server: python manage.py runserver"
echo "  3. Open your browser to: http://localhost:8000"
echo ""
echo "Optional: Create a superuser for admin access"
echo "  python manage.py createsuperuser"
echo ""
echo "Happy habit tracking! 🚀"

