import media #it import all media file function automatically

import fresh_tomatoes #it import file from fresh tomatoes file and accessing function and variables in it

bajrangi_bhaijaan = media.Movie("Bajrangi Bhaijaan", 
			"2015",
			"https://upload.wikimedia.org/wikipedia/en/d/dd/Bajrangi_Bhaijaan_Poster.jpg", 
			"https://www.youtube.com/watch?v=vyX4toD395U")# it contains Movie name,its YEAR OF release,its image link,its trailer video link

pk = media.Movie("PK", 
			"2014", 
			"https://upload.wikimedia.org/wikipedia/en/c/c3/PK_poster.jpg", 
			"https://www.youtube.com/watch?v=gwcb4ebAB8s")# it contains Movie name,its YEAR OF release,its image link,its trailer video link

lagaan = media.Movie("Lagaan", 
			"2001",
			"https://upload.wikimedia.org/wikipedia/en/b/b6/Lagaan.jpg",
			"https://www.youtube.com/watch?v=oSIGQ0YkFxs")# it contains Movie name,its YEAR OF release,its image link,its trailer video link

fanaa = media.Movie("Fanaa", 
			"2006",
			"https://upload.wikimedia.org/wikipedia/en/4/40/Fanaa_Poster.jpg", 
			"https://www.youtube.com/watch?v=kofrlCHyiaU")# it contains Movie name,its YEAR OF release,its image link,its trailer video link

sholay = media.Movie("SHOLAY", 
			"1975", 
			"https://upload.wikimedia.org/wikipedia/en/5/52/Sholay-poster.jpg",
			"https://www.youtube.com/watch?v=hLhzpe3_V_g")# it contains Movie name,its YEAR OF release,its image link,its trailer video link

dil_chahta_hai = media.Movie("Dil Chahta Hai", 
			"2001",
			"https://upload.wikimedia.org/wikipedia/en/d/db/Dil_Chahta_Hai.jpg",
			"https://www.youtube.com/watch?v=m13b25V0B10")# it contains Movie name,its YEAR OF release,its image link,its trailer video link

jab_we_met = media.Movie("Jab We Met", 
			"2007", 
			"https://upload.wikimedia.org/wikipedia/en/9/9f/Jab_We_Met_Poster.jpg", 
			"https://www.youtube.com/watch?v=i7VGyugYCIk")# it contains Movie name,its YEAR OF release,its image link,its trailer video link

swades = media.Movie("SWADES",
                     "2004",
                     "https://upload.wikimedia.org/wikipedia/en/5/5f/Swades_movie_poster.png",
                     "https://www.youtube.com/watch?v=NC7GuohSdWA")# it contains Movie name,its YEAR OF release,its image link,its trailer video link

kal_ho_na_hoo = media.Movie("Kal Ho Naa Ho",
                            "2003",
                            "https://upload.wikimedia.org/wikipedia/en/b/b4/KalHoNaaHo.jpg",
                            "https://www.youtube.com/watch?v=tVMAQAsjsOU")# it contains Movie name,its YEAR OF release,its image link,its trailer video link

movies = [bajrangi_bhaijaan,pk,lagaan,fanaa,sholay,dil_chahta_hai,jab_we_met,swades,kal_ho_na_hoo]# a list is made which contains the details of movies created above

fresh_tomatoes.open_movies_page(movies)# it calls the function to open the videos

			
			

			
			
