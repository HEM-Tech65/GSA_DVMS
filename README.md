# DVMS - Digital Visitor Management System

A Django-based web application for managing visitor check-ins at Ghana Communication Technology University. The system allows visitors to check in by providing their name and host name, storing data both locally in SQLite and syncing to Firebase Firestore for cloud storage.

## Features

- Visitor check-in form
- Local SQLite database storage
- Cloud synchronization with Firebase Firestore
- Simple web interface with HTML templates

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Firebase project with Firestore enabled (service account key required)

## Installation and Setup

1. **Clone or Download the Project**
   ```
   # If cloning from a repository
   git clone <repository-url>
   cd GSA_DVMS
   ```

2. **Create a Virtual Environment**
   ```
   python -m venv venv
   ```

3. **Activate the Virtual Environment**
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

5. **Database Setup**
   ```
   python manage.py migrate
   ```

6. **Firebase Configuration**
   - Ensure `serviceAccountKey.json` is present in the project root directory
   - This file should contain your Firebase service account credentials

7. **Run the Development Server**
   ```
   python manage.py runserver
   ```

8. **Access the Application**
   - Open your web browser and go to `http://127.0.0.1:8000/`
   - Navigate to the check-in page (configured in URLs)

## Project Structure

- `dvms_project/` - Main Django project settings
- `visitor_manager/` - Django app containing models, views, and templates
- `db.sqlite3` - Local SQLite database
- `serviceAccountKey.json` - Firebase service account key
- `manage.py` - Django management script

## Usage

1. Visit the check-in page
2. Enter visitor name and host name
3. Submit the form
4. Data is saved locally and synced to Firebase Firestore
5. Success page is displayed

## Security Notes

- The application includes basic validation for required fields
- In production, ensure proper security measures are implemented
- Keep the `serviceAccountKey.json` secure and never commit it to version control

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

[Add license information here]