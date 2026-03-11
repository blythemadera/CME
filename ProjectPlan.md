# Overview
The goal of our project is to understand the relationship between areas where affordable housing is most prevalent and the accessibility of parks and libraries within the same community/zip code in Chicago. Our approach to achieving our goal is to examine the presence of parks and libraries and compare their locations (zip codes) with those of affordable housing, and to assess whether there is a positive or negative correlation between the inputs. We aim to assess whether people and families living in affordable housing have access to public services, such as parks and libraries, that support child development and a sense of community. The main steps we will take to execute the project are to take the data from the City of Chicago Data Portal, format it into dataframes in Python, clean the data, and merge on the zip codes. An important part of our process will be assigning the parks and library data to community areas in Chicago to see area-specific counts. Due to the varying row counts between the library, park, and housing datasets, a major step is going to be to figure out the best way to aggregate the data and make sure the zip code and community areas match up between dataframes. Affordable housing is indicative of the struggle with high and rising rent prices in the city of Chicago, and the presence of parks and libraries may have a relationship with the income level or affordability of an area.

# Team
Alyssa and Blythe are both responsible for an equal amount of work on each step of the project. Blythe will be in charge of submitting assignments on Canvas and creating the necessary files on GitHub. Alyssa will keep us on track with our timeline, adding additional tasks when necessary and making sure we are working on the correct things each week.
We will meet weekly to discuss additional steps of the project. We will ask each other questions when we don't understand certain parts of the code or a step in our project. We will conduct additional outside research on our own and ask for help from the TAs and the professor when needed. We will set additional deadlines before the class due dates to ensure we have enough time to peer review our work.


# Research Questions
What is the relationship between affordable housing and the number of libraries and parks in different areas of Chicago? 

# Datasets
- Affordable housing by community data: https://data.cityofchicago.org/Community-Economic-Development/Affordable-Housing-Units-by-Community-Area/yvj4-y3fb
  - Downloaded from the Chicago Data Portal
  - A map is provided on the website with color-coded sections separating different community areas of Chicago
  - 598 rows describing different communities of Chicago
  - Descriptions include community name and number, property type and name, address, zip code, management company, units, coordinates, and location
  - Last updated on December 17, 2025

- Library Data:
https://data.cityofchicago.org/Education/Libraries-Locations-Hours-and-Contact-Information-/wa2i-tm5d
  - 81 rows showing information from different libraries
  - Library information includes branch name, service hours, address, city, state, zip code, phone number, website, email, and location coordinates
  - Downloaded from the Chicago Data Portal
  - Last updated on February 20, 2025

  
- Park data:
https://data.cityofchicago.org/Parks-Recreation/Parks-Map-deprecated-November-2016-/2eaw-bdhe
  - Downloaded from the Chicago Data Portal
  - 581 Rows showing information for parks in Chicago
  - Information includes park number, name, and class, street address, zip code, acres, ward, label, location, and specific amenities offered
  - A map is provided on the data portal with dots displaying each park
  - Last updated February 20, 2025


# Timeline

- March 22 - March 28:
  - Begin writing Interim Status Report
  - Work on datasets
    - cleaning: removing unnecessary columns that do not add to our research
    - grouping: make sure each zip code corresponds to one neighborhood in the housing dataset, and aggregate the data based on the zip code for all data sets, will do  by count to avoid confusing string combinations
    - combining: merge datasets on zip code and assigne parks and libraries to the corresponding communities
- March 29 - April 4:
  - Finalize the status report and edit the file with the feedback received
  - Continue working on datasets (cleaning, grouping, combining)
- March 32 - Interim report Due
- April 5 - April 11:
  - Finalize the combination of all three datasets (clean and analyze result)
- April 12 - April 18:
  - Begin working on the Final Project Submission
  - Continue editing datasets to observe different factors of it
- April 19 - April 25:
  - Continue working on the Final Project Submission
  - Create visualizations for datasets
  - Finalize dataset analysis and research
- April 26 - May 2:
  - Finalize the Final Project Submission
- May 3: Final Project Due


# Constraints
The datasets have been accessed and downloaded from the City of Chicago data portal, so there is no issue with licensing, as the data is provided by a government body. Limitations and challenges that come from our datasets are that there is some vagueness around the timeframe for the data provided for the park mapping/locations. Limitations that come from the Affordable Housing dataset are completeness and some difficulty with cleaning and processing the data. The challenge that we face with the cleaning and processing is that we have to ensure that each zip code corresponds to one community area, so that when we combine the datasets were can properly organize the libraries and parks into their respective communities. The limitation that we face with the completeness of the dataset comes from the data that is included only in completed housing developments, which potentially excludes many developments that are in progress or planned for development.


# Gaps
We have not yet learned many data cleaning methods that will be helpful when cleaning our data. Initial dataset analysis reveals some rows with missing or unnecessary information that we will need to remove or change. Additionally, we have not fully learned and practiced data integration. This feature will be very important because we have three datasets to combine. Lastly, we haven't learned about workflow automation and provenance, which will be helpful throughout our whole project. Aside from class topics that we haven't learned yet, we will also need to do further research on our datasets to fill in gaps from information not provided. We could analyze additional affordable housing being built in areas of Chicago not mentioned, we can analyze property value trends based on community factors, and further use other datasets that might provide more insight into the locations with more or less affordable housing. Finally, our datasets haven't been updated since last year, and changes in the information could affect our final analisis to our research question.

