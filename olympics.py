import streamlit as st
import pandas as pd
import noc , helper
import plotly.express as px 
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.figure_factory as ff 
df = pd.read_csv('athlete_events.csv')


region_df = pd.read_csv('noc_regions.csv')
df = noc.preprocess(df,region_df)
st.sidebar.title("Olympics Analysis")
st.sidebar.image('data:image/jpeg;base64,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')
user_menu = st.sidebar.radio(
    'Select an Option' ,
    ('Medal Tally' , 'Overall Analysis' , 'Country_wise Analysis' ,'Athlete wise Analysis')
)

if user_menu == 'Medal Tally':
    # st.header('Medal Tally')
    years,country = helper.country_year_list(df)
    selected_year =st.sidebar.selectbox("Select Year" , years)
    selected_country =st.sidebar.selectbox("Select Country" , country)
    
    medal_tally = helper.fetch_medal_tally(df, selected_year, selected_country)
    if selected_year == 'Overall' and selected_country == 'Overall' :
        st.title('Overall Tally')
    if selected_year != 'Overall' and selected_country == 'Overall' :
        st.title('Medal Tally in ' + str(selected_year))
    if selected_year == 'Overall' and selected_country != 'Overall' :
        st.title(selected_country + ' Overall Performance')
    if selected_year != 'Overall' and selected_country != 'Overall' :
        st.title(selected_country + ' Performance in ' + str(selected_year) + ' Olympics')

    st.dataframe(medal_tally)

if user_menu == 'Overall Analysis' :
    edition = df['Year'].unique().shape[0]-1 
    cities = df['City'].unique().shape[0]
    sports = df['Sport'].unique().shape[0]
    events = df['Event'].unique().shape[0]
    athlete = df['Name'].unique().shape[0] 
    nations = df['region'].unique().shape[0]
    st.title("Top Statistics")
    col1,col2,col3 = st.columns(3)
    with col1 :
        st.header("Edition")
        st.title(edition)
    with col2 :
        st.header("Hosts")
        st.title(cities)
    with col3 :
        st.header("Sports")
        st.title(sports)
    col4,col5,col6 = st.columns(3)
    with col4 :
        st.header("Events")
        st.title(events)
    with col5 :
        st.header("Nations")
        st.title(nations)
    with col6 :
        st.header("Athletes")
        st.title(athlete)
 
    nations_over_time = helper.data_over_time(df,'region')
    fig = px.line(nations_over_time , x='Edition',y='region')
    st.title("Participating Nations Over the Years")
    st.plotly_chart(fig)

    events_over_time = helper.data_over_time(df,'Event')
    fig  = px.line(events_over_time , x='Edition',y='Event')
    st.title("Events Over the Years")
    st.plotly_chart(fig)

    athlete_over_time = helper.data_over_time(df,'Name')
    fig = px.line(athlete_over_time , x='Edition',y='Name')
    st.title("Events Over the Years")
    st.plotly_chart(fig)

    st.title("No of Events Over time(Every Sports)")
    fig,ax = plt.subplots(figsize=(20,20))
    a = df.drop_duplicates(['Year','Sport','Event'])
    ax = sns.heatmap(a.pivot_table(index='Sport',columns='Year',values='Event',aggfunc='count').fillna(0).astype('int'),annot=True)
    st.pyplot(fig)

    st.title("Most successful Athletes")
    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')
    selected_sport = st.selectbox('Select a Sport',sport_list)
    x = helper.most_successful(df,selected_sport)
    st.table(x)

if user_menu == 'Country_wise Analysis' :
    st.title('Country-Wise Analysis')
    country_list = df['region'].dropna().unique().tolist()
    country_list.sort()
    selected_country = st.sidebar.selectbox("Select a Country",country_list)
    country_df = helper.yearwise_medal_telly(df,selected_country)
    fig = px.line(country_df, x='Year',y='Medal')
    st.title(selected_country + " Medal Tally Over the Years")
    st.plotly_chart(fig)

    pt = helper.country_event_heatmap(df,selected_country)
    fig,ax = plt.subplots(figsize=(20,20))

    ax = sns.heatmap(pt,annot=True)
    st.title(selected_country + " Excels in the following sports ")
    st.pyplot(fig)
    
    st.title("Top 10 Athletes of " + selected_country)
    top_ten_df = helper.most_successful_countrywise(df,selected_country)
    st.table(top_ten_df)


if user_menu == 'Athlete wise Analysis' :
    athlete_df = df.drop_duplicates(subset=['Name','region'])
    x1 = athlete_df['Age'].dropna()
    x2 = athlete_df[athlete_df['Medal']=='Gold']['Age'].dropna()
    x3 = athlete_df[athlete_df['Medal']=='Silver']['Age'].dropna()
    x4 = athlete_df[athlete_df['Medal']=='Bronze']['Age'].dropna()
    fig =ff.create_distplot([x1,x2,x3,x4],['Overall Age' , 'Gold Medalist' , 'Silver Medalist','Bronze Medalist'],show_hist=False,show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.title("Distribution of Age")
    st.plotly_chart(fig)

    x = []
    name = []
    famous_sports = [
    'Basketball',
    'Judo',
    'Football',
    'Speed Skating',
    'Athletics',
    'Ice Hockey',
    'Swimming',
    'Badminton',
    'Sailing',
    'Gymnastics',
    'Alpine Skiing',
    'Handball',
    'Weightlifting',
    'Wrestling',
    'Water Polo',
    'Hockey',
    'Rowing',
    'Fencing',
    'Equestrianism',
    'Shooting',
    'Boxing',
    'Taekwondo',
    'Cycling',
    'Diving',
    'Canoeing',
    'Tennis',
    'Modern Pentathlon',
    'Figure Skating',
    'Golf',
    'Archery',
    'Volleyball',
    'Table Tennis',
    'Baseball',
    'Rhythmic Gymnastics',
    'Freestyle Skiing',
    'Rugby Sevens',
    'Beach Volleyball',
    'Triathlon',
    'Ski Jumping',
    'Curling',
    'Snowboarding',
    'Short Track Speed Skating'] 


    for sport in famous_sports:
        temp_df = athlete_df[athlete_df['Sport'] == sport]
        age_data = temp_df[temp_df['Medal'] == 'Gold']['Age'].dropna()
        if not age_data.empty:
           x.append(age_data)
           name.append(sport)

    fig =ff.create_distplot(x,name,show_hist=False,show_rug=False)
    fig.update_layout(autosize=False,width=1000,height=600)
    st.title("Distribution of Age with respect to Sports")
    st.plotly_chart(fig)

    sport_list = df['Sport'].unique().tolist()
    sport_list.sort()
    sport_list.insert(0,'Overall')
    st.title('Height Vs Weight')
    selected_sport = st.selectbox('Select a Sport ',sport_list)
    temp_df = helper.weight_v_height(df,selected_sport)
    fig , ax = plt.subplots()
    ax = sns.scatterplot(x = temp_df['Weight'],y = temp_df['Height'],hue=temp_df['Medal'],style=temp_df['Sex'],s=100)
    st.pyplot(fig)

   
    final = helper.men_vs_women(df)
    st.title("Men Vs Women Participation over the year")
    fig = px.line(final , x = 'Year' , y = ['Male' , 'Female'])
    st.plotly_chart(fig)
