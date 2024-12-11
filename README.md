# Backend for Pic-Desc and SketchToCode project

## Steps to follow before starting the project
- ### Clone the repo
  ```shell
  git clone https://github.com/KanishkRastogi46/pic-desc-backend.git
  ```
- ### Create virtual environment
  ```shell
  python -m venv venv
  ```
- ### Activate virtual environment
  ```shell
  ./venv/Scripts/activate
  ```
- ### Install required packages
  ```shell
  pip install -r requirements.txt
  ```
- Create .env file at the root folder
- Also create an API key to integrate Google Gemini Api on [Google ai studio](https://aistudio.google.com/)
- Run your app using
  ```shell
  uvicorn main:app --reload
  ```
- Your app is running on port 8000
