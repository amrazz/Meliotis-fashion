# Meliotis Fashion

## 📌 Overview

Meliotis Fashion is a fully-featured e-commerce platform built with Python Django. It provides a seamless shopping experience with dedicated sections for Men's, Women's, and Kids' fashion, along with accessories. The platform includes comprehensive features such as user authentication, product catalog management, shopping cart functionality, wishlist, payment processing via Razorpay, and filter capabilities.

## ✨ Features

- **User Authentication**
  - Email and OTP verification
  - Google OAuth integration
  - User profile management
  - Address management system

- **Product Management**
  - Categorized products (Men, Women, Kids, Accessories)
  - Product variants (sizes, colors)
  - Multiple product images
  - Brand management
  - Detailed product pages

- **Shopping Experience**
  - Shopping cart functionality
  - Wishlist feature
  - Product filtering and search
  - Responsive design for all devices

- **Payment Processing**
  - Razorpay integration
  - Secure checkout process
  - Order management

- **Marketing Tools**
  - Discount coupons system
  - Category offers
  - Referral program
  - Banner management

- **Admin Dashboard**
  - Product inventory management
  - Order tracking
  - Customer management
  - Sales analytics

## 🛠️ Tech Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript
- **Database**: PostgreSQL
- **Payment Gateway**: Razorpay
- **Authentication**: Django AllAuth (with Google OAuth)
- **Styling**: Bootstrap 4, Crispy Forms
- **Email**: SMTP (Gmail)


```

## 🔧 Installation & Setup

### Prerequisites

- Python 3.8+
- PostgreSQL
- pip

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone https://github.com/amrazz/Meliotis-fashion.git
   cd meliotis-fashion
   ```

2. **Create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   cd ecom
   ```

4. **Set up environment variables**

   Create a `.env` file in the ecom directory with the following variables:
   ```
   SECRET_KEY=your_secret_key
   DATABASE_NAME=ecomdata
   DATABASE_USER=postgres
   DATABASE_PASSWORD=your_password
   EMAIL_HOST_USER=your_email@gmail.com
   EMAIL_HOST_PASSWORD=your_app_password
   RAZOR_KEY_ID=your_razorpay_key_id
   RAZOR_KEY_SECRET=your_razorpay_key_secret
   ```

5. **Set up the database**
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the site**
   Open your browser and navigate to `http://127.0.0.1:8000/`
   For admin access, go to `http://127.0.0.1:8000/admin/admin_login`

## 🔐 Google OAuth Setup

1. Create a project in the [Google Developer Console](https://console.developers.google.com/)
2. Enable the Google+ API
3. Create OAuth client ID credentials
4. Add authorized redirect URIs (e.g., `http://localhost:8000/accounts/google/login/callback/`)
5. Add the client ID and secret to the Django admin site:
   - Go to `/admin/socialaccount/socialapp/`
   - Add a new social application
   - Select "Google" as the provider
   - Fill in the client ID and secret

## 💳 Razorpay Integration

1. Create an account at [Razorpay](https://razorpay.com/)
2. Get your API key ID and secret from the dashboard
3. Add them to your `.env` file

## 🚀 Deployment

For deployment to a production server:

1. Set `DEBUG = False` in settings.py
2. Configure proper ALLOWED_HOSTS
3. Set up a production database
4. Configure a web server (Nginx/Apache) with Gunicorn/uWSGI
5. Set up HTTPS with Let's Encrypt