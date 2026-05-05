# Accessibility of Public Amenities near Affordable Housing Areas
By: Alyssa Lopez and Blythe Madera

# Summary: [500-600 words] Description of your project, motivation, research question(s), and any findings.

The purpose of our project is to understand the relationship between areas where affordable housing units are more prominent and the presence of parks and libraries within the same zip code in Chicago. We wanted to see the relationship between the amount of affordable housing units in a given area, and the availability of a library and/or park in the same area. The relationship would address our overarching interest in the availability of public services to those who utilized affordable housing in the Chicago area. The relationship would also help us learn about the accessibility of public services that support child development and community, in areas that tend to have those in need of income adjusted rent. Affordable housing is indicative of the struggle with high and rising rent prices in the city of Chicago, and the presence of parks and libraries may have a relationship with the income level or affordability of an area. We had an interest in pursuing this topic of research because we understand the importance of public services in the development of children, and for low-income families. Our research question was: What is the relationship between affordable housing and the number of libraries and parks in different areas of Chicago? To attempt ot answer this question we found data provided by the City of Chicago Data Portal about Affordable Housing, Parks, and Libraries. We took that data, cleaned it in OpenRefine, downloaded and formatted the cleaned data in Python, and then aggregated each dataset into counts based on the zip code. The housing data became a count of all units in a given zip code, and the park and library data were a count of all parks or libraries in a zip code area, that were then merged on the zip codes. The parks and library data sets were merged onto the housing data set to keep all of the zip codes that had affordable housing units, and only look at parks and libraries that were within those zip codes. Findings: 


# Data profile: [max 2000 words] For each dataset used, describe its structure, content, and characteristics. Specify the location of the dataset files in your project repository. Discuss any ethical or legal constraints associated with the data and explain how the datasets relate to your questions

Affordable housing by community data: 
https://data.cityofchicago.org/Community-Economic-Development/Affordable-Housing-Units-by-Community-Area/yvj4-y3fb 
  - Downloaded as a csv from the Chicago Data Portal
  - A map is provided on the website with color-coded sections separating different community areas of Chicago
  - 598 rows describing different communities of Chicago
  - Descriptions include community name and number, property type and name, address, zip code, management company, units, coordinates, and location
  - Last updated on December 17, 2025
Library Data:
https://data.cityofchicago.org/Education/Libraries-Locations-Hours-and-Contact-Information-/wa2i-tm5d 
  - 81 rows showing information from different libraries
  - Library information includes branch name, service hours, address, city, state, zip code, phone number, website, email, and location coordinates
  - Downloaded as a json file from the Chicago Data Portal (json__ link taken from the Data Portal and uploaded into OpenRefine)
  - Last updated on February 20, 2025
Park data:
https://data.cityofchicago.org/Parks-Recreation/Parks-Map-deprecated-November-2016-/2eaw-bdhe 
  - Downloaded as a csv from the Chicago Data Portal
  - 581 Rows showing information for parks in Chicago
  - Information includes park number, name, and class, street address, zip code, acres, ward, label, location, and specific amenities offered
  - A map is provided on the data portal with dots displaying each park
  - Last updated February 20, 2025
Our datasets are within the main branch of our CME repository.
The datasets have been accessed and downloaded from the City of Chicago data portal, so there is no issue with licensing, as the data is provided by a government body.


# Data quality: [500-1000 words] Summary of the quality assessment.
Affordable Housing Dataset 

Accuracy: Most of the data in the zip code column was syntactically correct. There was an instance in one of the rows, where a zip code was not a Chicagoland area zip code. After further research is it syntactically accurate but not semantically correct? 

Completeness: This dataset was complete in the columns necessary, there were missing units' numbers. We concluded that this was unrelated to our project. For the scope of our analysis, the dataset is complete. 

Consistency: All data provided is consistent with the expected values. 

Timeliness: Last updated was December 17, 2025. Not many changes have to be made if there’s no new affordable housing. However the housing data set is vulnerable to timeliness because the dataset consists of complete affordable housing units, and we could be missing units that are in the process of being built, or units that have been completed since 2025. 


 

Parks Dataset 

Accuracy: From our cleaning and analysis, we concluded that all of the data was syntactically and semantically accurate. 

Completeness: There were missing values in the columns for street address and zip code for one row. 

Consistency: All data provided is consistent with the expected values. 

Timeliness: Last updated was February 20, 2025. Not many changes have to be made if there’s no new parks. 

 

Library Dataset 

Accuracy: From our cleaning and analysis, we concluded that all of the data was syntactically and semantically accurate. 

Completeness: The data was complete in all columns. We did not find any missing values. 

Consistency: All data provided is consistent with the expected values. 

Timeliness: Last updated on February 20, 2025. Not many changes have to be made if there are no new libraries. 

# Data cleaning: [max 1000 words] Summarize the data cleaning operations you performed and explain how each operation addressed specific data quality issues in your datasets.


# Findings: [~500 words] Description of any findings including numeric results and/or visualizations.

There is a correlation of 0.42787949462635716 between housing and parks, and a correlation of 0.07630969672584442 between housing and libraries. The relationship between the amount of affordable housing units and libraries within the same zip code is positive, but the co-movement is relatively moderate. The relationship between the number of affordable housing units and libraries is positive, but is very small and relatively weak, showing almost no relationship. What we have concluded is that it is more likely that we have parks and not libraries for every unit of affordable housing built in a zip code area. 


# Future work: [~500-1000 words] Brief discussion of any lessons learned and potential future work.
In the future, fully checking the datasets you use is crucial to having an accurate analysis of the data. Cleaning the dataset was one of the most important parts of our project, which resulted in several issues being raised and resolved. Sometimes datasets can be incomplete or inaccurate, and by catching these errors at the beginning, before further analysis, a lot of time can be saved. Additionally, understanding which columns from your dataset are necessary and important to your research question should happen before you clean your dataset, because then your main focus when cleaning the dataset will surround those columns. 
We learned that while we could come to a conclusion based on the statistics drawn from the data and personal knowledge, however, a more comprehensive and supported answer would need more data and information outside of counts of units and locations. Future work could look into the average income of areas that have more public services, education levels of areas with more units, and/or what those units are built for, for example family units versus senior living. 


# Challenges: [~500 words] Discuss the main challenges you encountered while working on the project.
A couple of the main challenges encountered revolved around missing or inaccurate data in the datasets. Some values were out of the Chicago zip code areas, causing discrepancies with our other datasets that only focused on the Chicagoland area. Additionally, there were some missing values in the Zip Code column. To resolve this, we searched the address provided for that row and manually input the zip code we found online. Lastly, a challenge we encountered with the data occurred when we began to analyze visualizations, and one of the zip codes appeared to be an outlier. We searched for that zip code and learned that it wasn’t a Chicago zip code. This semantic error caused us to question and recheck our data to ensure that we were only analyzing Chicagoland zip codes. 

Other challenges we encountered included being unable to combine columns using Open Refine because some zip codes had more than one park or library, causing the data to become distorted and confusing. We resolved this by grouping the data in Python, making it easier to analyze thereafter. This was something we had originally planned on doing before using Open Refine, making our solution to this issue easy to come to. 

Finally, another challenge we encountered was having to switch our analysis from Chicago neighborhoods to Chicago zip codes because our datasets did not have those columns. The Affordable Housing dataset had a “Community Area” column, and the Parks dataset had a “Ward” column, but the one that was in common for all three of our datasets was “Zip Code.” Overall, this didn’t really affect much of our analysis because we were still separating Chicago into different sections, only the way we separated changed. 

# Reproducing: Sequence of steps required for someone else to reproduce your results.


# References: Formatted citations for any papers, datasets, or software used in your project.

“Affordable Housing Units by Community Area: City of Chicago: Data Portal.” Chicago Data Portal, data.cityofchicago.org/Community-Economic-Development/Affordable-Housing-Units-by-Community-Area/yvj4-y3fb. Accessed 1 May 2026.  

“Libraries - Locations, Hours and Contact Information - Map: City of Chicago: Data Portal.” Chicago Data Portal, data.cityofchicago.org/Education/Libraries-Locations-Hours-and-Contact-Information-/wa2i-tm5d. Accessed 1 May 2026.  

Open Refine 

“Parks - Map (Deprecated November 2016): City of Chicago: Data Portal.” Chicago Data Portal, data.cityofchicago.org/Parks-Recreation/Parks-Map-deprecated-November-2016-/2eaw-bdhe. Accessed 1 May 2026. 
