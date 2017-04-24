#!/usr/bin/python
# -*- coding: utf-8 -*-

import webbrowser#web browser function call it attributes /function such as open etc


class Movie:#class is created

    VALID_RATINGS = ['G', 'PG', 'PG-13', 'R'] # some ratings are provided to review the movies

    def __init__(
        self,
        movie_title,
        movie_year,
        poster_image,
        trailer_youtube,
        ):#self function init is defined contain movie title,year of release,image,youtube link

        self.title = movie_title
        self.year = movie_year
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        #assigning values

    def show_trailer(self): # a function named show trailer is called in order to show the trailers of movie
        webbrowser.open(self.trailer_youtube_url)



			
