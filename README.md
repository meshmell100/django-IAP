# A restaurant website done in Django

This is a site done in `Django`

## How to contribute

1. Create a virtual environment

   ```bash
   python -m venv venv
   ```

2. Activate the virtual environment

   - Linux:

     ```bash
     source venv/bin/activate
     ```

   - Windows:

     ```bash
     venv/Scripts/activate
     ```

3. Install the project requirements

   ```bash
   pip install -r requirements.txt
   ```

4. Prepare database migrations

   ```bash
   python manage.py makemigrations
   ```

5. Apply database migrations

   ```bash
   python manage.py migrate
   ```

6. Run the site server on your local host

   ```bash
   python manage.py runserver
   ```
