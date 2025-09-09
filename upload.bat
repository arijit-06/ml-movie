@echo off
echo Initializing Git repository and uploading to GitHub...
echo.

REM Initialize git repository
git init

REM Add core files only
git add recommender.py
git add requirements.txt  
git add README.md
git add mlmodel.ipynb
git add .gitignore

REM Create initial commit
git commit -m "Initial commit: Movie recommendation system with content-based filtering"

REM Add GitHub remote (you'll need to replace with your actual repository URL)
echo.
echo Please create a new repository on GitHub first, then run:
echo git remote add origin https://github.com/YOUR_USERNAME/mustwatch.git
echo git branch -M main
echo git push -u origin main
echo.
pause