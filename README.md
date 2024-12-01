● Default Virtual Environment:
i. Activate the virtual environment: use the
e4_trainor_django_course virtual env
● Application Description:
○ The web application is designed to provide information about living in
different cities. It caters to both regular users and administrative users.
Regular Users:
Tourists: Tourists can log in using the username "tourist" and the password "{iSchoolUI}".
They have active accounts and staff privileges, allowing them to access and interact with
various features across the application.
Tourist Guides: Tourist guides have the username "touristguide" and the password
"{iSchoolUI}". They possess active accounts and staff privileges, enabling them to use
features designed for guiding tourists.
Testers: Testers have the username "tester" and the password "{iSchoolUI}". They have
active accounts, staff privileges, and superuser status. This grants them extensive
access to the application, facilitating thorough testing and quality assurance.
Administrative Users:
Sysadmins: Sysadmins use the username "sysadmin1" and the password "{iSchoolUI}".
They enjoy active accounts, staff privileges, and superuser status, providing them with
comprehensive control and management capabilities within the application.
Citizen: Citizens have the username "citizen" and the password "{iSchoolUI}". They are
part of the "ci_user" group, with active accounts, staff privileges, and the ability to access
and manage different aspects of the application.
○
● Authentication and Authorization Scheme:
Spreadsheets: group_permissions_finalproject users_for_finalproject
Screenshots of spreadsheets (users, permissions):
○ The application uses Django's built-in authentication system.
● Tourists:
○ Authentication: Tourists are authenticated using a username-password pair. They
use the username "tourist" and the password "{iSchoolUI}" to log in.
○ Authorization: Tourists have the following permissions:
i. City: View, add, change, delete
ii. Country: View countries
iii. Event: View, add, change, delete
iv. Hotel: Not allowed to view
v. Landmark: View landmarks.
vi. Museum: View museums.
vii. Restaurant: View restaurants.
viii. Review: View and add reviews.
● Tourist Guides:
○ Authentication: Tourist guides authenticate with the username "touristguide" and
the password "{iSchoolUI}".
○ Authorization: Tourist guides have the following permissions:
i. City: View, add, change, delete cities
ii. Country: View, add, change, delete countries.
iii. Event: View, add, change, delete
iv. Hotel: View, add, change, delete
v. Landmark: View, add, change, delete landmarks.
vi. Museum: Not allowed to view.
vii. Restaurant: View, add, delete, change
viii. Review: Not allowed to view.
○ Tourist guides can add tours and activities to events and hotels.
● Testers:
○ Authentication: Testers log in with the username "tester" and the password
"{iSchoolUI}".
○ Authorization: Testers have the following permissions:
i. City: View, add, change, delete
ii. Country: View, add, change, delete
iii. Event: View events, add events, change events, and delete events.
iv. Hotel: View hotels, add hotels, change hotels, and delete hotels.
v. Landmark: View landmarks, add landmarks, change landmarks, and
delete landmarks.
vi. Museum: View museums, add museums, change museums, and delete
museums.
vii. Restaurant: View restaurants, add restaurants, change restaurants, and
delete restaurants.
viii. Review: View reviews, add reviews
● Sysadmins:
○ Authentication: Sysadmins authenticate using the username "sysadmin1" and the
password "{iSchoolUI}".
○ Authorization: Sysadmins possess superuser status, granting them extensive
access and control:
i. All permissions available to testers.
ii. Ability to add, change, and delete cities, countries, and tourist attractions.
iii. City: View, add, change, delete
iv. Country: View, add, change, delete
v. Event: View events, add events, change events, and delete events.
vi. Hotel: View hotels, add hotels, change hotels, and delete hotels.
vii. Landmark: View landmarks, add landmarks, change landmarks, and
delete landmarks.
viii. Museum: View museums, add museums, change museums, and delete
museums.
ix. Restaurant: View restaurants, add restaurants, change restaurants, and
delete restaurants.
x. Review: View reviews, add reviews
● Citizen:
○ Authentication: Citizens log in with the username "citizen" and the password
"{iSchoolUI}".
○ Authorization: Citizens are part of the "ci_user" group and have the following
permissions:
i. City: View cities.
ii. Country: View countries.
iii. Event: View events.
iv. Hotel: View hotels.
v. Landmark: View landmarks.
vi. Museum: View museums.
vii. Restaurant: View restaurants.
viii. Review: View reviews.
● User IDs and Passwords (Look above for more descriptions):
○ User: tourist
i. Password: {iSchoolUI}
ii. Explanation: This user represents tourists who visit the application. They
have limited access to view cities, countries, events, hotels, landmarks,
museums, restaurants, and reviews. They can also add reviews to
various entities.
○ User: touristguide
i. Password: {iSchoolUI}
ii. Explanation: This user represents tourist guides. They have more
privileges than tourists, including the ability to view, add, change, and
delete events, hotels, landmarks, museums, restaurants, and reviews.
They can also add tours and activities to events and hotels.
○ User: tester
i. Password: {iSchoolUI}
ii. Explanation: Testers are quality assurance professionals. They have
extensive permissions, including viewing and managing cities, countries,
events, hotels, landmarks, museums, restaurants, and reviews. They can
add, change, and delete these entities for testing purposes.
○ User: sysadmin1
i. Password: {iSchoolUI}
ii. Explanation: Sysadmins are system administrators with superuser
privileges. They have full control over the application, including the ability
to view and manage cities, countries, events, hotels, landmarks,
museums, restaurants, and reviews. They can add, change, and delete
these entities as needed.
○ User: citizen
i. Password: {iSchoolUI}
ii. Explanation: Citizens are regular users who can view cities, countries,
events, hotels, landmarks, museums, restaurants, and reviews
● Testing Instructions:
○ To test the application, follow these steps:
i. Start the Django development server: python manage.py
runserver
ii. Open a web browser and navigate to the local server URL
(e.g., http://localhost:8000/)
iii. Use the provided user IDs and passwords to log in as different
user types and test the functionalities described above.
iv. Test various features, including browsing cities,
adding/editing/deleting cities (for administrative users), leaving
comments.
Other Relevant Information:
○ The application is designed to be responsive and mobile-friendly, ensuring
a consistent user experience across different devices.
○ The project code follows the PEP 8 style guide for Python code formatting
and adheres to Django's best practices.
○ Please refer to the code comments and docstrings for additional details
about specific functions, classes, or modules.
