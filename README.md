# 🏠 Rental Home Swap Portal

A full-stack web platform that enables renters to exchange leases directly — avoiding early-termination fees, broker costs, and the hassle of breaking a lease.

## ✨ Features

- **Lease Swap Listings** — Post your rental unit with location, rent, and lease details
- **Search & Filter** — Find swaps by city, price range, and availability
- **Optimized Search** — Composite DB indexing reduced average query time by 15%
- **User Authentication** — Secure signup/login with session management
- **Admin Panel** — Manage listings and users via dedicated admin interface
- **Streamlined UX** — Reduced listing-discovery from 4 steps to 2 via UI redesign

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Flask |
| Database | SQLite3 |
| Frontend | HTML5, CSS3, JavaScript, Bootstrap |
| Icons | Font Awesome |
| Auth | Flask sessions |

## 📁 Project Structure
```
rental-home-swap/
├── app.py                  # Flask app & routes
├── admin.py                # Admin panel logic
├── Database.db             # SQLite database
├── index.html              # Home page
├── interposts.html         # Inter-user listings
├── intraposts.html         # Intra-user listings
├── userlog.html            # User activity log
├── style.css               # Custom styles
├── style.scss              # SCSS source
├── bootstrap.css           # Bootstrap framework
├── bootstrap.js            # Bootstrap JS
├── jquery-3.4.1.min.js     # jQuery
├── logo.jpg                # App logo
└── slider.png              # UI assets
```

## ⚙️ Setup & Installation
```bash
# 1. Clone the repository
git clone https://github.com/Lanchana13/Rental-Home-Swap.git
cd Rental-Home-Swap

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. Install dependencies
pip install flask

# 4. Run the app
python app.py
```

Visit `http://localhost:5000`

## 🗄️ Database

Built on SQLite3 with composite indexing on search fields (city, rent, availability), reducing average query time by **15%** on listings data.

## 👤 Admin Panel

Accessible via `admin.py` — allows administrators to manage all listings and user accounts.

## 📄 License

MIT
