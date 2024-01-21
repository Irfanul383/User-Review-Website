# **Process Model Analysis**

**Introduction:**

This document describes the process model that we implemented for our project sprint 2.

**Product:**

A website where users can login with their credentials, create new topics to be reviewed and leave point-based reviews.

**Product backlog:**

Below are the features we currently have in our product backlog:

1. Make draft reviews
2. Bookmark reviews

**Sprint backlog:**

Below are the features we had in our sprint 2 backlog:

1. Make logic for anonymous button
2. Sort by topic
3. Session management for multiple users
4. Handle post topic
5. Handle post reviews
6. Add function to get logged in user
7. An auto tagging feature

**Sprint:**

Sprint 2 was 2 and a half weeks (19 days) long.

**Process overview:**

The software development process that we followed during the development period is an agile approach with incremental development and this process encompasses the entire software development lifecycle.

**Process steps:**

**Requirement gathering:**

- The required resource to initiate the sprint 2 for the project were the instructions and notes provided by professor in his website.
- We asked professor for further clarification/information about the resources provided and the requirements outlined on the website so we would have a clear understanding of what we had to build and how to design and implement the project.
- Each of us researched online to find instructions on using different python modules used in our project and ways to make our code more concise.
- We repeated these steps throughout the complete sprint cycle.

**Design:**

- We had to design how users would access and interact with our website. For example: we first created a visual diagram of what we would want the user to see as they first clicked the website and as they interacted with each component such as each of the buttons or each text fields or each page of the website.
- Then we discussed the design for the development process such as the basic infrastructure and the frontend and backend components to build and in what order to build them and how they would interact with each other.
- Although we made an overall design at the beginning of our sprint cycle we had to change and redesign multiple times during the sprint as we were facing logic issues with implementing the initial pattern because we were not very thorough with the design.

**Activities:**

**Creation:** During sprint 1 after we had the required resources and an initial design to start our project we created activities and broke all activity into a total of 5 components and created tasks corresponding to each component. For sprint 2 we just followed that structure and the created new tasks for each component.

**Evaluation:** After pull requests were created for each task we reviewed them in our meetings and either merged the PRs or suggested improvements to be made. Each activity was evaluated by observing the overall outcome and evaluation of the tasks associated with that activity. If all the tasks belonging to an activity showed desired outcome then that activity was considered to have been completed. However, if any of the tasks of an activity had some problem in it then that activity was not complete until all the problems related to the task were not resolved.

**Start and completion:** The start of each activity was triggered during the design phase when we agreed on how to design our development process and the completion of each activity is when all the key tasks associated with that activity are completed and the codes are merged with the main project through pull requests after reviewing the code in team meetings.

**Tasks:** Tasks are created in Kanban board. We divided all activities into a total of 5 components in sprint 1 and each person in the group was assigned 1 component based on team discussion and what each person felt confidence in accomplishing. In our sprint 2 backlog we created tasks which were assigned to the person who was already in charge of that specific component that the tasks belong to. For each task PRs were created and we reviewed the code in team meetings and either merged the PRs or suggested further improvements.

The process we adopted can be broken down two three distinct activities:

1. **Infrastructure Setup:** this involved establishing the groundwork for the website we are building and the outcome of this activity are three components of our project website which are a server, a database and a session management system. This activity involves creating basic building blocks for the website so there is an active website and the users can store their login and session info.

   **Relation:** This activity is related to frontend development as without the server the website will not be working and also to the backend development as without the database and session management the application logic will not be able to create the logic to control the website.

- **Key components:**

- Server:

Key tasks for server: 

Route the TPL files with appropriate methods

Map data to database

Route post review page

  - Database:

Key tasks for database: 

Create a topic table in database

Create a table for post review page

Update review table

- Session management:

Key tasks for session management:

Implement session management for multiple users

2. **Frontend Development:** this involved building the user interface for the website and one member of the development team was assigned to complete the key task.

   **Relation:** This activity is related to the infrastructure set up as without it the server would be ineffective. For out project frontend development did not directly overlap with the app logic, however, the app logic needed the server to work and the server depended on the frontend development so there is a secondary dependency.

- **Key Components:**

- Template file creation:

Key tasks for TPL file creation: 

Create Template (TPL) file for write review page

Create TPL file for write topic page.

Create TPL file for point based review page

3. **Backend Development:** this involved creating logic behind the application which governs how all the pieces of infrastructure and frontend interconnect together and build a functional website.

   **Relation:** This activity is related to the infrastructure setup as it requires the database, server files and the session management functions to create interconnection. One person was assigned the key task.

- **Key Components:**

- Application logic:

Key tasks for app logic: 

Develop application logic for handling the

routing methods for point based post review

page in server file

Logic for create new topic page

Logic for post review page

Make logic for handling the anonymous button

**Roles and responsibilities:**

- **Scrum master:** Each week one member of the team was in charge of guiding the team in the effective use of Scrum.
- **Development team:** The entire team of five of us participated in the development process.

Infrastructure Setup :

- Key tasks for server: Aaron Graab
- Key tasks for database: Emmanuel Otobo
- Key task for session management: Anika Farhad

Frontend Development:

- Key tasks for Template file creation: Mohammed Irfanul Haque

Backend Development:

Key tasks for app logic: Faraz Abdollahihaghi

**Incomplete tasks:**

- Could not implement sort by topic as we were not sure about how the feature should be implemented and by the time we got enough clarity we did not have enough time to finish it.
- Also, could not finish the auto tagging feature due to not having enough time for that.
- Could not implement session management for multiuser, in this sprint as bottle does not actually support simultaneous multiuser system because it is not multithreaded. Spent most of the time researching different ways to implement the system but ultimately could not find a working solution.

**Scrum:**

**Planning:** On our first scrum meeting we discussed the requirements set by professor for sprint 2 and based on that reviewed our product backlog and selected the two features which we wanted to implement this sprint; and in next few meetings we planned our sprint by designing the architecture for our project for sprint 2.

**Pull requests and code reviews:** After completing the key tasks the team members created PRs. During meetings we reviewed the code in the PRs. Each member participated in code reviews and provided feedback. The scope of reviews would be to discuss only the code in PR. We first checked if the code showed the desired outcome by running it and then we would walk through the code to see if it was properly de coupled and style looked clean and concise.

We discussed the rubrics and other resources for sprint2 that were provided by the professor. We also talked about how everybody was doing with their respective tasks and if they needed any support. Although we planned the sprint initially we still had to go back multiple times make changes to the initial plan. We had a total of 7 scrum meetings which were on Oct 23rd, Oct 24th, Oct 27th, Oct 30th, Nov 6th, Nov 7th and Nov 9th.

**Testing:** We were not able to create functional unit tests for all the modules for sprint2 so we manually tested them by running the application several times using different inputs and in different states. For example: we tried registering and logging into our website using each of the credentials, we created new topic and topic questions and we rated the topic questions to see if all the functionalities were working fine, we checked if the application was still running fine after any adjustments made.

**Performance reviews:** At the end of the sprint everybody provided feedback on other team members' performance.

**Changes made after sprint1:**

1. In the code reviews we made comments before merging the PRs as opposed to verbal suggestions that we provided during sprint 1.
2. We made sure to make properly labeled and color-coded cards in the Kanban board.
3. We described our project architecture and workflow in details as well as provided each member's overview on every minor task. We did not do this in sprint 1.

**Tools and technologies:**

- Design phase: We used a simple white board and a marker to design the visual diagram and illustrated the development process
- Development phase:

- To complete the tasks, we used PyCharm IDE and a web browser to run the website.

**Suggested improvements:**

1. We could not implement all the features from the sprint backlog as we lacked clarity and information regarding implementing those features. Our design did not include the details for the implementation which caused us run into problem when implementing logic for the features. In the next sprint we should try to gather all the necessary information in details within first few days of the sprint cycle.
2. Our pull request deadline was not set way ahead the actual deadline which we should have for the next sprint.
3. We were not able to design functional unit tests for all the modules due to lack of time. In the next sprint we should set a pull request deadline for the actual modules a number of days earlier so we can work on creating unit tests.
4. We were not supposed to code in modules outside our assigned components but we did not maintain that. We should change it for next sprint.

**Conclusion:** We added the necessary information to illustrate our process for sprint 2 in this process model analysis since a model is only an abstraction of an actual process and does not require all the details of a process. We excluded details such as intricate coding details, minor tasks such as booking a meeting place.