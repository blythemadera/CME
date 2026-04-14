# Update on tasks
We cleaned the datasets using OpenRefine. We focused on the columns of zip codes, affordable housing units, names of parks, and names of libraries. We looked at each of these columns and resolved inconsistencies like missing values. We used Python to combine the highlighted columns into one dataset. We group data by counts to begin looking at the overall datasets to analyze and explore these results. After this, the Status Report will be submitted.

Our next steps all revolve around the Final Project Submission. We will analyze the new dataset more with the necessary columns. We will create different visualizations to analyze the data better.

# Updated Timeline
- March 22 - March 28:
  - Begin writing Interim Status Report (**DONE**)
  - Work on datasets (**DONE**)
    - cleaning: removing unnecessary columns that do not add to our research
    - grouping: make sure each zip code corresponds to one neighborhood in the housing dataset, and aggregate the data based on the zip code for all data sets, which will be done by count to avoid confusing string combinations
    - combining: merge datasets on zip code and assign parks and libraries to the corresponding communities
- March 29 - April 4:
  - Finalize the status report and edit the file with the feedback received (**DONE**)
  - Continue working on datasets (cleaning, grouping, combining) (**DONE**)
- March 31 - Interim report Due (**Due Date Changed to April 14**)
- April 5 - April 11:
  - Finalize the combination of all three datasets (clean and analyze result) (**DONE**)
- April 12 - April 18:
  - Begin working on the Final Project Submission (**IN PROGRESS**)
  - Continue editing datasets to observe different factors of it (**IN PROGRESS**)
- April 19 - April 25:
  - Continue working on the Final Project Submission
  - Create visualizations for datasets
  - Finalize dataset analysis and research
- April 26 - May 2:
  - Finalize the Final Project Submission
- May 3: Final Project Due


# Changes
Changes to our Project Plan based on our feedback focused on making more specific tasks for each other. Blythe and Alyssa will work on cleaning the datasets individually and then meet to discuss any changes made. Alyssa will download the files after cleaning to merge them. We will meet to discuss our thoughts for the status report, and we will both add our ideas to the status report. We will both explore different forms of visualizations for the data. We will meet to discuss our analysis and write our findings separately for the final project submission. We will individually write our parts in the file after our meeting.

We were able to use OpenRefine for a lot of the cleaning of the important columns in the datasets. We prepared the datasets until they were ready for use, and then we downloaded them and worked with Python for the next tasks. 

We are no longer grouping by neighborhoods; several neighborhoods are assigned to the same zip code, and we would not be able definitively assign parks and libraries to the correct neighborhoods with the data at hand. Instead, we have decided to move in a different direction and group by zip code and gather a count of how many parks and libraries are in the area and looking at the amount of affordable housing units. 

# Challenges
We were going to use OpenRefine to merge the columns for one dataset, and we wanted to merge based on zip code, but when adding the parks and library columns to the affordable housing file, places with multiple amenities in one zip code only chose to add one of those amenities (parks or libraries). This then caused us to go back to our original plan of using Python to merge the columns. From there, we will continue working on the new file. 

Other issues we faced were that we encountered missing data for some of the parks and affordable housing units. These places didn’t have a zip code. To resolve this, we looked up the address of that location and manually added that zip code to the file. 

We were planning to assign each library and park to a neighborhood/community, however there are multiple communities within a zip code area, so now we are shifting to grouping by zip code and we must reassess our plans and how they are affected. We are also interested in creating a map visualization that created a zone mapping of the zip code areas and shows the density of parks, libraries, and affordable housing in each area. With that comes the challenge of figuring out how to code for the map visualization, as we have not created a visual of that type before.  

# Team-Member Contribution
Alyssa: I worked on cleaning the housing and library datasets, I uploaded and worked on the library json file and the housing csv file in OpenRefine. The biggest item that needed addressing was in the library data. There was a cell that was missing the number of units, which was found and inputted. The affordable housing data, management groups were merged, and the syntactic errors were addressed. I brought the cleaned datasets from OpenRefine to VScode to aggregate the data and make it into a single dataset. Firstly, I created data frames from the data sets and grouped them by zip codes, which created counts in the other columns of parks/libraries in those zip codes, or for the housing dataset I grouped by zip codes and used the unit column to aggregate the amount of affordable housing units in each area. I then joined the parks and library data onto the housing data, getting rid of zip codes that were not in the affordable housing dataset, leaving us with a data frame that is made of rows of individual zip codes, the amount of affordable housing units, parks, and libraries in those zones. I then pushed the cleaned datasets as well and the notebook with all the mentioned data frames, into the GitHub repository.  

Blythe: I reviewed each file in OpenRefine and examined the columns to identify any inconsistencies or missing data. I explored different features in OpenRefine to analyze the data further. I helped address missing data and shared my findings to ensure we were both working with the same data. I began exploring the datasets in Python. Finally, I helped write half of the answers to the Status Report, participated in our meetings, and shared my findings.

