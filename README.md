# Yggdrasil

## Description

**Yggdrasil** is a web application for creating and managing family trees. Users can register, add people, define relationships, and visualize their family history in a structured and interactive way. The app supports multiple languages and country information, making it suitable for international use.
The Website is made by two Apps. "Familytree" which is the main component and "People of History" which is a small feature to learn about important People of History.

## Live Version

You can try the application here: [Yggdrasil Live Version](You can try the application here: [Yggdrasil Live Version](https://your-yggdrasil-app.herokuapp.com))

To access an account without logging in use following login information:
- Username: MainTester
- Password: 2Amag2SkkP27iA5

![Yggdrasil Start view](./readme-images/homepage/start-view.png)

![Yggdrasil Start view](./readme-images/homepage/start-view-two.png)

![Yggdrasil Start view](./readme-images/homepage/start-view-three.png)

![Yggdrasil Start view](./readme-images/homepage/start-view-four.png)

![Yggdrasil Start view](./readme-images/homepage/start-view-five.png)

![Sign in view](./readme-images/signUps/sign-in.png)

![Sign up view](./readme-images/signUps/sign-up.png)

![Logout view](./readme-images/signUps/sign-out.png)

![Family detailed view](./readme-images/detail-view/detail-view.png)

![Yggdrasil person of the day view](./readme-images/person-of-the-day/person-of-the-day.png)

![Yggdrasil person of the day view](./readme-images/person-of-the-day/person-of-the-day-two.png)

![Family single view](./readme-images/family-view/singel-view.png)

![Family parents view](./readme-images/family-view/parents-view.png)

![Family siblings view](./readme-images/family-view/siblings-view.png)

![Family partner view](./readme-images/family-view/partner-view.png)

![Family children view](./readme-images/family-view/children-view.png)

![Entire family view](./readme-images/entire-view/entire-view.png)

![Family detailed view](./readme-images/detail-view/detail-view.png)

![Edit view](./readme-images/edit-person/edit-person.png)

![Yggdrasil faq view](./readme-images/faq/faq.png)

![Yggdrasil legal notice](./readme-images/footer-links/legal-notice.png)

![Yggdrasil privacy-polic](./readme-images/footer-links/privacy-policy.png)

## Features

### Core Features

- **User Registration & Login:**  
  Users can create an account, log in, and manage their own family trees.

  ![Sign in view](./readme-images/signUps/sign-in.png)

  ![Sign up view](./readme-images/signUps/sign-up.png)

  ![Logout view](./readme-images/signUps/sign-out.png)

- **Automatic Family Tree Creation:**  
  A family tree is automatically created for each user when they add their first person.

- **Person Management:**  
  - Add, edit, and delete people.
  - Assign birth and death dates, biography, nationality, and languages.
  - Upload a profile picture (Cloudinary integration).

  ![Edit view](./readme-images/edit-person/edit-person.png)

- **Relationship Management:**  
  - Assign parents, children, partners, and siblings.
  - Relationships are clearly displayed in the family tree.

  ![Family parents view](./readme-images/family-view/parents-view.png)

  ![Family siblings view](./readme-images/family-view/siblings-view.png)

  ![Family partner view](./readme-images/family-view/partner-view.png)

  ![Family children view](./readme-images/family-view/children-view.png)

- **Multilingual & Country Support:**  
  - Select native language(s) and nationality for each person.
  - Many languages and countries available via dropdowns.

  ![Language selection](./readme-images/languages/language-selection.png)

  ![Language selection](./readme-images/languages/language-selection-two.png)

- **Responsive Design:**  
  The app is optimized for both desktop and mobile devices.

### User Interface

- **Intuitive Navigation:**  
  Clear menus and user guidance.

  ![Navbar](./readme-images/navbar/navbar.png)

  *The Navbar on mobile phone*

  ![Navbar mobile view](./readme-images/navbar/navbar-mobile.png)

  ![Navbar mobile view](./readme-images/navbar/navbar-mobile-two.png)

- **Dynamic Visualization:**  
  Family structures are displayed in an organized way.

  ![Family detailed view](./readme-images/detail-view/detail-view.png)

- **Feedback & Validation:**  
  Users receive feedback for invalid input and successful actions.

  *Successful Person update*
  ![Successful Person view](./readme-images/messages/update-success.png)
  
  *Successful delete*
  ![Successful delete view](./readme-images/messages/delete-success.png)

  *Wrong input when adding a Person*
  ![Wrong input when adding a Person view](./readme-images/messages/wrong-input.png)

### User Interface and Experience

Yggdrasil offers a clean and intuitive user interface designed to make managing family trees simple and enjoyable for users of all technical backgrounds. The navigation is straightforward, with clear menus and logical page layouts that guide users through the process of adding people, defining relationships, and exploring their family tree.

Key aspects of the user experience include:

- **Responsive Design:**  
  The interface adapts seamlessly to both desktop and mobile devices, ensuring accessibility and usability on any screen size.

- **Clear Feedback:**  
  Users receive immediate feedback on their actions, such as confirmation messages when a person is added or relationships are updated, as well as helpful error messages for invalid input.

- **Guided Actions:**  
  Step-by-step forms and prompts help users enter information accurately and efficiently, reducing the chance of mistakes.

- **Visual Organization:**  
  Family members and their relationships are displayed in a structured and visually appealing way, making it easy to understand complex family connections at a glance.

- **Accessibility:**  
  The application uses readable fonts, sufficient contrast, and accessible navigation to ensure a positive experience for all users.

Overall, Yggdrasil focuses on providing a smooth, user-friendly experience that makes building and exploring family trees both easy and engaging.

## Workprocess

### Planning & Design

The planning and design phase for Yggdrasil focused on creating a user-friendly and scalable family tree application. Initial brainstorming sessions were used to define the core features, user flows, and technical requirements. Wireframes and flowcharts were created to visualize the main pages, navigation structure, and the relationships between different components of the app.

Key considerations during the design process included:

- **User Experience:** Ensuring that users of all technical backgrounds can easily navigate the application, add people, and define relationships without confusion.
- **Data Structure:** Designing database models that efficiently represent people, relationships, languages, and countries, while allowing for future expansion.
- **Responsiveness:** Planning a layout that adapts well to both desktop and mobile devices.
- **Internationalization:** Including support for multiple languages and countries from the start to make the app accessible to a global audience.
- **Security:** Incorporating secure authentication and data privacy best practices.

Throughout the planning stage, feedback from potential users and mentors was considered to refine the feature set and interface. The design was iteratively improved based on this feedback, resulting in a clear, logical, and visually appealing structure that supports the core goal of helping users build and explore their family trees with ease.

### Balsamiq wireframe

To begin the project, I created wireframes using Balsamiq. These wireframes allowed me to visualize the overall structure and design of the project. This step was crucial in translating abstract ideas into tangible layouts, ensuring that the design would align with the game's core objectives. Although the interface changed fundamentally later on during the process the foundation was build on these wireframes.

![Wireframe start page](./readme-images/wireframe/start-page.png)

![Wireframe login page](./readme-images/wireframe/log-in-page.png)

![Wireframe sign up](./readme-images/wireframe/sign-up.png)

![Wireframe New user - Start page](./readme-images/wireframe/new-user-start-page.png)

![Wireframe New User - Adding parents](./readme-images/wireframe/new-user-adding-parents.png)

![Wireframe New User - Adding Siblings](./readme-images/wireframe/new-user-adding-siblings.png)

![Wireframe New User - Adding children](./readme-images/wireframe/new-user-adding-children.png)

![Wireframe New User - Adding partner ](./readme-images/wireframe/new-user-adding-partner.png)

![Wireframe New user - only input himself](./readme-images/wireframe/new-user-only-input-himself.png)

![Wireframe main user with entered partner](./readme-images/wireframe/main-user-with-entered-partner.png)

![Wireframe main user with visibale partner](./readme-images/wireframe/main-user-with-visibale-partner.png)

![Wireframe main user with entered all](./readme-images/wireframe/main-user-with-entered-all.png)

![Wireframe main user with visible](./readme-images/wireframe/main-user-with-visible.png)

![Wireframe main user with visible two](./readme-images/wireframe/main-user-with-visible-two.png)

![Wireframe Add Premium](./readme-images/wireframe/add-premium.png)

![Wireframe Start POV](./readme-images/wireframe/start-POV.png)

Due to the already large scale of the project i waived the "login point of views"

### Flowchart

After the wireframe stage, I used Miro to further refine the proeject's structure and flow. Miro served as a dynamic tool for visualizing both the project's mechanics and its underlying code. This flowchart outlines the systematic, from login to the process of fetching Data and displaying it to the correct Person. Although i worked with a "POV-System" in the Workflow and Wireframes the conncept is the same for a group of different users:

1. Login Display
The login display is the user's entry point to Yggdrasil. It was designed to be simple and welcoming, allowing users to quickly access their family trees or create a new account. The login page provides clear options for both returning users and new registrations, ensuring a smooth onboarding process. User authentication is handled securely, and upon successful login, users are redirected to their personalized dashboard, where they can immediately start building or exploring their family tree.

![Log in](./readme-images/workflow/user-login.png)

2. Data-Base and POVs
The database structure is at the core of Yggdrasil, enabling efficient storage and retrieval of family data. Each user is associated with their own family tree, and all persons, relationships, and attributes are linked through well-defined models. The concept of "POV" (Point of View) is used to determine which person is currently being viewed or edited within the tree. This approach allows users to navigate complex family structures intuitively, always knowing whose perspective they are seeing. The backend ensures data integrity and consistency, so that relationships and family connections are accurately represented and easy to manage.

![Data base](./readme-images/workflow/data-base-and-pov.png)

This structured approach allowed me to stay organized and focus on the most critical elements of the project. Each step provided a clear roadmap for the development process, ensuring that the data base and interactions between elements were cohesive and aligned with the original vision.

## User Stories

I created user storys which i expected for a standard website. I skipped some featuers due to time reasons while still maintaining the most importend features of the website and completing the project as a whole project.

#### **First Time Visitor Goals**

| Issue ID    | User Story |
|-------------|-------------|
|[#1.1](https://github.com/fairytaib/Yggdrasil/issues/1)| As a new user, I want to register an account, so that I can manage my family tree digitally. |
|[#1.2](https://github.com/fairytaib/Yggdrasil/issues/2)|As a registered user, I want to log in with my email and password, so that I can access my family tree.|
|[#1.3](https://github.com/fairytaib/Yggdrasil/issues/3)|As a registered user, I want to reset my password, so that I can regain access to my account if I forget my password.|
|[#1.4](https://github.com/fairytaib/Yggdrasil/issues/12)|As a First Time Visitor, I want to be able to find the app useful, so that I can use it according to my needs.|


#### **Active App User**

| Issue ID    | User Story |
|-------------|-------------|
|[#2.1](https://github.com/fairytaib/Yggdrasil/issues/4)| As a user, I want to add new family members, so that I can build my family tree.|
|[#2.2](https://github.com/fairytaib/Yggdrasil/issues/5)|As a user, I want to edit existing family members, so that I can update their details (e.g., name, birthdate).|
|[#2.3](https://github.com/fairytaib/Yggdrasil/issues/6)|As a user, I want to delete a family member, so that I can keep my family tree up to date.|
|[#2.4](https://github.com/fairytaib/Yggdrasil/issues/7)|As a user, I want to switch between different perspectives, so that I can see either my parents & siblings or my children & partner.|

#### **Mobile User**

| Issue ID    | User Story |
|-------------|-------------|
|[#3.1](https://github.com/fairytaib/Yggdrasil/issues/8)| As a user, I want a mobile-friendly interface, so that I can manage my family tree on my phone.|

#### **Users Privacy Concerns**

| Issue ID    | User Story |
|-------------|-------------|
|[#4.1](https://github.com/fairytaib/Yggdrasil/issues/9)| As a user, I want my family data to remain private, so that only I can access it.|
|[#4.2](https://github.com/fairytaib/Yggdrasil/issues/10)|As a user, I want my images to be securely stored, so that my data is safe and private.|
|[#4.3](https://github.com/fairytaib/Yggdrasil/issues/6)|As a user, I want to delete a family member, so that I can keep my family tree up to date.|
|[#4.4](https://github.com/fairytaib/Yggdrasil/issues/7)|As a user, I want to switch between different perspectives, so that I can see either my parents & siblings or my children & partner.|

#### **Developer**

| Issue ID    | User Story |
|-------------|-------------|
|[#5.1](https://github.com/fairytaib/Yggdrasil/issues/11)| As a developer, I want the application to run on Heroku, so that it is always accessible online.|


## Testing and Validation

### Manual Functionality Testing

Manual functionality testing was carried out to ensure that all core features of Yggdrasil work as intended and provide a smooth user experience. The following aspects were tested:

- **User Registration and Authentication:**  
  Verified that users can register, log in, and log out successfully. Checked that authentication is required to access personal family trees.

- **Family Tree Creation:**  
  Confirmed that a new family tree is automatically created when a user adds their first person.

- **Person Management:**  
  Tested adding, editing, and deleting people. Ensured that all fields (name, birth/death dates, biography, nationality, languages, and profile picture) can be entered and updated correctly.

- **Relationship Management:**  
  Checked that users can assign parents, children, partners, and siblings, and that these relationships are displayed accurately in the family tree.

- **Language and Country Selection:**  
  Verified that users can select multiple languages and a country for each person, and that these selections are saved and displayed properly.

- **Image Upload:**  
  Ensured that profile pictures can be uploaded and displayed using Cloudinary integration.

- **Navigation and User Interface:**  
  Confirmed that all navigation links, buttons, and forms work as expected on both desktop and mobile devices.

- **Feedback and Validation:**  
  Checked that users receive appropriate feedback for successful actions and error messages for invalid input.

- **Responsive Design:**  
  Tested the application on different screen sizes to ensure that the layout adapts and remains user-friendly.

  - Homepage:

    ![Mobile view Homepage](./readme-images/Validation/responsivness/home.png)
  
    ![Mobile view Homepage lower section](./readme-images/Validation/responsivness/home-two.png)

  - People of History:
  
    ![Mobile view People of History](./readme-images/Validation/responsivness/peopleOfHistory.png)

  - Family view:
  
    ![Mobile view Family view](./readme-images/Validation/responsivness/view_family.png)

  - Classic familytree:
  
    ![Mobile view classic Familytree](./readme-images/Validation/responsivness/family_tree.png)

  - View details:
  
    ![Mobile view View Details](./readme-images/Validation/responsivness/view_details.png)

  - Edit person:
  
    ![Mobile view edit person](./readme-images/Validation/responsivness/edit_person.png)

All major user flows were tested manually, and any issues discovered during testing were addressed and resolved to ensure a reliable and intuitive experience for all users.

### Django unit testing

At the very beginning of the project, I decided to use Django's built-in unit testing framework.

I am running the following testing commands in my terminal to test the code:

```
python3 manage.py test <name of the app>
```

To create the coverage report, I run the following command:

```
coverage run --source=<name of the app> manage.py test
```

```
coverage report
```

To see the html version of the report and find out whether some pieces of code are missing, I run the following command:

```
coverage html
```

```
python3 -m http.server
```

**Automated Testing results**

As there are four main apps in the project, we can test them separately.
I knew at the very beginning that I had to implement automated testing. As I was highly concentrated on developing all functionality first, so I left testing to the end. While testing my work, I found that each time a new Person was entered by the same user a new Familytree instance was created. I fixed this problem along with the testing process.

**Familytree**

![Familytree Coverage](./readme-images/automated-testing/familytree.png)

**People of History**

![People Of History Coverage](./readme-images/automated-testing/peopleOfHistory.png)


### Code Validation 
 **HTML**:
  Due to [W3C](https://validator.w3.org/nu/) beeing unable to render/validate Django-templates, i opend the source code and copied it directly into the validator.
  
  - Homepage: ![HTML Homepage validation](./readme-images/Validation/html-validation/homepage.png)

  - People of History: ![People of History](./readme-images/Validation/html-validation/people-of-history.png)

  - FAQ: ![FAQ](./readme-images/Validation/html-validation/faq.png)

  - Adding a family member: ![Adding a family member](./readme-images/Validation/html-validation/add-person.png)

  - Family view: ![Family view](./readme-images/Validation/html-validation/family-view.png)

  - Deleting a family member: ![Deleting a family member](./readme-images/Validation/html-validation/deleting-person.png)

  - Editing a family member: ![Editing a family member](./readme-images/Validation/html-validation/edit-person.png)

  - Entire Family view: ![Entire Family view](./readme-images/Validation/html-validation/entire-view.png)

  - Viewing details: ![Viewing details](./readme-images/Validation/html-validation/view-details.png)

  **CSS**
  CSS was also tested via direct insertion of the code into the [W3C validator](https://jigsaw.w3.org/css-validator/validator). Due to my cookies the output was in german but you can cleary see the success message.

  - Base Css: ![Base Css](./readme-images/Validation/css-validation/base.png)

  - Homepage: ![Homepage](./readme-images/Validation/css-validation/home.png)

  - People of History: ![People of History](./readme-images/Validation/css-validation/people-of-history.png)

  - FAQ: ![FAQ](./readme-images/Validation/css-validation/faq.png)

  - Forms: ![Forms](./readme-images/Validation/css-validation/edit.png)

  - Family view: ![Family view](./readme-images/Validation/css-validation/family-view.png)

  - Deleting a family member: ![Deleting a family member](./readme-images/Validation/css-validation/delete.png)

  - Entire Family view: ![Entire Family view](./readme-images/Validation/css-validation/entire-view.png)

  - Viewing details: ![Viewing details](./readme-images/Validation/css-validation/view-details.png)

  **Javascript**
  In this project i only used three short javascript files and validated them with [jshint](https://jshint.com):

  - Base.js: ![Base.js](./readme-images/Validation/javascript-validation/base.png)

  - Add_unknown_parent.js: ![Add unknown Parent](./readme-images/Validation/javascript-validation/add-unknown-parent.png)

  - family_view.js: ![Add unknown Parent](./readme-images/Validation/javascript-validation/family_view.png)

  **Python**
  I validated the code with Code Institutes [Python Linter](https://pep8ci.herokuapp.com):

  **People of History**
  
  - Admin.py: ![Admin.py](./readme-images/Validation/python-validation/people-of-history/admin.png)

  - Apps.py: ![Apps.py](./readme-images/Validation/python-validation/people-of-history/apps.png)

  - Models.py: ![Models.py](./readme-images/Validation/python-validation/people-of-history/models.png)

  - Tests.py: ![Tests.py](./readme-images/Validation/python-validation/people-of-history/tests.png)

  - Urls.py: ![Urls.py](./readme-images/Validation/python-validation/people-of-history/url.png)

  - Views.py: ![Views.py](./readme-images/Validation/python-validation/people-of-history/views.png)

  **Family Tree**
  The linter warning E227/E225: missing whitespace around bitwise or shift operator may appear falsely when using & inside f-strings for URL parameters. This is not an actual error and can be safely ignored or avoided by building the URL in multiple lines.

  - Admin.py: ![Admin.py](./readme-images/Validation/python-validation/familytree/admin.png)

  - Apps.py: ![Apps.py](./readme-images/Validation/python-validation/familytree/apps.png)

  - Context_proecessors.py: ![Context_proecessors.py](./readme-images/Validation/python-validation/familytree/context_processor.png)

  - forms.py: ![forms.py](./readme-images/Validation/python-validation/familytree/forms.png)

  - Models.py: ![Models.py](./readme-images/Validation/python-validation/familytree/models.png)

  - Signals.py: ![Signals.py](./readme-images/Validation/python-validation/familytree/signals.png)

  - Tests:

    - Add family Member :![Add family Member](./readme-images/Validation/python-validation/familytree/tests/add-family-member.png)
    - Add self :![Add self](./readme-images/Validation/python-validation/familytree/tests/add-self.png)
    - Delete Person :![Delete Person](./readme-images/Validation/python-validation/familytree/tests/delete-person.png)
    - Edge Cases :![Edge Cases](./readme-images/Validation/python-validation/familytree/tests/edge-cases.png)
    - Edit person :![Edit person](./readme-images/Validation/python-validation/familytree/tests/edit-person.png)
    - Entire View :![Entire View](./readme-images/Validation/python-validation/familytree/tests/entire-tree-view.png)
    - Family relation form :![Family relation form](./readme-images/Validation/python-validation/familytree/tests/family-relation-model.png)
    - Family relation model :![Family relation model](./readme-images/Validation/python-validation/familytree/tests/family-relation-model.png)
    - Familytree model :![Familytree model](./readme-images/Validation/python-validation/familytree/tests/familytree-model.png)
    - Get owner file :![Get owner file](./readme-images/Validation/python-validation/familytree/tests/get-owner.png)
    - Person form :![Person form](./readme-images/Validation/python-validation/familytree/tests/person-form.png)
    - Person model :![Person model](./readme-images/Validation/python-validation/familytree/tests/person-model.png)
    - Tree tags :![Tree tags](./readme-images/Validation/python-validation/familytree/tests/tree-tags.png)
    - View Details :![View Details](./readme-images/Validation/python-validation/familytree/tests/view-details.png)
    - View Family :![View Family](./readme-images/Validation/python-validation/familytree/tests/view-family.png)


  - Urls.py: ![Urls.py](./readme-images/Validation/python-validation/familytree/urls.png)

  - Views.py: ![Views.py](./readme-images/Validation/python-validation/familytree/views.png)
    
# Lighthouse performance rating

  The website was evaluated using Google's Lighthouse extension and received the following performance ratings. Due to the necessity to login it seems lighthouse was blocked for all pages that where a login is requiered. This project uses Cloudinary to serve dynamic images.

  Also Lighthouse may report a mixed content warning (http:// request inside an https:// page), even though Cloudinary automatically upgrades all requests to HTTPS.

  All image resources are securely delivered via HTTPS in production.
  There is no actual security risk, and the warning can safely be ignored.

  Cloudinary’s automatic upgrade ensures end-to-end encryption, and the project is fully compliant with web security best practices.

  - Homepage: I wasn't able to increase the performance rating to 100 due to lack of time.
  ![Homepage](./readme-images/Validation/lighthouse-performance/home.png)

  - FAQ: ![FAQ](./readme-images/Validation/lighthouse-performance/faq.png)

  - Legal Notice: ![Legal Notice](./readme-images/Validation/lighthouse-performance/legal-notice.png)

  - Privacy Policy: ![Privacy Policy](./readme-images/Validation/lighthouse-performance/privacy-policy.png)

  - Signup: ![Signup](./readme-images/Validation/lighthouse-performance/signup.png)

  - Login: ![Login](./readme-images/Validation/lighthouse-performance/login.png)

### Development Tools

- **Python Linter**: Code validation conducted using [CI Python Linter](https://pep8ci.herokuapp.com/#).
- **Git**: Version control handled with [Git](https://git-scm.com/).
- **GitHub**: Cloud-based platform for storing and sharing code via [GitHub](https://github.com/).
- **Heroku**: Used for deploying and hosting the game, enabling live testing and accessibility on [Heroku](https://www.heroku.com/home).
- **VS Studio Code**: Text editor for coding

## Technologies Used

- **Backend:**  
  - Python 3  
  - Django  
  - PostgreSQL  
  - Cloudinary (for image hosting)

- **Frontend:**  
  - HTML5  
  - CSS3  
  - JavaScript (for dynamic UI)

- **Other:**  
  - Django-Allauth (authentication)
  - pycountry (country data)
  - multiselectfield (multi-language selection)
  - Heroku (deployment)

- **Version Control**:

  - Git: Used for version control to track changes and manage the development process.
  - GitHub: Used as a cloud-based platform to store and share the code repository.
  - Heroku: The game is deployed on Heroku, allowing easy access and testing in a live environment.

- **Extras**
  - Miro: Used for planning and visualizing game structure, creating flowcharts, and collaborating on gameplay mechanics.

## Setup & Installation

### Prerequisites

To run Yggdrasil locally, ensure you have:

- **Python 3.x** installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).
- **Git** installed to clone the repository. Download it from [git-scm.com](https://git-scm.com/).

### Installation

1. **Clone the repository**  
   Open a terminal and run:
   ```sh
   git clone https://github.com/fairytaib/yggdrasil-two.git
   ```
2. **Navigate to the folder**
   ```Sh
   cd yggdrasil-two
   ```
3. **Create and activate a virtual environment**

   This ensures that all dependencies are installed in an isolated environment and do not clutter your global Python installation.

- On Windows
  ```sh
  python -m venv venv
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```sh
  python -m venv venv
  venv\Scripts\activate
  ```

4. **Install dependencies**

   Instead of installing libraries manually, install all required dependencies from the requirements.txt file:

   ```sh
   pip install -r requirements.txt
   ```

5. **Run the website**

Open your terminal and run the command:

```sh
py manage.py runserver
```

#### Deactivating the Virtual Environment

Once you are done, you can deactivate the virtual environment by typing CTRL + C

### Deployment

To deploy Yggdrasil on **Heroku** using their web interface, follow these steps:

#### 1. Create a Heroku Account

- Go to [Heroku](https://www.heroku.com/) and sign up for a free account if you don’t have one.

  ![Heroku Homepage](readme-images/heroku-images/heroku-home.png)

#### 2. Create a New Heroku App

- Log in to your Heroku dashboard.
- Click **"New" → "Create new app"**.
- Enter a unique app name and choose a region (e.g., Europe or United States).
- Click **"Create app"**.
  ![Heroku New App](readme-images/heroku-images/create-new-app.png)
  ![Heroku New App](readme-images/heroku-images/create-new-app-two.png)

#### 3. Connect to GitHub

- In the **"Deploy"** tab, find the **"Deployment method"** section.
- Select **GitHub** and click **"Connect to GitHub"**.
- Search for your Hangman repository and connect it.

  ![Heroku New App](readme-images/heroku-images/connect-github.png)

#### 4. Configure Buildpacks

- In the **"Settings"** tab, scroll down to **"Buildpacks"** and click **"Add buildpack"**.
- Add **Python** and **NodeJs** as a buildpack.

  ![Heroku New App](readme-images/heroku-images/connect-github.png)

- Scroll down to **"Config Vars"** and following Keys and their corresponding values.

  ![Heroku New App](readme-images/heroku-images/keys.png)

- Add other needed **Config Vars** for your databases etc.

#### 5. Deploy the Application

- Go back to the **"Deploy"** tab.
- Under **"Manual deploy"**, choose the branch (usually `main` or `master`).
- Click **"Deploy Branch"** to start the deployment.
- Wait for the build process to complete. If successful, Heroku will provide a link to your live app.

  ![Heroku New App](readme-images/heroku-images/deploy-view.png)

#### 6. Enable Automatic Deployments (Optional)

- In the **"Automatic deploys"** section, click **"Enable Automatic Deploys"** to deploy new changes automatically when you push updates to GitHub.

#### 7. Run the App

- Click **"Open app"** in the top-right corner of the Heroku dashboard to view your deployed Hangman game.

  ![Heroku New App](readme-images/heroku-images/open-app.png)

## Bugs Encountered, Solutions, and General Observations

### Bugs and Problems encountered
- **Django Views and URLs**: It took me some time to fully understand how Django views and URL routing work. Setting up the correct connections between views, templates, and URLs required careful reading of the documentation and some trial and error.

- **Design Problem**: The initial design of the family view, as shown in the wireframes, could not be fully implemented. Creating an aesthetically pleasing mobile view proved to be very challenging, especially for families with multiple members, which led to display issues and usability problems on smaller screens.

- **Info Button**: For some reason, the info button sometimes loses its color after being pressed. I have found no solution, and this must be an internal problem within Bootstrap.
  - Normal:
  
    ![Heroku New App](readme-images/bugs/info-button-normal.png)
  - The bug:

    ![Heroku New App](readme-images/bugs/info-button-bug.png)

- **Wrong Spelling**: When creating the "People of History" App i didn't go with the standard spelling (snake-case) in Django/Python. Changing it afterwards could cause problems so i leave it at that and mention it here

## Future Plans
 - **Editing Relationships**: Currently the initialy selected Relationship cannot be changed. In further updates this is supposed to be changed in an intuitive way 

 - **Uploading Images**: In future updates the User will be able to upload and create his own Gallery at the correspondings persons profile

 - **HTMX / React**: For a better User experience it is planned to switch to HTMX or React. This feature was planned for the initial Website but was postponed due to time reasons.

- **Parent connection**: When parents are added, there is no direct relationship linking them as partners. This is because a person can have, for example, both a biological parent and a foster parent who are not in a relationship with each other. In the future, there will be an option to select a person from the family list to avoid creating duplicate entries.

## Disclaimer

- The contact information provided on the website is not real and is included only as placeholder content for demonstration purposes.

## Credits

**Creative Content**

- **ChatGpt**: Creating Images and Logos
- **Miro**: [Miro](https://miro.com/de/) was my tool to create and visualize my pseudo-code
- **Wireframe**: My Page layout was created with the tool [Balsamiq](https://balsamiq.com/)

**Content and Tutorials**

- **Stack Overflow**: All kinds of different questions and anwsers from [Stack Overflow](https://stackoverflow.com/).

- **Django documentation**: For in depth questions or specific questions i used the offical [Django documentation](https://docs.djangoproject.com/en/5.2/)

**Libraries**

The following libraries and packages were used in this project (as listed in `requirements.txt`):

- **Django**: The main web framework used to build the application.
- **dj-database-url**: Simplifies database configuration from environment variables.
- **gunicorn**: WSGI HTTP server for deploying Django applications.
- **psycopg2-binary**: PostgreSQL database adapter for Python.
- **cloudinary**: Integration for image upload and management via Cloudinary.
- **django-allauth**: Provides authentication, registration, and account management.
- **pycountry**: Provides ISO country, subdivision, language, currency and script definitions.
- **django-multiselectfield**: Allows the use of multi-select fields in Django models.
- **whitenoise**: Simplifies static file serving for Django apps.
- **pillow**: Python Imaging Library, used for image processing.
- **crispy-bootstrap5**: Django Crispy Forms template pack for Bootstrap 5.
- **django-crispy-forms**: Helps to manage Django forms rendering.
- **dj3-cloudinary-storage**: Cloudinary storage backend for Django.
- **python-dotenv**: Loads environment variables from a `.env` file.
- **requests**: Allows sending HTTP requests easily.
- **gunicorn**: Production WSGI server for running Django apps.


**Mentoring and Guidance**

- **Iuliia Konovalova**: Mentoring and guidance by [Iuliia Konovalova](https://github.com/IuliiaKonovalova).

- **Code Institute & Code Institute Student Support**: Helping me debugg specific difficultys and learning needed content