🎬 Movie Ticket Booking System



A full-stack Movie Ticket Booking System built with Django REST Framework and React.js. The application allows users to browse movies, view available shows, select seats, book tickets, manage bookings, and handle seat availability.



🚀 Project Overview



The Movie Ticket Booking System provides a real-world online movie booking workflow with a React frontend and Django REST API backend.



Users can:



\- Create an account and sign in

\- Browse available movies

\- View movie details and available shows

\- Select seats for a particular show

\- Book movie tickets

\- Manage bookings

\- Cancel bookings

\- Handle seat availability

\- Process booking/payment information

\- Automatically release expired seats



✨ Key Features



👤 User Authentication



\- User registration

\- User login

\- JWT-based authentication

\- User profile management

\- Update password

\- Sign out functionality



🎬 Movie Management



\- Display active movies

\- Movie title and description

\- Genre and language

\- Movie duration

\- Release date

\- Movie posters



🎟️ Show Management



\- Movie-wise shows

\- Show date and time

\- Screen information

\- View available shows before booking



💺 Seat Booking



\- Display seats for a selected show

\- Select multiple seats

\- Track booked seats

\- Prevent already-booked seats from being selected

\- Release expired seats automatically



💳 Booking \& Payment



\- Booking management

\- Booking-seat relationship

\- Payment information/model

\- Booking cancellation support



🔄 Automatic Seat Release



A Django management command is included to check expired shows/bookings and release seats when required.



python manage.py reset\_expired\_seats



🛠️ Technologies Used



Frontend



\- React.js

\- JavaScript

\- HTML5

\- CSS3

\- Axios

\- React Router



Backend



\- Python

\- Django

\- Django REST Framework

\- JWT Authentication



Database



\- SQLite3



Development Tools



\- Visual Studio Code

\- Git

\- GitHub

\- Django Admin

\- Vite



📁 Project Structure



Movie\_Tricket/

│

├── api/

│   ├── management/

│   │   └── commands/

│   │       └── reset\_expired\_seats.py

│   ├── migrations/

│   ├── models.py

│   ├── serializers.py

│   ├── urls.py

│   ├── utils.py

│   └── views.py

│

├── authen/

│   ├── migrations/

│   ├── templates/

│   ├── urls.py

│   └── views.py

│

├── base/

│   ├── migrations/

│   ├── templates/

│   ├── models.py

│   ├── urls.py

│   └── views.py

│

├── Movie\_Tricket/

│   ├── settings.py

│   ├── urls.py

│   ├── asgi.py

│   └── wsgi.py

│

├── Media/

├── static/

├── templates/

├── manage.py

└── README.md



⚙️ Installation \& Setup



1\. Clone the repository



git clone https://github.com/kp1312-bot/movie-ticket-booking.git

cd movie-ticket-booking



2\. Create a virtual environment



python -m venv my\_venv



3\. Activate the virtual environment



Windows



my\_venv\\Scripts\\activate



4\. Install dependencies



pip install django djangorestframework djangorestframework-simplejwt django-cors-headers pillow



5\. Apply migrations



python manage.py migrate



6\. Create an admin account



python manage.py createsuperuser



Follow the prompts to create the Django admin account.



7\. Start the Django server



python manage.py runserver



The backend will normally run at:



http://127.0.0.1:8000/



🔗 API



The project provides REST APIs for movie, show, seat, authentication, and booking functionality.



Example API endpoints:



/api/movies/

/api/shows/

/api/seats/<show\_id>/

/api/signup/

/api/signin/

/api/profile/

/api/signout/

/api/update\_profile/

/api/update\_password/



🖥️ Frontend



The React frontend communicates with the Django REST API using Axios.



Example API base URL during local development:



http://127.0.0.1:8000/api/



The frontend provides the booking flow:



Home

&#x20; ↓

Movie

&#x20; ↓

Available Shows

&#x20; ↓

Seat Selection

&#x20; ↓

Booking

&#x20; ↓

Payment / Booking Management



🧪 Expired Seat Management



The project includes a custom Django management command for handling expired seats.



Run:



python manage.py reset\_expired\_seats



Expected result:



Expired shows checked successfully.



📸 Screenshots



Home Page



Add your Home page screenshot here:



screenshots/home.png



Movie Shows



Add your Shows page screenshot here:



screenshots/shows.png



Seat Selection



Add your Seat Selection page screenshot here:



screenshots/seats.png



Booking / Payment



Add your Booking or Payment screenshot here:



screenshots/booking.png



«Create a "screenshots" folder in the repository and add your actual project screenshots using the filenames above.»



🎯 Learning Outcomes



Through this project, I practiced:



\- Full-stack web application development

\- Django REST API development

\- React frontend development

\- API integration using Axios

\- JWT authentication

\- Database relationships

\- Movie and show management

\- Seat booking logic

\- Booking and cancellation workflow

\- Git and GitHub

\- Django management commands

\- Frontend-backend integration



📌 Future Improvements



Possible future enhancements include:



\- Online payment gateway integration

\- Email booking confirmation

\- Downloadable booking ticket

\- QR code on tickets

\- Movie search and filtering

\- Theatre/location selection

\- Booking history dashboard

\- Production database such as MySQL/PostgreSQL

\- Cloud deployment



👨‍💻 Developer



Krishna Pal



2025 BBA-CA Graduate | Python Full Stack Developer Fresher



Skills



\- Python

\- Django

\- Django REST Framework

\- React.js

\- JavaScript

\- HTML

\- CSS

\- SQL

\- Git \& GitHub



🔗 GitHub Repository



"Movie Ticket Booking System" (https://github.com/kp1312-bot/movie-ticket-booking)



\---



⭐ This project was developed as a full-stack learning and portfolio project demonstrating frontend, backend, API, authentication, database, and booking workflow implementation.

