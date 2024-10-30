# GitHub Users and Repositories Data
<h6>
  
- I utilized the GitHub API to scrape data on users located in Toronto with over 100 followers, gathering both their profile information and public repositories.
  
- One surprising finding was that some users had a substantial number of repositories while having fewer than 1,000 followers, highlighting that follower count does not always correlate with repository activity.

- To enhance community engagement, I recommend developers in Toronto connect with users who have numerous repositories, as they may offer valuable insights and collaboration opportunities.
</h6>

# Data Files
`users.csv`: <h6>Contains information about GitHub users, including their profiles and work history.</h6>

`repositories.csv`: <h6>Lists the public repositories of the users, detailing their activity and contributions.</h6>

# How I scraped the data:
<h6>Below are the links of the python code used to scrape the data:</h6>

- <a href='https://github.com/22f3001377/Pro1/blob/main/users_csv_scrape.py'>user_csv_scrape.py</a>
- <a href='https://github.com/22f3001377/Pro1/blob/main/repo_csv_scrape.py'>repo_csv_scrape.py</a>

# The most interesting and surprising fact you found after analyzing the the data
<h6>One surprising finding was that some users had a substantial number of repositories while having fewer than 1,000 followers, highlighting that follower count does not always correlate with repository activity.</h6>

![image](https://github.com/user-attachments/assets/585e6cb4-ab6d-4008-b945-05c727ff74e5)

<h6>The above image is the screenshot of the user.csv after being sorted from highest to lowest in terms of no. of repositories. Comparing that with the no. of followers beside it we can see that the no. of followers a user has doesn't depend on the number of repos they create.</h6>

![image](https://github.com/user-attachments/assets/9c41e252-c9e2-4463-b94e-6bb4dd5781f0)

<h6>Infact, after 2020 we can see that the number of repos even though less,some users have more followers. User <i><a href='https://github.com/laion01?tab=overview&from=2024-10-01&to=2024-10-31'>laion01</a></i> has made many contribution to the github community. Below are his graphs in 2024 and 2023 with 2023 being the year he contributed the most.</h6>

![image](https://github.com/user-attachments/assets/3b322d3d-6178-4180-9c08-47cf4e7eb237)


![image](https://github.com/user-attachments/assets/4729cd1e-1649-4533-b7cb-7862be5dca99)



<h6>Inspecting his profile more, I found out the user has collaborated and coauthored several merge pull requests.</h6>



![image](https://github.com/user-attachments/assets/da20dc8f-c9c4-4bd1-88b3-1530145aa3e7)

  
<h6>However,even though user <i><a href='https://github.com/jsoref?tab=overview&from=2024-10-01&to=2024-10-31'>jsoref</a></i> contributed a lot more(graph above), his contributions weren't as much significant to other people which he himself admits in his profile. This user is working on a project called spelling checker (a github action). Therefore, we can deduce that there is no particular relationship between no. of repos or contribution to them and no. of followers in github. </h6>

<h6>There are other facts that can be considered here for e.g. the no. of people each of these users are following and when have they created their accounts and such.</h6>

# What is one actionable recommendation for developers based on my analysis.

<i><h5>Encourage Collaboration and Community Engagement</h5></i>

<h6>Developers are encouraged to engage with the GitHub community, alongside creating repositories. Building connections through collaboration, participating in discussions, and contributing to existing projects can enhance visibility and foster a supportive network. By focusing on community interactions, developers may find new opportunities for growth and collaboration, regardless of their repository count.</h6>


## How to Use This Data

This dataset can serve multiple purposes, such as identifying potential collaborators for software projects or understanding the trends in technology use among developers in Toronto. Users can leverage this information to network, share insights, and discover innovative projects.
