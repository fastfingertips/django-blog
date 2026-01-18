@echo off
echo Setting up the project...

:: Install uv if not found
where uv >nul 2>nul
if %ERRORLEVEL% neq 0 (
    echo uv not found, installing via pip...
    pip install uv
)

:: Sync dependencies
echo Installing dependencies...
uv sync

:: Create .env if it doesn't exist
if not exist .env (
    echo Creating default .env file...
    echo SECRET_KEY=django-insecure-development-key > .env
    echo DEBUG=True >> .env
    echo ALLOWED_HOSTS=127.0.0.1,localhost >> .env
)

:: Run migrations
echo Running database migrations...
uv run python manage.py migrate

echo.
echo Setup complete! You can now run the project using run.bat.
pause
