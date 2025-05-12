@echo off
cd /d "%~dp0"
echo [+] Adding all changes...
git add .

echo [+] Committing...
git commit -m "Auto commit from script" 2>nul

echo [+] Pushing to GitHub...
git push origin main

echo [✓] Push complete.
pause
