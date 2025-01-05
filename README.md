# README: Message Board Web Application

## Default Virtual Environment
**Virtual Environment Name**: `e4_trainor_django_course`  
**Activation**: Activate the virtual environment before running the project.

---

## Application Description
This web application provides information about living in different cities, designed for two primary user groups: regular users and administrative users.

### Regular Users
1. **Tourists**
   - **Username**: `tourist`
   - **Password**: `{iSchoolUI}`
   - **Privileges**:
     - View and add reviews
     - View cities, countries, events, landmarks, museums, and restaurants
     - Not allowed to view hotels

2. **Tourist Guides**
   - **Username**: `touristguide`
   - **Password**: `{iSchoolUI}`
   - **Privileges**:
     - View, add, change, and delete cities, countries, events, hotels, landmarks, and restaurants
     - Cannot view museums
     - Can add tours and activities to events and hotels

3. **Testers**
   - **Username**: `tester`
   - **Password**: `{iSchoolUI}`
   - **Privileges**:
     - Superuser access
     - View, add, change, and delete cities, countries, events, hotels, landmarks, museums, restaurants, and reviews
     - Extensive permissions for testing and quality assurance

### Administrative Users
1. **Sysadmins**
   - **Username**: `sysadmin1`
   - **Password**: `{iSchoolUI}`
   - **Privileges**:
     - Superuser access
     - Full control over the application
     - Manage all entities, including cities, countries, events, hotels, landmarks, museums, restaurants, and reviews

2. **Citizens**
   - **Username**: `citizen`
   - **Password**: `{iSchoolUI}`
   - **Privileges**:
     - View-only access to cities, countries, events, hotels, landmarks, museums, restaurants, and reviews
     - Part of the "ci_user" group

---

## Authentication and Authorization Scheme
The application leverages Django’s built-in authentication and permission system.

### Spreadsheets
- Group permissions and user data are defined in spreadsheets:
  - `group_permissions_finalproject`
  - `users_for_finalproject`

### Permissions Overview
1. **Tourists**: Limited view permissions with the ability to add reviews.
2. **Tourist Guides**: Advanced permissions, including adding and managing entities.
3. **Testers**: Full access for testing purposes.
4. **Sysadmins**: Complete administrative control with superuser privileges.
5. **Citizens**: Basic viewing permissions.

---

## Testing Instructions
1. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```
2. **Access the Application**:
   - Navigate to the local server URL (e.g., `http://localhost:8000/`).
3. **Log in as Different Users**:
   - Use the provided credentials for each user type to test their respective features.
4. **Test Functionalities**:
   - Browse cities, events, and other entities.
   - Test adding, editing, and deleting entities (for users with the required permissions).
   - Leave reviews and validate user permissions.

---

## Key Features
- **User Roles**:
  - Differentiated user roles with distinct permissions for regular users and administrators.
- **Responsive Design**:
  - Ensures consistent user experience across devices.
- **Code Quality**:
  - Adheres to PEP 8 and Django best practices.
- **Authentication**:
  - Secure username-password-based authentication.
- **Authorization**:
  - Fine-grained access control with group-based permissions.

---

## Relevant Information
- **Responsive Design**: Mobile-friendly layout for seamless usage on various devices.  
- **Code Style**: Follows PEP 8 and includes comments/docstrings for clarity.  
- **Documentation**: Refer to inline comments and docstrings for further details on specific modules, classes, or functions.
