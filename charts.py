import plotly.graph_objects as go
from plotly.subplots import make_subplots


def create_pie_charts(df, title_color="#4ECDC4"):

    df_animals = df.groupby('fav_animals').size().reset_index(name='counts')
    df_place = df.groupby('fav_place').size().reset_index(name='counts')
    
    hobby_columns = ['hobby_art', 'hobby_books', 'hobby_movies', 'hobby_other', 'hobby_sport', 'hobby_video_games']
    hobby_translation = {
    'hobby_art': 'sztuka',
    'hobby_books': 'książki', 
    'hobby_movies': 'filmy',
    'hobby_other': 'inne',
    'hobby_sport': 'sport',
    'hobby_video_games': 'gry wideo'
    }
    df_hobby = (df[hobby_columns]
            .rename(columns=hobby_translation)
            .sum()
            .reset_index(name='counts')
            .rename(columns={'index': 'hobby'})
            .sort_values('counts', ascending=False))
    
    learning_columns = [
    'learning_pref_books',
    'learning_pref_chatgpt',
    'learning_pref_offline_courses',
    'learning_pref_online_courses',
    'learning_pref_personal_projects',
    'learning_pref_teaching',
    'learning_pref_teamwork',
    'learning_pref_workshops'
    ]
    learning_translation = {
    'learning_pref_books': 'książki',
    'learning_pref_chatgpt': 'ChatGPT',
    'learning_pref_offline_courses': 'kursy offline',
    'learning_pref_online_courses': 'kursy online',
    'learning_pref_personal_projects': 'projekty osobiste',
    'learning_pref_teaching': 'nauczanie',
    'learning_pref_teamwork': 'praca zespołowa',
    'learning_pref_workshops': 'warsztaty'
    }
    df_learning = (df[learning_columns]
               .rename(columns=learning_translation)
               .sum()
               .reset_index(name='counts')
               .rename(columns={'index': 'learning_method'})
               .sort_values('counts', ascending=False))

    # Definition of color palettes for each chart
    color_palettes = {
        'hobby': ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FECA57', '#FF9FF3'],
        'learning': ['#6C5CE7', '#A29BFE', '#74B9FF', '#00B894', '#00CEC9', '#FDCB6E', '#E17055', '#FD79A8'],
        'animals': ['#FF7675', '#74B9FF', '#55A3FF', '#00B894', '#FDCB6E', '#FD79A8', '#E84393'],
        'places': ['#00CEC9', '#6C5CE7', '#FDCB6E', '#E17055', '#00B894', '#FF7675', '#74B9FF']
    }

    # Create a subplot with 2x2 layout for pie charts
    fig = make_subplots(
        rows=2, cols=2, 
        specs=[[{'type':'domain'}, {'type':'domain'}], 
            [{'type':'domain'}, {'type':'domain'}]],
        subplot_titles=['', '', '', '']  # Emty titles for subplots
    )

    # Adding charts with individual color palettes and separate legends
    fig.add_trace(
        go.Pie(
            labels=df_hobby['hobby'], 
            values=df_hobby['counts'], 
            hole=.5,  # The hole for the pie chart
            name='Hobby',
            marker_colors=color_palettes['hobby'][:len(df_hobby)],
            textinfo='label+percent',
            textposition='outside',
            legendgroup='hobby',
            legendgrouptitle_text='Hobby',
            showlegend=True
        ), 
        row=1, col=1
    )

    fig.add_trace(
        go.Pie(
            labels=df_learning['learning_method'], 
            values=df_learning['counts'], 
            hole=.5,
            name='Metody nauki',
            marker_colors=color_palettes['learning'][:len(df_learning)],
            textinfo='label+percent',
            textposition='outside',
            legendgroup='learning',
            legendgrouptitle_text='Metody nauki',
            showlegend=True
        ), 
        row=1, col=2
    )

    fig.add_trace(
        go.Pie(
            labels=df_animals['fav_animals'], 
            values=df_animals['counts'], 
            hole=.5,
            name='Ulubione zwierzęta',
            marker_colors=color_palettes['animals'][:len(df_animals)],
            textinfo='label+percent',
            textposition='outside',
            legendgroup='animals',
            legendgrouptitle_text='Ulubione zwierzęta',
            showlegend=True
        ), 
        row=2, col=1
    )

    fig.add_trace(
        go.Pie(
            labels=df_place['fav_place'], 
            values=df_place['counts'], 
            hole=.5,
            name='Ulubione miejsca',
            marker_colors=color_palettes['places'][:len(df_place)],
            textinfo='label+percent',
            textposition='outside',
            legendgroup='places',
            legendgrouptitle_text='Ulubione miejsca',
            showlegend=True
        ), 
        row=2, col=2
    )

    # Upddating layout from titles in the center of each pie chart
    fig.update_layout(
        title_text='Wykresy kołowe', 
        title_x=0.5,
        title_font_size=20,
        # Titles in the center of each pie chart
        annotations=[
            dict(text='<b>Hobby</b>', x=0.225, y=0.815, font_size=16, showarrow=False, 
                xanchor="center", yanchor="middle", font_color=title_color),
            dict(text='<b>Metody<br>nauki</b>', x=0.775, y=0.815, font_size=16, showarrow=False, 
                xanchor="center", yanchor="middle", font_color=title_color),
            dict(text='<b>Ulubione<br>zwierzęta</b>', x=0.225, y=0.19, font_size=16, showarrow=False, 
                xanchor="center", yanchor="middle", font_color=title_color),
            dict(text='<b>Ulubione<br>miejsca</b>', x=0.775, y=0.19, font_size=16, showarrow=False, 
                xanchor="center", yanchor="middle", font_color=title_color)
        ],
        # Setting the legend properties
        legend=dict(
            orientation="v",
            yanchor="top",
            y=1,
            xanchor="left",
            x=1.05,
            font_size=10,
            groupclick="toggleitem"
        ),
        # Margins and size adjustments
        margin=dict(t=80, b=50, l=50, r=200),  # Increased right margin for legend
        height=700,  # Increased height for better visibility
        width=1200   # Increased width for better visibility
    )

    return fig