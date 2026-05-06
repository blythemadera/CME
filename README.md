# Accessibility of Public Amenities near Affordable Housing Areas
By: Alyssa Lopez and Blythe Madera

# Summary
The purpose of our project is to understand the relationship between areas where affordable housing units are more prominent and the presence of parks and libraries within the same zip code in Chicago. Our project details an interpretation of the relationship between affordable housing with public amenities, including parks and libraries, in the Chicagoland area. We wanted to see the relationship between the number of affordable housing units in each area, and the availability of a library and/or park in the same area. The relationship would address our overarching interest in the availability of public services to those who utilized affordable housing in the Chicago area. The relationship would also help us learn about the accessibility of public services that support child development and community, in areas that tend to have those in need of income-adjusted rent. Affordable housing is indicative of the struggle with high and rising rent prices in the city of Chicago, and the presence of parks and libraries may have a relationship with the income level or affordability of an area. We had an interest in pursuing this topic of research because we understand the importance of public services in the development of children, and for low-income families. Our research question was: What is the relationship between affordable housing and the number of libraries and parks in different areas of Chicago? To attempt to answer this question, we found data provided by the Chicago Data Portal about Affordable Housing, Parks, and Libraries. We took that data, cleaned it in OpenRefine, downloaded and formatted the cleaned data in Python, and then aggregated each dataset into counts based on the zip code. We separated different areas by using all three locations’ zip codes to be able to see which zip codes from affordable housing had the most access to parks and libraries in their areas. The housing data became a count of all units in each zip code, and the park and library data were a count of all parks or libraries in a zip code area that were then merged on the zip codes. The parks and library data sets were merged onto the housing data set to keep all of the zip codes that had affordable housing units and only look at parks and libraries that were within those zip codes.  

From our research and analysis of the data provided by the Chicago Data Portal, we found that there was a moderate positive relationship between the number of affordable housing units in an area and the presence of parks within that same zip code. We also found that there was a positive, but weak, relationship between the amount of affordable housing units and the presence of libraries within the same zip code area. The correlations we were able to find suggested to us that we are more likely to see more parks located inside zip code zones that have more affordable housing units, but with a more moderate correlation, the relationship is notable but strong. With that, the presence of libraries within those same areas does not have a meaningful increase with the increase of affordable housing units. Our research suggests that the presence of parks and libraries in a particular area is impacted by other factors more strongly than the presence of affordable housing units.


# Data profile

Affordable housing by community data: https://data.cityofchicago.org/Community-Economic-Development/Affordable-Housing-Units-by-Community-Area/yvj4-y3fb  

The data set was downloaded as a JSON file from the Chicago Data Portal, it was uploaded to OpenRefine to be cleaned, and then uploaded to the GitHub repository on the main branch. On the webpage for the data, a map is provided with color-coded sections separating different community areas of Chicago. The dataset has 598 rows describing different communities of Chicago, and 14 columns providing descriptions including community name and number, property type and name, address, zip code, management company, units, coordinates, and location. According to the Data Portal the last update was on December 17, 2025. For the Affordable Housing by Community data there are no legal constraints associated with the dataset as it is open use as provided by the Chicago Data Portal, and with proper attribution to the Chicago Data Portal. With the data there is no information that could be used to identify any one individual, the data consists of information solely about the location and qualities of a property that has affordable housing units. Ethical constraints associated with the data mainly come from any results or conclusions drawn from the data. Incorrect interpretations or biased analysis may stigmatize groups and harm individuals who rely on subsidized rent and affordable housing units. This specific dataset was chosen to help answer our research question as it contains the most relevant data on affordable housing units in the Chicago area, provides the zip code for the units and provides the number of units in a residential building that are affordable housing.  

 

Library Data: https://data.cityofchicago.org/Education/Libraries-Locations-Hours-and-Contact-Information-/wa2i-tm5d\ The dataset was downloaded as a csv file from the Chicago Data Portal. The Json link was copied and uploaded into Open Refine to create a new project available for analysis. There were 81 rows showing information from different libraries in the Chicagoland area. Library information included in the dataset includes columns such as branch name, service hours, address, city, state, zip code, phone number, website, email, and location coordinates. This dataset was last updated on February 20, 2025. On the Data Portal Website, an interactive map is provided displaying the different locations. This dataset has no legal constraints attached. It comes from the Chicago Data Portal, a public dataset website available for downloading by anyone. There are no ethical constraints associated with this data. It simply provides a list of library locations in Chicago with basic information regarding their location and its operability. Misinterpretations occurring from this website would be the result of the analyzer and not the information provided. This dataset was chosen because we wanted to highlight the importance of library amenities for all residents of Chicago. Accessibility to these locations can help boost education scores for residents. This dataset provides and inclusive list of all libraries and includes a zip code column, important for the focus of our analysis. 

 

Park data: https://data.cityofchicago.org/Parks-Recreation/Parks-Map-deprecated-November-2016-/2eaw-bdhe This dataset was downloaded as a csv file from the Chicago Data Portal. We copied the link into a new project on Open Refine to be able to clean and observe the data before downloading it and begin the coding section of our project. There are 581 rows showing information about parks in Chicago. Information includes park number, name, and class, street address, zip code, acres, ward, label, location, and specific amenities offered. A map is provided on the data portal with dots displaying each park. This dataset was last updated on February 20, 2025. Our datasets are within the main branch of our CME repository. The datasets have been accessed and downloaded from the City of Chicago data portal, so there is no issue with licensing, as the data is provided by a government body. Misinterpretations from this dataset would not be due to the data provided, but because of the analyzer. Missing or inaccurate values should be observed before using this dataset. There are no ethical constraints associated with this data as it relates to public numerical information about parks in Chicago, their locations and amenities accessible to the public. This dataset was chosen because parks are crucial for recreational activities for residents of Chicago. We also wanted to highlight the importance of accessibility to parks for all, especially people living in affordable housing units. This dataset provides a comprehensive list of all parks and a zip code column which we used in our analysis of all three datasets.


# Data quality
Affordable Housing Dataset 

Regarding accuracy, the data in the zip code column was syntactically correct but not fully semantically correct. There was an instance in one of the rows, where a zip code was not a Chicagoland area zip code. After further inspection we concluded that the entry was syntactically accurate but not semantically correct. The zip code was for an area in Kansas. Although it was a valid zip code, it was not a Chicago zip code, which is what the dataset focused on. Regrading completeness, this dataset was almost fully complete, but it was missing one value in the units column. This was related to our project because we focused on the number of units available for affordable housing locations. We resolved this by looking up the building and the number of units. Regarding consistency, all data provided is consistent with the expected values. The values were formatted appropriately, and no errors stood out. Regarding timeliness, the last time this dataset was updated was on December 17, 2025. Not many changes have to be made if there’s no new affordable housing buildings. However, the housing data set is vulnerable to timeliness because the dataset consists of complete affordable housing units, and we could be missing units that are in the process of being built, or units that have been completed since 2025. 

 

Parks Dataset 

Regarding accuracy, from our cleaning and analysis, we concluded that all the data was syntactically and semantically accurate. No errors stood out and all of the values were valid for Chicagoland zip codes. Regarding completeness, there were missing values in the columns of street addresses and zip code for one of the rows. When we looked up this park, the address varied because of the length of the park. The park extended across a long path that resulted in multiple addresses. But the zip code remained constant throughout all the addresses, allowing us to manually input this into the dataset. This then left us with a completed dataset for the columns we were interested in. Regarding consistency, all data provided is consistent with the expected values. There are no formatting errors that we noticed. Regarding timeliness, this dataset was last updated on February 20, 2025. Not many changes have to be made if there’s no new parks. 

 

Library Dataset 

Regarding accuracy, from our cleaning and analysis, we concluded that all of the data was syntactically and semantically accurate. There were no errors that we could find with inaccurate or misleading data values. Regarding completeness, the data was complete in all columns. We did not find any missing values. Regarding consistency, all data provided is consistent with the expected values. There were no values that stood out in unusual formatting. Regarding timeliness, this data was last updated on February 20, 2025. Not many changes have to be made if there are no new libraries. This dataset had the highest quality out of the three we used, there were no mistakes in the columns we observed for our project.

# Data cleaning


# Findings
There is a correlation of 0.42787949462635716 between housing and parks, and a correlation of 0.07630969672584442 between housing and libraries. The relationship between the amount of affordable housing units and libraries within the same zip code is positive, but the co-movement is relatively moderate. The relationship between the number of affordable housing units and libraries is positive, but is very small and relatively weak, showing almost no relationship. What we have concluded is that it is more likely that we have parks and not libraries for every unit of affordable housing built in a zip code area. 


# Future work
This project has taught us several lessons about the datasets we’ve picked. We have learned to continuously check our data to ensure we have cleaned and prepped it properly for further analysis. We have learned to take the project step by step without skipping ahead so that we can stay on track with what we want to achieve and the types of results we want to produce. Furthermore, we have learned how to adapt quickly when errors do arise or when challenges become present. This project has made us look at our data in different ways and through different platforms, changing things as necessary while remaining consistent with our research question. We have seen aspects of our project that we would change if we were to reproduce it. Our project could be conducted with different focuses on other public amenities and other locations than Chicago. These changes could help expand our research to our questions regarding affordable housing accessibility to other community resources. 

In the future, fully checking the datasets you use is crucial to having an accurate analysis of the data. Cleaning the dataset was one of the most important parts of our project, which resulted in several issues being raised and resolved. Sometimes datasets can be incomplete or inaccurate, and by catching these errors at the beginning, before further analysis, a lot of time can be saved. Ensuring the datasets we use are accurate and reliable is also crucial to the answers you produce to your research question. If you use unreliable data, your whole project could be misleading and incomplete. Checking our work several times has helped us eliminate inaccuracies that could mislead our conclusions. Thus, we have found that a data quality assessment is helpful to evaluate the data we use. Additionally, understanding which columns from your dataset are necessary and important to your research question should happen before you clean your dataset, because then your focus when cleaning the dataset will surround those columns.  

We learned that while we could conclude based on the statistics drawn from the data and personal knowledge, however, a more comprehensive and supported answer would need more data and information outside of counts of units and locations. If we were to redo this project in the future, there are several changes we could make to further conclusions. Future work could investigate the average income of areas that have more public services, education levels of areas with more units, and/or what those units are built for, for example family units versus senior living. Using different datasets or adding more datasets to these would add more information that could explain the number of public amenities. This could also bring other crucial public amenities that are not represented in areas with more affordable housing. Analyzing smaller areas in Chicago, like neighborhoods or counties, and expanding further research to areas outside of Chicago can bring more information on the accessibility of public amenities. Expanding the research area could bring issues regarding accuracy and accessibility for this data. 

Overall, this project has taught us a lot on how to handle multiple datasets for analysis. It has also enhanced situations where we have to change our planned path. Finally, it has given us ideas of further research we would be interested in to expand our analysis.


# Challenges
A couple of the main challenges encountered revolved around missing or inaccurate data in the datasets. Some values were out of the Chicago zip code areas, causing discrepancies with our other datasets that only focused on the Chicagoland area. Additionally, there were some missing values in the Zip Code column. To resolve this, we searched the address provided for that row and manually input the zip code we found online. Lastly, a challenge we encountered with the data occurred when we began to analyze visualizations, and one of the zip codes appeared to be an outlier. We searched for that zip code and learned that it wasn’t a Chicago zip code. This semantic error caused us to question and recheck our data to ensure that we were only analyzing Chicagoland zip codes.  

 

Other challenges we encountered included being unable to combine columns using Open Refine because some zip codes had more than one park or library, causing the data to become distorted and confusing. To answer our research question we wanted to look at the counts of parks and libraries in zip code areas that had affordable housing. In OpenRefine we were unable to aggregate the data into counts, so we resolved this by grouping the data in Python, making it easier to analyze thereafter. This was something we had originally planned on doing before using Open Refine, making our solution to this issue easy to come to.  

 

When it came to the visualizations and concluding statistics from our analysis we had originally planned to make a density map visualization to show the prevalence of affordable housing units, parks, and libraries within the zip code areas in Chicago. We were able to develop other more basic visualizations, like a heatmap, to show the results of our analysis, but creating a visualization on a real map of Chicago brought more challenges. We decided to not continue with creating a density map, similar to the maps shown on the City of Chicago Data Portal, as we felt our technical skills were not up to par with the skills and knowledge needed to create such visualizations.  

 

Finally, another challenge we encountered was having to switch our analysis from Chicago neighborhoods to Chicago zip codes because our datasets did not have those columns. The Affordable Housing dataset had a “Community Area” column, and the Parks dataset had a “Ward” column, but the one that was in common for all three of our datasets was “Zip Code.” At the start of our project we were planning to merge the datasets with the count values on the common “Zip Code” column, and use that to separate the park and library counts into the appropriate neighborhoods, but we found that the zip codes and neighborhoods were not one-to-one making it difficult to properly categorize the parks and library counts into the correct area. We then made the decision to focus on zip codes only as that was the common descriptor between data sets that we would be able to merge them on. Overall, this didn’t really affect much of our analysis because we were still separating Chicago into different sections, only the way we separated changed. 

# Reproducing
1. We downloaded our datasets from the Chicago Data Portal.  

- https://data.cityofchicago.org/Community-Economic-Development/Affordable-Housing-Units-by-Community-Area/yvj4-y3fb 

- https://data.cityofchicago.org/Education/Libraries-Locations-Hours-and-Contact-Information-/wa2i-tm5d 

- https://data.cityofchicago.org/Parks-Recreation/Parks-Map-deprecated-November-2016-/2eaw-bdhe 

2. We uploaded each dataset to Open Refine and began to analyze the columns and data provided 

- Affordable Housing Dataset: We focused on the “_-zip_code” and “_-units” columns. We changed the column names to make the analysis universal between the other datasets. We observed outliers and missing information. We edited values for missing and inaccurate rows including row 28 and row 289. Row 28, we added "83" to the units column. For row 289, we changed the zip code to "60607." The history of our work is provided here: https://github.com/blythemadera/CME/blob/4d77c20dbafd4614ee476f507818daff70b51f7a/History-Affordable-Housing.json 

- Libraries Dataset: We analyzed the “ZIP” and “BRANCH” columns. We didn’t have to edit any of the rows. We didn’t need to change any of the column names because we used “ZIP” for all datasets. The history of our work is provided here: https://github.com/blythemadera/CME/blob/4d77c20dbafd4614ee476f507818daff70b51f7a/History-Libraries 

- Parks Dataset: We analyzed the columns “ZIP” and “PARK NAME.” We didn’t have to change any of the column names. We edited row 129 to "60643" in the zip column because it had a missing value. We used the name of the park to find the location online and thus; we were able to complete the data. The history of our work is provided here: https://github.com/blythemadera/CME/blob/4d77c20dbafd4614ee476f507818daff70b51f7a/History-Parks-Locations 

3. We downloaded the files and using Python opened each file in a pdf (https://github.com/blythemadera/CME/blob/1e65e8ffee773261a2cd8434e9b61ab649aa9cbd/Project.ipynb). 

4. We observed the dataset downloaded from each file for each of the three datasets.  

5. We grouped each zip code by their count for each of the three datasets. 

6. We aggregated each column name (units, branch, and park name, respectively) to their corresponding zip code creating a count of each per every separate zip code. 

7. We merged all three datasets into one. Having the counts of each amenity to each zip code. 

8. We created visualizations for the datasets and observed the data. 

9. We uploaded the Snake-make file and script in the repository (https://github.com/blythemadera/CME/blob/1e65e8ffee773261a2cd8434e9b61ab649aa9cbd/Snakefile). 

# References

“Affordable Housing Units by Community Area: City of Chicago: Data Portal.” Chicago Data Portal, data.cityofchicago.org/Community-Economic-Development/Affordable-Housing-Units-by-Community-Area/yvj4-y3fb. Accessed 1 May 2026.  

“Libraries - Locations, Hours and Contact Information - Map: City of Chicago: Data Portal.” Chicago Data Portal, data.cityofchicago.org/Education/Libraries-Locations-Hours-and-Contact-Information-/wa2i-tm5d. Accessed 1 May 2026.  


“Parks - Map (Deprecated November 2016): City of Chicago: Data Portal.” Chicago Data Portal, data.cityofchicago.org/Parks-Recreation/Parks-Map-deprecated-November-2016-/2eaw-bdhe. Accessed 1 May 2026. 
