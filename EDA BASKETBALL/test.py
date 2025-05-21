import streamlit as st
import pandas as pd
import base64
st.write('Hello World!')
select_year = st.selectbox('Year', list(reversed(range(1970, 2026))))
def load_data(year):
    url = 'https://www.basketball-reference.com/leagues/NBA_' + str(year) + '_per_game.html'
    html = pd.read_html(url)
    df = html[0]
    df = df.set_index('Rk')
    df = df.drop(columns = 'Age')
    df = df.fillna("0")
    return df
player_stats = load_data(select_year)
sorted_unique_team = sorted(player_stats.Team.unique())

selected_team = st.sidebar.multiselect('Team', sorted_unique_team,sorted_unique_team)
unique_pos = ['C','PF','SF','PG','SG']
selected_pos = st.sidebar.multiselect('Position', unique_pos, unique_pos)
df_selected_team = player_stats[player_stats.Team.isin(selected_team) & player_stats.Pos.isin(selected_pos)]

st.header('Display Player Stats of Selected Team(s)')
st.write('Data Dimension: ' + str(df_selected_team.shape[0]) + ' rows and ' + str(df_selected_team.shape[1]) + ' columns.')
st.dataframe(df_selected_team)
st.write(df_selected_team.shape)


def filedownload(df):
    csv = df.to_csv(index = False)
    b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    href = f'<a href="data:file/csv;base64,{b64}" download="playerstats.csv">Download CSV File</a>'
    return href

st.markdown(filedownload(df_selected_team), unsafe_allow_html=True)