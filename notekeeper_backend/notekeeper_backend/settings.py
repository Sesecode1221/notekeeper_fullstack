INSTALLED_APPS = [
    'django.contrib.admin',  # ✅ Added missing comma
    'django.contrib.contenttypes',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.sites',  # Required for authentication and middleware
    'django.contrib.staticfiles',  # Required for serving static files
    'django.contrib.messages',  # Required for flash messages

    # Third-party apps
    'rest_framework',
    'corsheaders',

    # Your apps
    'notes',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Keep this for CORS
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'notekeeper_db',
        'USER': 'postgres',
        'PASSWORD': 'notekeeper',  # Ensure this matches your PostgreSQL password
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# ✅ Fix: Allow Hosts (Required for Production)
DEBUG = True  # Change to False in Production
ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'your-production-domain.com']

# ✅ Improved CORS Configuration
if DEBUG:
    CORS_ALLOW_ALL_ORIGINS = True  # Allow all origins in development
else:
    CORS_ALLOWED_ORIGINS = [
        "http://localhost:4200",  # Example: Angular frontend
        "https://yourfrontenddomain.com",  # Your production domain
    ]

# ✅ Static Files (Required for Deployment)
STATIC_URL = '/static/'

# ✅ Root URL Configuration
ROOT_URLCONF = 'notekeeper_backend.urls'  # Ensure this matches your project structure

# ✅ Default Auto Field (Django 3.2+ Requirement)
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ Site ID (Required for `django.contrib.sites`)
SITE_ID = 1

# ✅ Templates Configuration (Ensure Django Can Find Your Templates)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # Update if needed
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
