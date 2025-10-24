# DonDont 🎯

A beautiful, modern Django web application for tracking your daily habits with dos and don'ts. Build better habits, track your progress, and visualize your journey with an intuitive interface.

![DonDont Banner](https://via.placeholder.com/800x200/667eea/ffffff?text=DonDont+-+Daily+Habit+Tracker)

## ✨ Features

- **Daily Journal**: Check off your daily dos and don'ts with a clean, intuitive interface
- **Streak Tracking**: See your consecutive days of success for each habit
- **Progress Dashboard**: Visual heatmap showing your completion percentage over 90 days
- **Habit Management**: Easily add, edit, and remove habits
- **Percentage Scoring**: Track your daily completion rate
- **Beautiful UI**: Modern, responsive design with Tailwind CSS
- **Local & Private**: Runs locally with SQLite database - your data stays with you

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone or download this repository**

```bash
cd dondont
```

2. **Create a virtual environment** (recommended)

```bash
python -m venv venv

# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Run database migrations**

```bash
python manage.py migrate
```

5. **Create a superuser** (optional, for admin access)

```bash
python manage.py createsuperuser
```

6. **Start the development server**

```bash
python manage.py runserver
```

7. **Open your browser** and navigate to:

```
http://localhost:8000
```

🎉 You're all set! Start tracking your habits!

## 📖 How to Use

### First Time Setup

1. Go to **Manage Habits** (click "Manage" in the navigation)
2. Add your daily "Do" items (things you want to accomplish)
3. Add your daily "Don't" items (things you want to avoid)
4. Navigate to **Today** to start checking them off!

### Daily Usage

1. Click **Today** in the navigation
2. Check off each habit as you complete it
3. Watch your percentage score update in real-time
4. See your streaks grow as you maintain consistency!

### Viewing Progress

- The **Dashboard** shows a beautiful heatmap of your progress
- Green squares indicate high completion rates
- Click any day to view that day's journal
- Navigate between days using the arrow buttons

## 🎨 UI Preview

The app features:

- **Gradient Header**: Beautiful purple gradient navigation
- **Color-Coded Items**: Green for "Dos", Red for "Don'ts"
- **Interactive Checkboxes**: Smooth animations and instant updates
- **Streak Badges**: Fire emoji with day count
- **Progress Bar**: Visual representation of daily completion
- **Heatmap Calendar**: GitHub-style activity visualization

## 🔧 Configuration

### Database

By default, DonDont uses SQLite, which requires no additional setup. The database file (`db.sqlite3`) will be created automatically in your project directory.

### Security

⚠️ **Important**: The default `SECRET_KEY` in `settings.py` is for development only. If you deploy this app, generate a new secret key:

```python
from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())
```

### Customization

- **Time Zone**: Edit `TIME_ZONE` in `dondont/settings.py`
- **Language**: Edit `LANGUAGE_CODE` in `dondont/settings.py`
- **Colors**: Modify Tailwind classes in templates
- **Dashboard Days**: Change the 90-day range in `journal/views.py`

## 📁 Project Structure

```
dondont/
├── dondont/              # Django project settings
│   ├── settings.py       # Configuration
│   ├── urls.py          # Root URL routing
│   └── ...
├── journal/             # Main application
│   ├── models.py        # Database models
│   ├── views.py         # View logic
│   ├── urls.py          # App URL routing
│   ├── admin.py         # Admin interface
│   └── ...
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   └── journal/         # App templates
├── static/              # Static files (CSS, JS)
├── db.sqlite3          # SQLite database (created on first run)
├── manage.py           # Django management script
└── requirements.txt    # Python dependencies
```

## 🛠️ Development

### Adding New Features

The codebase follows Django best practices:

- **Models** (`journal/models.py`): Define your data structure
- **Views** (`journal/views.py`): Handle business logic
- **Templates** (`templates/journal/`): Design your UI
- **URLs** (`journal/urls.py`): Map routes to views

### Database Schema

**DoDont Model**:
- `text`: The habit description
- `item_type`: Either 'do' or 'dont'
- `is_active`: Soft delete flag
- `order`: Display order

**DailyEntry Model**:
- `dodont`: Foreign key to DoDont
- `date`: The date of the entry
- `completed`: Boolean completion status

### Admin Interface

Access the admin panel at `http://localhost:8000/admin` to:
- View all habits and entries
- Manually edit data
- Manage the database

## 🤝 Contributing

This is an open-source project! Contributions are welcome:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 💡 Tips for Success

1. **Keep it Simple**: Start with 3-5 habits
2. **Be Consistent**: Check in daily, even if you miss some items
3. **Celebrate Streaks**: Watch those fire emojis grow!
4. **Review Weekly**: Use the dashboard to identify patterns
5. **Adjust as Needed**: Add or remove habits as your goals evolve

## 🐛 Troubleshooting

**Server won't start?**
- Make sure you've activated your virtual environment
- Check that all dependencies are installed: `pip install -r requirements.txt`
- Run migrations: `python manage.py migrate`

**Can't access the app?**
- Ensure the server is running: `python manage.py runserver`
- Try `http://127.0.0.1:8000` instead of `localhost`

**Database issues?**
- Delete `db.sqlite3` and run `python manage.py migrate` again
- This will create a fresh database (you'll lose your data)

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the Django documentation: https://docs.djangoproject.com/

## 🌟 Acknowledgments

Built with:
- Django - Python web framework
- Tailwind CSS - Utility-first CSS framework
- SQLite - Embedded database
- Love and coffee ☕

---

**Made with ❤️ for habit tracking enthusiasts**

Start building better habits today! 🚀

