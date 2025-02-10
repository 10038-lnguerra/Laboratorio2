from pathlib import Path
from datetime import timedelta
from dotenv import load_dotenv
import os

# Obtener la ruta base del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
dotenv_path = os.path.join(BASE_DIR, ".env")

# Forzar la carga manual del archivo `.env`
if os.path.exists(dotenv_path):
    print(f"Cargando variables de entorno desde: {dotenv_path}")  # 🔹 Mensaje de depuración
    load_dotenv(dotenv_path=dotenv_path, override=True)  # 🔹 Cargar variables de entorno
else:
    print("⚠ ERROR: No se encontró el archivo .env en la raíz del backend.")

# Configuración de seguridad
SECRET_KEY = os.getenv("SECRET_KEY", "django-insecure-default-key")
DEBUG = os.getenv("DEBUG", "True") == "True"
ALLOWED_HOSTS = os.getenv("ALLOWED_HOSTS", "localhost,127.0.0.1").split(",")

# Configuración de Google Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if not GEMINI_API_KEY:
    raise ValueError("⚠ ERROR: La API Key de Google Gemini no está configurada. Revisa el archivo .env.")

print("🔹 API Key de Gemini cargada correctamente:", GEMINI_API_KEY[:10] + "********")  # 🔹 Debugging

# Google Cloud Credentials (Opcional)
GOOGLE_APPLICATION_CREDENTIALS = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

# Aplicaciones Instaladas
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Django REST Framework y Seguridad
    'rest_framework',
    'rest_framework_simplejwt',
    'corsheaders',
    
    # Apps propias
    'api',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',  # Habilitar CORS
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Configuración de Rutas
ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'

# Configuración de Base de Datos (SQLite por defecto)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Validaciones de Contraseña
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Configuración de Internacionalización
LANGUAGE_CODE = 'es'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Archivos Estáticos
STATIC_URL = 'static/'

# Configuración de DRF y JWT (Tokens de Autenticación)
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
}

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=30),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True,
    'AUTH_HEADER_TYPES': ('Bearer',),
}

# Configuración de CORS (Permitir peticiones desde el frontend)
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # React frontend
    "http://127.0.0.1:3000",
]

CORS_ALLOW_ALL_ORIGINS = True  # ⚠️ Solo para desarrollo, en producción usa CORS_ALLOWED_ORIGINS

# Variable para Debug
print("🔹 API Key de Gemini cargada correctamente:", GEMINI_API_KEY[:10] + "********")  # 🔹 Debugging
