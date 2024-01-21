# Meeting Notes

## October 2nd, 2023
Time: 12pm – 1pm                      
SCRUM Master: Emmanuel                      
Note Taker: Aaron                      
Location: In Class                      
Attendance: All                      
Pre-Meeting Questions/ Goals:                      
-	Elect Note taker
-	Discuss project architecture.
-	Assign developer tasks.
-	Ensure members have read note 8.
-	Project repo invitation.
-	Doc folder.
Meeting Notes:                      
- Aaron is Dev 1, Faraz is Dev 2, Emmanuel is Dev 3, Irfanul is Dev 4, Anika is Dev 5.
- Aaron Elected as note taker.
- Got clarification about the assignment from Dr. Brown.
- Next meeting will be in the next class.
- Discussed Emmanuel’s ‘hello name’ server functions and how we think we want to build the server.
Pull Request Performance Reviews and Code Reviews:                      
-	NA

## October 3rd, 2023
Time: 12pm – 1pm                      
SCRUM Master: Anika                      
Note Taker: Irfanul                      
Location: In Class                      
Attendance: All                      
Pre-Meeting Questions/ Goals:                      
-	Figure out website template.
-	Decide framework.
-	Figure out how to deal with pull requests.
-	Discuss specific project outlines.
Professor Recommendations:                      
-	Elect notetaker (implied for all meetings), 
-	Discuss project architecture, assign general areas of responsibility for project code, 
-	Discuss strategy for initial tasks.
-	Decided to do meeting PR from previous meetings at next meetings.
-	Will go over code review and performance reviews at next meetings about previous meetings.
-	Ensure all members are up to date on coding standards and interface design (note 8) 
-	Add your own project-based agenda items.
Meeting Notes:                      
-	Going to use Bottle.
-	Website will strictly be HTML and not a combination of Java script/ CSS.
-	Pull requests will be strictly dealt with together in group meetings so we can comment and go over the code together before committing to Master.
-	Want to have code reviews and performance reviews during our meetings so we can go over code as a group before accepting pull requests.
-	Discussed with Dr. Bown details about the how to approach the framework and project expectations.
Pull Request Performance Reviews:                      
-	NA
Pull Request Code Reviews:                      
-	NA

## October 5th, 2023
Time: 1pm – 2pm, 2pm – 3pm                      
SCRUM Master: Irfanul                      
Note Taker: Anika                      
Location: Class, Library 5010A                      
Attendance: All                      
Pre-Meeting Questions/ Goals:                      
-	What do we want the page line up to look like?
-	How do we want to organize the files?
-	What files should we have for what specific tasks?
-	What database are we going to use? SQLite?
-	What server template are we using? Bottle? No framework?
-	How each person wants to implement their responsibilities/ tasks?
-	How our Github process should work? Only one person approving project specific PR? 
-	Aaron is the note taker, only he can directly push the notes to main?
-	How can we maybe take the workload off Emmanuel from PRs?
Professor Recommendations:                      
-	Setting up project issue tracker and KanBan board.
-	Set release cycle 1 schedule for final pull-requests.
-	Code reviews and performance reviews. 
-	Draft the software process for the project, 
-	Review the progress on defining service and module interfaces: the definitions should be stable soon.
-	Team agenda items: Scrum-master adds project-and-team based agenda items; members suggest new agenda items.
Meeting Notes:                      
-	Ask Dr. Brown about what topics we are supposed to include?
-	Ask Dr. Brown what he recommends for session management.
-	Drew diagrams of the page flow and button clicks.
-	Updated Trello.
-	Using SQLite.
-	What is a user, what is a review?
-	Talked about how to pull data for the review topic - individual vs group reviews.
-	Only one person can be logged in at once, when someone else logs in, it logs everyone else out.
-	Faraz: Work on 3 methods, attempt login, attempt register, and fetch draft into server.py.
-	Emmanuel: Creates SQL database and create write SQL operations and expose them as functions we can call.
-	Irfanul: Create a TPL file for HTML code templates for review page.
-	Anika: Draft Page.
-	Aaron: Login and Register Page, meeting notes.
-	app.py is where the server will be run from.
-	reviews folder that will have log in stuff?
-	If the browser goes to slash something, goes to that HTML template.
Pull Request Performance Reviews:                      
-	NA
Pull Request Code Reviews:                      
-	NA

## October 10th, 2023
Time: 1pm – 3pm                       
SCRUM Master: Faraz                      
Note Taker: Emmanuel                      
Location: Library 4016A                      
Attendance: All                      
Pre-Meeting Questions/ Goals:                      
-	Going over PR and approving them.
-	When is the next meeting date.
-	What are our tasks for the next meeting.
-	What will happen if there is an error in the registration page?
Professor Recommendations:                      
-	NA
Meeting Notes:                      
-	Went over PRs and merged to main.
-	Code Reviews and Performance Reviews.
-	Talked about SQLite database and how we want to store information.
-	Talked about routes and TPL files.
-	Talked about how to handle errors regarding usernames/ profile already existing.
-	How to pass data into a TPL file
-	Three errors to be passed: User doesn’t exist, if user is logged in, and if pw doesn’t match.
-	Talked about backend functions that will be needed.
-	For next meeting tasks - Due Thursday:
-	Aaron: Update notes and work on server code.
-	Anika: Work on session management code.
-	Emmanual: Write the DB methods for login/ register user, accept PR requests.
-	Irfanul: Work on HTML templates
-	Faraz: Login method, register method, specific logic.
Pull Request Performance Reviews from Oct 5th, 2023:
-	Everyone met the deadline of assigned tasks.
Pull Request Code Reviews from Oct 5th, 2023:                      
-	About Irfanul’s code:
o	Worked on review-list HTML template.
o	Emmanuel: Irfanul used anchors instead of routes. Changed before approving PR.
o	Faraz: Wanted to change the position of the buttons.
o	PR was approved.
-	About Aaron’s code:
o	Worked on login and register user HTML template page.
o	Emmanuel: Noticed naming convention for registered page could be simplified.
o	Anika: Wanted to remove redundant code.
-	About Anika’s code:
o	Worked on create review HTML template page.
o	Aaron: Wanted to rearrange HTML code for consistency.
-	About Emmanuel’s code:
o	Worked on setting up SQL database with tables and relationships.
o	Irfanul: Changed the names of the tables to singular form.
o	Faraz: Wanted to add topic table and linked it to the review table.
o	PR was approved.
-	About Faraz’s code:
o	Worked on login and register backend logic.
o	Anika: The login was successful the database entry was not changed.
o	Emmanuel: Implemented method in database to accommodate logins.
o	Faraz: Used Emmanuel’s method to change the database entry to logged in once log in is successful.
o	Approved the PR.

## October 12th, 2023
Time: 1pm – 3pm                      
SCRUM Master: Aaron                       
Note Taker: Faraz                      
Location: In Class                      
Attendance: All                      
Pre-Meeting Questions/ Goals:                      
-	Want to ask the professor specific questions about clarification.
-	Discuss next meeting goals.
Professor Recommendations:                      
-	Discuss user stories timeline and placement in the repo.
-	Meeting notes should be committed and pushed after each meeting so marking can assess whether meeting are being regularly help as intended. 
-	If your team is not doing this, you should start now. You might want to use a branch so the meeting notes are available even before they have been merged via pull-request.
Meeting Notes:                      
-	Asked Dr Brown what he means by types - groups vs individual.
-	Meeting to discuss marking template goals.
-	Aaron: Create a READ ME file for marking template.
-	Anika: Combine the review list page to the login button regardless of the logic being present.
-	Irfanul: Investigate logic code for username checking.
-	Emmanuel: Implementing database code and creating new table for topics.
-	Faraz: Working on user logic for logging in.
-	Decided to work on the project all together.
-	Want to meet Monday from 1-4pm to try to finish the project together as much as possible.
-	Will look at writing the test code by hand.
Pull Request Performance Reviews from Oct 10th, 2023:                      
-	Everyone did a good job and got the tasks done for the deadline.
Pull Request Code Reviews from Oct 10th, 2023:                      
-	About Irfanul’s code:
o	Worked on adjusting HTML interface.
o	Anika: Asked about anonymous checkbox when writing the review.
o	Irfanul: Added anonymous checkbox in HTML template.
o	PR was approved.
-	About Aaron’s code:
o	Updated meeting notes and set up server and database in entry point file.
o	PR was approved.
-	About Anika’s code:
o	Worked on implementing user authentication for users to log in and create accounts.
o	PR was approved.
-	About Emmanuel’s code:
o	Worked on functions that included SQL code to interact with the database.
o	Aaron: Wanted to add a decorator function to close database connection every time a new query was executed.
-	About Faraz’s code:
o	Worked on logic for login and registration. 
o	Emmanuel: Refactored code for clarity purposes.
o	Code was tested and worked well; PR was approved.

## October 16th, 2023
Time: 1pm – 5pm                      
SCRUM Master: Emmanuel                      
Note Taker: Aaron                       
Location: Classroom, Library 3016                      
Attendance: All                      
Pre-Meeting Questions/ Goals:                      
-	Session management.
-	Reorganizing all of our files.
-	Better understanding of how we want our review page to work.
Professor Recommendations:                      
-	Discuss progress on sprint 1 deliverables and code implementation status. 
-	If you’re still doing interface design, you may not meet all the deliverables for sprint 1.
Meeting Notes:                      
-	Fixing issues relating to session management for if a user is logged in and someone opens a new tab and logs into another account.
-	Notice issue relating to when a user types in the wrong password, error states the password entered was incorrect.
-	This issue will be fixed later by adding "Invalid login information" etc instead of stating password error.
-	Working on the review’s topic page.
-	Discussed topic searching for specific topics to bring up a thread of the total reviews.
-	Got clarification from Dr. Brown about how the review pages should work.
-	Discussed with Dr. Brown how our formatting and file organization should work.
-	Discussed with Dr. Brown team dynamics and marking schemes.
-	Decided to completely remodel our file system structure to match the five-developer schematic in Dr. Brown’s notes.
-	Completely revamped our GitHub commits to fully restart with five empty folders representing the five developer’s positions.
-	Re-commit files into correct file folders corresponding to specific developer’s topic.
-	Worked on specific README file for marking scheme and updated meeting notes.
-	Tasks: Everyone was tasked to individually rewrite their code based on their development flowchart assignment and commit to their branch.
Pull Request Performance Reviews from Oct 12th, 2023:                      
-	Aaron didn’t meet the deadline as was waiting for better clarification from the group.
-	Irfanul, Anika, and Faraz did not need to create PR for review purposes.
-	Emmanuel was able to meet the deadline for the PR.
-	Full group was on the same page throughout the meeting and no group conflicts occurred.
Pull Request Code Reviews from Oct 12th, 2023:                      
-	About Irfanul’s code:
o	No PR to review.
-	About Aaron’s code:
o	Worked on README file for marking template.
o	Waited for group discussion before continuing.
o	Wasn’t completed so no PR was created.
-	About Anika’s code:
o	No PR to review.
-	About Emmanuel’s code:
o	Worked on creating database table for topics.
o	Thought about ways to search the table for topics.
o	Irfanul suggested all caps no spaces search to reduce user error.
o	PR was approved.
-	About Faraz’s code:
o	No PR to review.

## October 17th, 2023
Time: 1pm – 5pm                      
SCRUM Master: Anika                      
Note Taker: Irfanul                        
Location: Classroom, Library 3016A, Library 4016A                        
Attendance: All                        
Pre-Meeting Questions/ Goals:                      
-	Updating Trello/ moving it to Github’s task manager thing.
-	Finish commits with files to new file management. 
-	Go over README file and meeting note updates.
-	Talk about writing tests – POSTMAN?

Professor Recommendations:                      
-	Detailing progress. 
-	The team should now start thinking about what elements of the first sprint will be completed, and what tasks, documents, and marking scheme elements will not be completed in time for the first sprint. 
-	Discuss how you will deal with this within your software process, making preliminary decision (for example, decisions about continuing some tasks into the next sprint) 
-	How this status will be conveyed to the markers, and on your board, and in your repo documents.

Meeting Notes:                      
-	Optimizing the new structure to import all related files.
-	Modularize the files further to increase decoupling.
-	Test that the website works properly.
-	Discussed unit tests.
-	Discussed README file contents and how we want to transfer over our meeting notes from the Word document to markdown file.
-	Looked into transferring Trello tasks to GitHub’s KanBan board.
-	Aaron: Work on README file to go over as a group next meeting.
-	Everyone: Work on transferring files to new dev structure
-	Discuss next meeting locations.

Pull Request Performance Reviews from Oct 16th, 2023:                      
-	Everyone met the designated deadline.

Pull Request Code Reviews from Oct 16th, 2023:                      
-	Everyone’s own restructured code was pushed to their own branch, and it was agreed upon in the meeting that since there are no extreme changes to the code, we call all create PRs and approve our own PRs at some point in the future before next meeting.

## October 19th, 2023
Time: 1pm – 4pm  
SCRUM Master: Emmanuel  
Note Taker: Aaron  
Location: Classroom, Library 3016A   
Attendance: All  
Pre-Meeting Questions/ Goals:
-	Clarification on the unit test.
-	Clarification on user stories.
-	Performance reviews after each meeting or one at the end of the sprint?

Professor Recommendations:
-	Final clean-up.
-	Code and performance reviews.
-	Documentation for end of sprint.

Meeting Notes:
-	Discussed how to run and create unit tests with Dr. Brown.
-	Discussed how we want to organize Performance Reviews relating to total time worked together in sprint #1.
-	Discussed with Dr. Brown how we should do our user stories and that each group member should create their own user story which includes two wanted backlog features.
-	Discussed and resynchronized everyone’s GitHub branches.
-	Emmanuel: Unit test
-	All: Performance reviews
-	All: User Stories
-	All: Make a readme file for their own dev folder
-	Aaron: Master ReadMe file

Pull Request Performance Reviews from Oct 17th, 2023:
-	Everyone approved their own pull requests for their transfer to the new developer file template as agreed in previous meeting.

## October 23rd, 2023
Time: 1pm – 2pm  
SCRUM Master: Emmanuel  
Note Taker: Aaron  
Location: Classroom  
Attendance: All  
Pre-Meeting Questions/ Goals:
-	NA

Professor Recommendations:
-	identify team tasks for 2nd sprint.
-	identify tasks still not completed from sprint 1.
-	identify features for 2nd sprint.
-	decompose features into coding tasks.
-	try to identify possible interface revisions required for coding tasks.

Meeting Notes:
-	Sprint 2 due November 10th.
-	Needs to be done from sprint 1:
o	Creating reviews under a topic
o	Filtering reviews by topic
o	User logs in
-	Should implement 2 backlog features.
-	Each group member should have at least 40 lines of code and delegated two coding tasks.
-	Each topic will have the four box checkboxes that people can rate in the boxes 1-10 rating.
-	Features we want to include this sprint:
o	Anonymity from review creation
	Blocked by creating a topic and review.
	Won’t be anonymous to the server.
o	Implementing tags
	Fixed tags
	Predetermined
	Optional tags
	Dropdown menu with 10 options
-	Need to assign: 
o	Anika - Session management: Provides that multiple users can be logged in and operating the app at the same time. The information from different sessions does not get mixed up by the application. 
o	Faraz and Emmanuel - Review entries can be found with partial match searches of users or topics.
o	Aaron and Irfanul - A team should have the option of creating and including a series of rating items as part of a review. This may require the creation of new data structures for the app logic. (maybe Faraz as well)
o	As an example, a team might want to use these rating items in a review: 
<div style="padding: 50px; margin: 10px 80px; border: solid;"> 
Rate the following on a scale from 1 to 10:  <br><br> <input type="number" min="1" max="10"> Effort expended on this topic.   <br> <input type="number" min="1" max="10"> Communication with team.   <br> <input type="number" min="1" max="10"> Participation in critical reviews.   <br> <input type="number" min="1" max="10"> Attending team meetings.   <br> </div> 
o	a feature for automating aggregation of rating reviews and/or quantitative analysis based on rating reviews should be added to your project backlog (i.e. it does not need to be implemented in this sprint).

## October 24th, 2023
Time: 1pm – 2pm  
SCRUM Master: Anika		  
Note Taker: Emmanuel  
Location: Classroom  
Attendance: All  
Pre-Meeting Questions/ Goals:
-	Delegate tasks
-	Provide structure for who has to code what.
-	Discuss how Thursday’s meeting will be run.

Professor Recommendations:
-	Assign design and coding tasks for 2nd sprint and set deadlines for activities.
-	Especially pull request deadline for final sprint submissions.

Meeting Notes:
-	Approved Emmanuel’s PR for cleaning up the import statements.
-	Understanding the full goals for sprint 2.
-	Emmanuel: Are there specific things we have to rate?
-	What issues we want to resolve and how we are going to break them into tasks for KanBan:
o	Session Management – Anika/ Emmanuel:
	Using Bottle – Beaker library
	Following the Beaker examples and using functions and methods to implement feature for multiple user use at the same time.
o	Write review page - Aaron/ Irfanul:
	Create the TPL file/ HTML.
	Create the route for the server.
	Map review data to database.
o	Create the rating part - Aaron/ Irfanul/ Faraz:
	Figure out the specifics of how we want to include our review process.
	Figure out where we want to have the review process on the website.
	Implement the actual HTML code.
	Database to store the actual ratings – eventually we will have to manipulate the rating data.
	Want a 5-star rating process.
o	Create the anonymous feature – Faraz/ Emmanuel:
	Create the app logic.
	Possible changes to the database.
	Feature on the actual website – HTML code.
o	Implementing tags – Faraz/ Emmanuel/ Irfanul/ Aaron/ Anika:
	Creation of routes for the tags?
	Create list of tags.
	Create drop down menu for tags.
	Sorting by tags?
	Putting filters all in one spot?
	Connecting tags to reviews?

Pull Request Performance Reviews:
-	Emmanuel refactored code to fix module/ package imports.
o	Anika: Code looks cleaner.

## October 27th, 2023
Time: 1pm – 2pm, 2:30pm – 4pm  
SCRUM Master: Faraz		
Note Taker: Irfanul  
Location: Classroom, Library 3016  
Attendance: All  
Pre-Meeting Questions/ Goals:
-	What feature should we start working on today.
-	What tasks should we assign to everyone today.

Professor Recommendations:
-	Outline the architecture document incorporating updated modules interfaces for current sprint. 
-	Will you have consistent UML diagrams for the architecture document?

Meeting Notes:
-	Discussed specific approach to feature issues.
-	Implementing reviews and rating system, how would it work.
-	Get the actual server running again.
-	Figure out write review page (Irfanul and Aaron)
-	Figure out session management (Anika, Emmanuel, and Faraz)
-	We all went for lunch.
-	Clarification – What are we searching for, reviews or topics?
-	Drew the full website on a whiteboard so we all are on the same page with how it will look, what pages we want, what on click will do.
-	Talked about how to implement the point based and text-based reviews:
o	Separate pages
o	Each page is connected to their counter part (Ie point to text and other way around)
o	Submit button.
o	Some way of dealing with drafts – will come to that later.
-	Tasks for next meeting:
o	Irfanul: HTML Page for:
	Create list of topics page.
	Create rating-based review page.
	Create text-based review page.
	Create create-review page.
o	Aaron: Creating new routes for new webpages:
	Route called /topic, /topic/topic_id (dynamic route), / topic/<create>, topic/<rating>, topic/<text>
o	Faraz: Work on logic.
o	Anika: Fix the KanBan board.
o	Emmanuel: Creating topic table, update review table, changing or line to or word.

Pull Request Performance Reviews:
-	Faraz’s PR approved. No comments.

## October 30th, 2023
Time: 1pm – 2pm, 2:00pm – 4pm  
SCRUM Master: Irfanul	  
Note Taker: Anika  
Location: Classroom, Library 3016  
Attendance: All  
Pre-Meeting Questions/ Goals:
-	Get clarification for searches – topics vs reviews.

Professor Recommendations:
-	Review architecture document contributions.
-	Changes to interfaces entailed by detailed architecture design.
-	Tasks needed for new interface considerations.

Meeting Notes:
-	Got clarifications told to search for topics instead of reviews.
-	Schematics for topic search solution, Emmanuel will implement database part, Faraz will implement logic aspect, and Aaron will implement the controller functions.
-	Session management: Anika gave us an update on Beaker.
-	Kanban board was updated.
-	Github rebase tutorial and error fixing from mistakes made by group members.
-	Going through server and running tests to ensure everything flows properly.
-	Discussed how to implement our rating system which resulted in the group changing the current checkboxes to textboxes where users can put numbers from 1-10.
-	Write a review button should be clearer and have it so people have an understanding that they have an option through hyperlink. Like we do for the login page.
-	Add to the KanBan backlog: User should also be able to alter the questions regarding a topic.
-	Same hyperlink in the text base review page returning back to rating review page.
-	Fixed three for number of questions in the rating review.
-	KanBan backlog: Allow the user to choose how many questions they want per topic.
-	Under write_topic page they have possibility to write three questions, one in each box. Character limit. Text error. Topic must be created with all fields filled out.
-	Tags will be moved to backlog.
-	Emmanuel: Create a tag table with common tags, could kill two birds with one stone, individual and group tags included in tag features.
-	Mouse curser can be seen flashing in the Post Topic button for some reason.
-	List of possibly topics: Cuisine and nutrition, politics and government, science and technology, Sports and recreation, transport and travel, miscellaneous, arts and culture, economy and business, environment and nature, social and relationships, spirituality and philosophy, education and learning.
-	Working demo is now working.
-	Irfanul: Make topics clickable in topic list, add text area to write questions in write topic, changing post review page to have rating scale.
-	Aaron: Change post topic page to topic list page when logging in.
-	Faraz: Create handle_post_review, and handle_post_topic, searching logic.
-	Anika: Session management beaker.
-	Emmanuel: Add logged in user function, searching logic.

Pull Request Performance Reviews:
-	Aaron’s code: Need to change routes so after login it goes to the topic review page and not the review list page. Fixed up post/ get methods for route calls.
-	Irfanul’s code: Want to add additional features; including text boxes for three questions in create review page.
-	Emmanuel’s code: Looks good.
-	Faraz’s code: Want to create topic class.

## November 6th, 2023
Time: 1pm – 2pm, 2:00pm – 3pm  
SCRUM Master: Aaron	 
Note Taker: Emmanuel  
Location: Classroom, Library 3016  
Attendance: All  
Pre-Meeting Questions/ Goals:  
-	Go over PRs from last week.
-	Go over rubric from group markings of Sprint #1 and compile documentation about discrepancies. 
-	Go over rubric for Sprint #2.
-	Talk about session management with Anika.
-	Decide whether search function will be handled by database or logic.
-	Figure out tasks for next meeting.

Professor Recommendations:  
-	Review feedback from sprint 1.
-	What changes are needed to process model and team activities?
-	Discuss content of the process and architecture documents for sprint 2.
-	Task out those documents.

Meeting Notes:
-	Discussed search function – decided to have it implemented by the database. 
-	Discussed Sprint #1 rubric marking: Seen below in Meeting Notes.
-	Code Review for PRs that happened during the previous week. PRs that were completed for today were commented on and approved.
-	Rubric for Sprint #2 was analyzed.
-	Updated KanBan board.
-	Clarification on KanBan issue documentation. How does he want it to look like?

0/2 - Establish labels, color coding, and categories for the Kanban board cards and issues. 
Comments: Did not use colors or labels.
Argument: This might be due to us switching from Trello to KanBan last minute. We also have them labelled based on each person’s task and each person has their own colour. Slash how do you colour code things to your specifications on KanBan if that is a requirement?

0/5 - Problems with the team progress, dynamics and process must be identified and documented, and tracked with possible responses and progress on those items becoming kanban/agenda items. 
Comments: Even things that were noted, e.g. tardiness, no cards, response or followup mechanism is created.
Argument: Note is unclear. We did add issues to the KanBan that were related to the project. Further clarification is needed for future sprint rubrics.

2/10 - Code reviews are thorough, covering style issues (SOLID, de-coupling) as well as correctness. 
Comments: I could not find the substance of the code reviews anywhere, aside from a very few comments in the meeting notes. Did I miss the documentation?
Argument: This was explained in our README file. Code reviews were performed during meetings as all the PRs were presented and commented as a group during our meetings, to then be approved by the group as a whole. Some comments were also made directly on Github.

0/5 - All code should be reviewed before pull request is merged. 
Comments: I cannot tell if the reviews are related to PRs. How did you decide to pull? Regression testing is expected as part of the reviews. Are unit tests used anywhere? They are only for one unit? 
Arguments: In the README file, this was explained. We don’t think we should lose marks for unit test here since we did do all PR and discussed at meetings, commented at meetings, and approved at meetings. What is regression testing?

0/2 - Pull request deadlines established and enforced. 
Comments: Seems like you changed this at the end of the sprint?
Arguments: We did this based on your feedback on our project structure. This was all explained in our README file. Each meeting we set specific goals/ tasks for everyone to complete for the next meeting.

2/5 - User stories are complete and good quality.
Comments: Some of These seem to be ideas you had anyway, and you wrote a story around them. Stories should reveal features that would not otherwise occur to you. Stories are too simplistic per notes. I was expecting more along the lines of Sommerville's scenarios, not simply stories that read: I want this feature, I want that feature.
Argument: How is this a valid claim? The book was not mentioned in the rubric/ outlined for user stories.

Pull Request Performance Reviews:
-	Emmanuel’s PR: Faraz accepted them. Comments: Goals: return logged in user and slight bug fixes for the log in page, both were present. 
-	Aaron’s PR: Was approved by Aaron by accident. Issues with Github which were fixed later. Routes were all made for the five new tpl files. Irfanul noticed that the main login page route needed to be changes. Aaron made a PR for that change which was approved by the group.
-	Irfanul’s PR: Was approved by Aaron. All five pages were made successfully. 
-	Faraz’s PR: Create topic question. Logic aspect was not completed due to hindrance cause by other PRs (waiting on db). Expected to finish before end of the sprint.

## November 7th, 2023  
Time: 1pm – 2pm, 2:00pm – 4pm  
SCRUM Master: Faraz	  
Note Taker: Aaron  
Location: Classroom, Library 3016  
Attendance: All  
Pre-Meeting Questions/ Goals:
-	Discuss tagging.
-	Session management.
-	Discuss search.
-	KanBan revamp.
-	Model Analysis.
-	Component Architecture.
-	Coding Tasks.
-	Two features we want to include: Anonymous and Tags
  
Professor Recommendations:  
-	Discuss how MVC pattern might help in the design of your architecture.
  
Meeting Notes:
-	Faraz mentions issue with Post Review page which is logic cannot figure out which topic the review is addressed to.
-	Solutions: Revamp website so it keeps topic inside URL or database or put a field where the user addresses which topic they are reviewing.
-	Aaron: Has to figure out what the URL will look like relating to topics, dynamic URLs.
-	URL information will be taken when creating the reviews.
-	Alternative user is also asked which topic they are reviewing with a search bar or a drop-down menu. 
-	If doesn’t exist, can have an error implementation.
-	Emmanuel will send links for dynamic URLs documentations.
-	Issue: Revamping the review creation implementation:
o	Update template files.
o	Routing updates for dynamic URLs: 
o	Logic needs to be written.
-	Successful when template contains enough information for logic to work properly. Routing needs to pass information to logic. Logic needs to work.
-	Discussion about session management implementation:
o	Researching Beaker.
o	Want to multiusers to be able to log in and manipulate reviews at the same time.
o	Bottle doesn’t support that feature.
o	Doesn’t look like we will be able to implement this feature for Sprint 2.
o	Will be looking at implementing this in Sprint 3.
o	Referred to Dr. Brown’s videos.
o	Referred to Beaker videos.
o	Other groups have implemented Beaker and once we talked about our issues, he was also having similar issues. Had meeting with professor who said he will investigate the issue.
o	Beaker just saves cookies into the browser, not something that should be implemented in the real world.
o	Multiple devices would work with our feature/ current database.
-	Discussion about searching feature:
o	Professor asked us to implement this feature.
o	Not enough time to figure out how to implement it properly.
o	Don’t think it will be finished for the end of Sprint 2.
o	Emmanuel, Irfanul, and Faraz worked together on the issue.
o	Needed more clarity on if were searching for topics or reviews. Got the answer that we should be searching by topic towards the end of the sprint. Which didn’t give us enough time to finish this feature. 
o	Will be attempting to implement it in Sprint 3.
-	Discussion about tagging feature:
o	One of the features our group decided to implement as part as our selected features.
o	Doesn’t look like this feature will be finished in time for this Sprint.
o	Will be looking to finish it for Sprint 3.
o	This feature is locked behind Write-review process that we are still working on finishing.
o	Which is an issue with linking reviews and topics.
-	Discussion about KanBan revamping:
o	Got clarification with the professor about what an ideal KanBan board looks like.
o	Want to add specific tags on each task so we can better organize how to delegate each task.
o	Looking at how big issues can be broken down into smaller tasks and tags properly.
o	Need to rewatch the KanBan video the professor posted to better understand how to organize KanBan properly.
-	Anonymous Button Feature:
o	Template has checkmark box locked behind create-review.
o	Database logic is ready.
o	Logic aspect is ready.
o	All that’s needed is the templating and routing reconfigured in such a way that passes topic as an argument to logic when creating a review. 
-	Model Analysis:
o	Referring to Note 16 in the professor’s recommended readings.
-	Component Architecture:
o	Reference to lecture video from Dr. Brown.
-	What needs to be done:
o	Irfanul: KanBan. Implementing tags and reorganizing the KanBan board. Watching the video. Unit test.
o	Faraz: Template coding, anonymous logic. Unit Test.
o	Aaron: README file, Email prof, dynamic routing URLs, meeting notes. Unit Test.
o	Emmanuel: Component Architecture – Lecture Video. Logic for searching. Unit Test.
o	Anika: Model Analysis – Note 16. Unit Test.
-	Deadline for all tasks will be our next meeting on Thursday.
  
Pull Request Performance Reviews:
-	Faraz’s code: Created a new model for topic questions. Was approved by the group. Comments included that it all looked good. In compliance with the database table. Wasn’t much code to review.
-	Aaron’s Meeting notes PR was approved.
-	Emmanuel’s code: Fixed a bug relating to user not being able to log in because of the @use_db decorator functions.

## November 9th, 2023
Time: 1pm – 2pm, 2 – 4pm  
SCRUM Master: Faraz		  
Note Taker: Anika  
Location: Classroom, Library 3016  
Attendance: All  
Pre-Meeting Questions/ Goals:
-	Discuss KanBan board progress.
-	Discuss logic progress.
-	Discuss Model Analysis progress.
-	Discuss Unit Test progress.
-	Discuss README file progress.
-	Discuss Component Architecture progress.
-	Discuss meeting times with Dr. Brown about Sprint 1.
-	Discussion about Session Management.
  
Professor Recommendations:
-	NA
  
Meeting Notes:
-	README file discussion:
o	Document how we are changing our KanBan board with labels and making everything an issue.
o	Outline of README file will change so that the rubric is present and each component on the rubric is outlined directly.
-	Discussion about Session Management:
o	Restriction on Bottle with multithreading from Dr. Brown.
o	Webpage might time out if a request is being dealt with while another one is queued up.
o	If we decide to use Bottle, we just must mention that this is a restriction with the client we are using, but it is totally fine if we use it for our project.
o	Browser thinks there may be a time out when it’s just a queueing process.
o	This feature will not be completed in time for Sprint 2. Will be looking to complete it in Sprint 3.
-	Model Analysis Discussion:
o	Project backlog.
o	Should we put all features we weren’t able to finish in the project backlog?
o	Later, we don’t need to update them.
o	Started to work on features but we only partly completed features and how will these be incorporated into the next sprint.
o	Sprint backlog, ones we selected from product backlog should move into the next column.
o	Anika has a lot of material, which is good.
o	Full documentations were gone over during the meeting and will be pushed from Anika as all parts were given to her.
-	Component Architecture:
o	According to the video there is a specific software we should be using – UMLet.
o	Emmanuel took the lead and did research on how this task should be completed and passed that information on to the group.
o	We should be referring to video 17 in the professor’s notes. 
o	Making a diagram through the software is time consuming.
o	A diagram of everyone’s developer’s parts just like we were given.
o	Each component would have their own methods and descriptions within the parts.
o	Based on interfaces. 
-	Discussion about KanBan board process:
o	Began adding labels.
o	Every task needs to become an issue before labels can be added.
o	Got clarification from Dr. Brown that all tasks can be issues.
o	In progress of making all the tasks issues with labels now.
o	Labels include: Bug, Product Backlog, sprint backlog, code, database, documentation, duplicate, enhancement, help wanted, interface, invalid, logic, question, restructure, routing, session management, want to fix.
o	The date will show November 8th and 9th since we have been fixing it, even though the tasks have been there since the beginning of the sprint.
-	Discussion about Logic:
o	Three things have been done.
o	Implementations of post topic, write review, and post review.
o	Post topic is now completed and functional however, is going to need session management to return user in order to completely make a database reference.
o	Creator ID for the topic has been created but we don’t know how to access that.
o	This issue has been added to the KanBan board and will be resolved by session management for Sprint 3.
o	Write review and post review are also functional on a logic level.
o	Locked behind session management and database implementations.
o	CreatorID = 1. Needs it to be a function called from session management.
-	Tasks for Sprint 2 deadline: Friday
o	Everyone: Watch video 17 and work on architecture.
o	Aaron: README file, Email prof, performance review, help with component architecture.
o	Emmanuel: Performance review, help with component architecture. Unit tests.
o	Faraz: Performance review, take lead on component architecture.
o	Anika: Performance review, process model analysis.
o	Irfanul: Performance review, KanBan board labels.

Pull Request Performance Reviews:
-	Aaron’s PR: 
o	Just added dynamic routing routes.
o	Issues with when topic name needs to be pulled from dynamic routes.
-	Faraz’s PR: 
o	Redundant comments that can be removed. Could be added to our KanBan board.
o	The organization of codes and imports could be improved.
-	Anika’s PR:
o	Three files that were changed.
o	In casing input field into a form. 
o	Want to be able to separate post review and write review.
o	Post review is point based, write review is text based.
o	Might want to change the naming convention as it over complicates things.
o	Will be adding it to the backlog.
-	Aaron’s PR:
o	Logic can create specific functions to pill the data from the dynamic route. Will add this to the KanBan board.

## November 17th, 2023
Time: 1pm – 2pm  
SCRUM Master: Anika	  
Note Taker: Emmanuel  
Location: Classroom  
Attendance: All  
Pre-Meeting Questions/ Goals:
-	Previous Sprint Defects.
-	Discussion of new Sprint goals.
Professor Recommendations:
-	Finalize assignment of tasks for the sprint to team members.
-	Make sure any known defects in process from previous sprints are dealt with (these should be noted in your process documented form previous sprint but may have thought of new things since them.)
Meeting Notes:
-	Sprint 3 due December 4th, 2023.
-	Discussion of new Sprint and what needs to be accomplished:
o	Modify process model analysis.
o	Modify component architecture.
o	Microservices architecture document.
	A comparison of a microservices approach to the project to the existing (components-based) approach.
	A discussion on how the architecture and code would be different under a microservices architecture.
	A discussion of how the software process would be different under a microservices architecture.
o	A project requirements specification effective with setup tools and/or another build tool.
	Need more clarification.
o	Three implemented features from user stories/ backlog/ team member suggestions.
o	40 lines of code per or two coding tasks per group member need to be done.
o	Documentation of meeting notes.
o	Updating and cleaning up KanBan board.
-	Discussion of previous Sprint goals not completed:
o	Session management for multiusers.
o	Tags.
o	Search by topic.
o	Posting a new review.
o	Posting a topic.
o	Writing the topic questions.
o	Point based reviews.
o	Linking the anonymous checkbox.
o	Allow user to pick number of questions.
o	Unit tests?
o	Update the 
-	Next meeting will delegate tasks and start working on the Sprint 3.
-	Possibly meet with Dr. Brown on Monday to discuss Sprint 1 rubric.
Pull Request Code Reviews:
-	NA

## November 20th, 2023
Time: 1pm – 2pm  
SCRUM Master: Emmanuel  
Note Taker: Irfanul  
Location: Classroom, Library 3016  
Attendance: All  
Pre-Meeting Questions/ Goals:  
-	Ask Dr. Brown to meet Tuesday after class to discuss Sprint 1 rubric.
-	Discussion about which three features we want to add this Sprint.
-	Assignment of tasks to be worked on this Sprint.
  
Professor Recommendations:
-	Start discussion of changes to process and architecture documents for sprint 3. 
-	Start discussion of alternative architecture document.
  
Meeting Notes:
-	Discussion with Dr. Brown:
o	Meeting with him Tuesday after class to discuss Sprint 1 rubric.
-	Discussion about three features we want to add this sprint:
o	Adding a feature to allow the user to change the number of questions they can write.
o	Timed logout feature.
o	Add time stamp to reviews.
o	Colour coding topics. Saving the colour code in the database.
-	Team decided to be harsher this Sprint.
-	Will be assigning features to specific people so we can start holding group members accountable. Issue is some features can’t be implemented until other functions have been completed.
-	Want to get the overall review and topic posting functions working.
-	Will be assigning tasks next meeting.
-	Possibility of having the Sprint 3 deadline extended since the professor was sick for a week.
-	Anika mentioned she can work on updating our attribution table and the process model documents.
- Irfanul added tasks to the KanBan board.
  
Pull Request Code Reviews:
-	NA

## November 21st, 2023
Time: 1pm – 3pm  
SCRUM Master: Irfanul  	
Note Taker: Faraz  
Location: Classroom  
Attendance: All  
Pre-Meeting Questions/ Goals:
-	Discussion with Dr. Brown about Sprint 1 rubric.
-	Assignment of tasks to get the initial website functioning.
  
Professor Recommendations:
-	Nothing to contribute.
-	Continue with SCRUM.
  
Meeting Notes:
-	Class extension of a week for Sprint 3 because of professor’s illness.
-	Discussion with Dr. Brown about Sprint 1 rubric:
o	Email Dr. Brown everything we discussed in class and where he can find the support for our arguments.
-	Assignment of tasks:
o	Aaron: Email Dr. Brown the point of discussion for Sprint 1’s rubric. 
o	Anika: Session management.
o	Emmanuel: Create the database function for getting all the reviews from the topic_id.
o	Faraz: Create a function that calls DB function.
o	Irfanul: Update the HTLM page to render all the topics.

Pull Request Code Reviews:
-	Aaron: Updated dynamic routing for review_list.

## November 23rd, 2023
Time: 1pm – 2pm  
SCRUM Master: Faraz  
Note Taker: Aaron  
Location: Classroom  
Attendance: All  
Pre-Meeting Questions/ Goals: 
-	Merge outstanding PRs.
-	Understand the alternative Microservices Architecture Document.
-	Get clarification on Component Architecture Document.
-	Assignment of new tasks.
  
Professor Recommendations: 
-	Watch the recommended video on the course page to understand how to create the Microservice Architecture.
  
Meeting Notes: 
-	Clarification on Component Architecture document:
•	Dr. Brown wasn’t available for clarification, was talking with other groups.
-	Assignment of tasks:
•	Aaron: Follow up with Dr. Brown and README file.
•	Anika: Continue working on session management; begin work on the process model.
•	Faraz: Update the Component Architecture Document accordingly and the logic if needed.
•	Irfanul: Understand the Microservices Architecture Document and update the Kanban board.
•	Emmanuel: Watch the Sommerville video to understand how to create the Microservices Architecture Document.

Pull Request Code Reviews: 
-	Emmanuel's PR: Added DB functions to allow users to create topics and reviews that belong to a topic, as well as get topics and reviews that belong to a topic.

## November 28th, 2023
Time: 1pm – 2pm  
SCRUM Master: Aaron  
Note Taker: Anika  
Location: Classroom  
Attendance: All  
Pre-Meeting Questions/ Goals:
-	Discuss next items to get the project off the ground.
-	Go over any PRs if there are any.
-	Follow up on last meetings assignment of tasks and if they were completed.
-	Get clarification on component architecture document.
-	Assignment of tasks.
  
Professor Recommendations:
-	After the team has looked at chapter 9, discuss what details on testing or code review might be added to your process document / suggested process model.
-	Task someone to make sure external package installs are correctly represented in the repository.
  
Meeting Notes:
-	Discussion of project goals:
o	December 10th deadline.
o	Trying to get post topic and post review working.
o	Want to click on topic to get the review list of the topics:
	Database part of this functionality is complete. Template is complete. Logic still needs to be updated. Irfanul can work on template to render topics. Emmanuel can populate the database with falsified data to test functionality. 
o	Render topic:
	Logic will pass data to Irfanul to render HTML template.
	Gets the list from named arguments.
	Aaron calls logic from app.py and then Aaron passes data to Irfanul’s template.
	Logic.handle_fetch_topic_list()
	Any logic functions can be found under logic.
o	Create topic/ create review:
	Database part is complete.
	Faraz has questions about calling create_review, is Emmanuel internally checking to see if its text based?
	Emmanuel is in the database. Review by default is point based.
	Is text based but has an optional point based, what create_review does.
	Faraz will just pass Emmanuel reviews. 
	Going to just have text-based reviews currently.
	Faraz doesn’t want to change it as it looks good already.
	Faraz: Wants Aaron to pass him arguments in Review.py
-	Discussion on last meetings tasks:
o	Asked Dr. Brown about follow up for Sprint 1 email that was sent last week, he will look into it.
o	Aaron: Still in process of working on README file.
o	Faraz: Get clarifications on UML.
o	Emmanuel: Did watch the video. Can do it based on the way he structured it.
-	Discussion of component architecture:
o	In progress.
-	Assignment of tasks:
o	Aaron: README file. Fetching information required to make a review from the templates and pass it to logic.
o	Faraz: Take Aaron’s arguments and call Anika session management to create sessionID, package review and pass it to database to create a new review.
o	Emmanuel: Microservices. Update KanBan board.
o	Anika: Session management and model analysis documents. 
o	Irfanul: Microservice clarification. Update KanBan board.

Pull Request Code Reviews:
-	NA

## November 30th, 2023  
Time: 1pm – 2pm, 2 – 3pm  
SCRUM Master: Anika	  
Note Taker: Emmanuel  
Location: Classroom, Library 3016  
Attendance: All  
Pre-Meeting Questions/ Goals:
-	Connect interface review methods to database review methods.
-	Get clarification for UML in python.
-	Session management update.
-	Go over PRs.
  
Professor Recommendations:
-	Creating a requirements.txt list and instructions on using it for the README are tasks for this sprint cycle.
  
Meeting Notes:
-	Session management:
o	We think it got it to work. Not working on both tabs.
o	Anika is having a difficult time researching and implementing Bottle for multiuser session management.
o	Decided in terms of deadlines that she should abandon that task and focus her time on the process model analysis documentations.
-	Microservices architecture document:
o	Finished comparison to previous architecture.
o	Finished impact team software process.
o	Emmanuel is working on the third: identifying the microservices. How we want to rearchitect our project.
-	Emmanuel added dummy data for topics for the database.
-	Aaron is working on the README file based on the location of everything we are allocated marks for.
-	Aaron and Faraz are still working on connecting review methods to the database reviews methods.
-	Get UML clarification:
o	UML design was reviewed by Dr. Brown.
o	Noticed several problems such as:
	Most of our code was not in shape of objects but simply code written in the file. This is difficult to show in a UML diagram. Solution is to find specific things attributed to the package and list them in the diagram (ex. List all routes for app.py, list all interfaces for interfaces).
	App logic diagram looked too crowded. Solution is to break it into several diagrams.
	A lot of redundancy - don’t repeat yourself problem, which impedes expansion to the project. Solution, not necessary to rewrite code, it should definitely be discussed by all members in a meeting and should be put into our backlog.
-	Update KanBan board.
  
Pull Request Code Reviews:
-	Emmanuel’s PR:
o	Inserted dummy data into database. No comments. Approved by Anika.
-	Faraz’s PR:
o	Pass arguments from app.py to database. No comments. Approved by Aaron.

## December 5th, 2023
Time: 1pm – 2pm, 2 – 3pm  
SCRUM Master: Emmanuel	  
Note Taker: Faraz  
Location: Classroom, EN Computer Lab  
Attendance: All  
Pre-Meeting Questions/ Goals:
-	Microservices architecture document.
-	Component architecture updates.

Professor Recommendations:
-	NA

Meeting Notes:
-	Microservices diagram document discussion:
o	Agree on what is a microservice. Microservice is a very small thing that you can do in a subdomain in our application.
o	In subdomains they have specific tasks to accomplish.
o	Each is modeled as a microservice.
o	Will get extra marks if we comment opinions on microservice documents.
	Is too granular, too specific.
	Small scale project like ours, we don’t get any advantages.
	Should make microservices small?
o	Identified microservices, authentication broker, topic broker, review broker. All methods in db user file.
o	How you communicate between two services is through brokers.
o	Possible with UMLab.
-	Component architecture discussion:
o	Showed Dr. Brown documentation.
o	Mentioned there is a lot of redundancy.
o	Solution: Create a readme doc that said we understand these design flaws and that we are going to restructure and put that in the backlog in KanBan.
o	Address circular redundancies, “don’t repeat yourself” problem.
o	To address this issue, we have chosen to alter the position of certain files.
	User inside of logic which will be merge logic into session management. 
	Merge all db objects (ex db user, db topic, db review) into a general database module which contains all the methods for interacting with the database and URL code.
	Tasks into backlog but doesn’t need to be implemented.
	Will explain this all in a readme.
o	App logic being too crowded will be divided into multiple diagrams to solve the crowded issue.
-	Updated dynamic routing to pass topic_id from URL as an argument.

Pull Request Code Reviews:
-	NA
