# Full-Stack Login Application

This project is a full-stack login application built with a Vue 3 frontend and a Python (Flask) backend, based on the provided design diagram.

## Project Structure

\`\`\`
.
├── backend/        # Python Flask server
└── frontend/       # Vue 3 client application
\`\`\`

## Prerequisites

- Node.js and npm (or yarn)
- Python 3 and pip

## Backend Setup

1.  **Navigate to the backend directory:**
    \`\`\`bash
    cd backend
    \`\`\`

2.  **Create a virtual environment (recommended):**
    \`\`\`bash
    python -m venv venv
    source venv/bin/activate  # On Windows use \`venv\Scripts\activate\`
    \`\`\`

3.  **Install the required Python packages:**
    \`\`\`bash
    pip install -r requirements.txt
    \`\`\`

4.  **Run the Flask server:**
    \`\`\`bash
    python app.py
    \`\`\`
    The backend server will start running on \`http://127.0.0.1:5001\`.

## Frontend Setup

1.  **Navigate to the frontend directory in a new terminal:**
    \`\`\`bash
    cd frontend
    \`\`\`

2.  **Install the npm dependencies:**
    \`\`\`bash
    npm install
    \`\`\`

3.  **Run the Vue development server:**
    \`\`\`bash
    npm run dev
    \`\`\`
    The frontend application will be available at \`http://127.0.0.1:5173\` (or another port if 5173 is in use).

## How to Use

1.  Make sure both the backend and frontend servers are running.
2.  Open your web browser and go to the frontend URL (e.g., \`http://127.0.0.1:5173\`).
3.  The login page will be displayed.
4.  **Username:** \`admin\`
5.  **Password:** \`password\`
6.  Enter the characters you see in the captcha image.
7.  Click the "登录" (Login) button.

You will see an alert message indicating whether the login was successful or not. If login fails due to an incorrect captcha or credentials, the error will be displayed and a new captcha will be loaded.
