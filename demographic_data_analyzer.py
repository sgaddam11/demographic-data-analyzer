import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()

    # What is the average age of men?
    male_df = df[df['sex']=='Male']
    average_age_men = male_df['age'].mean().round(1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = df.shape[0]
    bachelors_count = df[df['education'] == 'Bachelors'].shape[0]
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)
  

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education_df = df[(df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate')]
    higher_education = (higher_education_df.shape[0] / total_people ) * 100
    lower_education_df = df[~((df['education']=='Bachelors') | (df['education']=='Masters') | (df['education']=='Doctorate'))]
    lower_education = (lower_education_df.shape[0] / total_people ) * 100
  
    # percentage with salary >50K
    higher_education_rich_df = higher_education_df[higher_education_df['salary'] == '>50K']
    higher_education_rich = round(((higher_education_rich_df.shape[0]/higher_education_df.shape[0]) * 100),1)
    lower_education_rich_df = lower_education_df[lower_education_df['salary'] == '>50K']
    lower_education_rich = round(((lower_education_rich_df.shape[0]/lower_education_df.shape[0]) * 100),1)
    

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers_df = df[df['hours-per-week'] == min_work_hours]
    num_min_workers = num_min_workers_df.shape[0]
    rich_num_min_workers_df =num_min_workers_df[num_min_workers_df['salary'] == '>50K']

    rich_percentage = (rich_num_min_workers_df.shape[0]/num_min_workers) * 100

    # What country has the highest percentage of people that earn >50K?
    df['salary_bool'] = df['salary'].apply(lambda x: 1 if x == '>50K' else 0)
    result_df = df.groupby('native-country')['salary_bool'].mean() * 100

    highest_earning_country = result_df.idxmax()
    highest_earning_country_percentage = result_df.max().round(1)

    # Identify the most popular occupation for those who earn >50K in India.
    country_df = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = country_df['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
