from art_showcase import showcase 

# showcase a maximum 5 fonts only , limit = 0 returns everthing font that meets the specs
fonts_showcased = showcase( "Hellothere", limit = 2 )
# fonts_showcased =  ['1943', '1row']


# Set the pause time in seconds in between fonts
fonts_showcased = showcase("Hellothere" , sleep = 0.1 , limit = 3 )
# fonts_showcased = ['1943', '1row', '3-d']


# Set constraints for the fonts to showcase

# Check if a font name contains the text provided
fonts_showcased = showcase( "Hellothere",
							contains = "re",
							sleep = 0.1,
							  )
# fonts_showcased = ['barbwire', 'fire_font-s', 'fireing', 'future_1', 'future_2', 'future_3', 'future_4', 'future_5', 'future_6', 'future_7', 'future_8', 'greek', 'green_be', 'ogre', 'rectangles', 'red_phoenix', 'rev', 'stforek', 'threepoint', 'trek']

# Check if a font name starts the text provided
fonts_showcased = showcase( "Hellothere",
							startswith = "3",
							sleep = 0.1,
							  )
# fonts_showcased = ['3-d', '3d_diagonal', '3x5']



# Check if a font name endswith the text provided
fonts_showcased = showcase( "Hellothere",
							enpdswith = "zy",
							sleep = 0.1,
							  )
# fonts_showcased = ['fuzzy']


# Randomize the showcase output
fonts_showcased = showcase( "Hellothere",
							startswith = "3",
							sleep = 0.1,
							randomize =  True
							  )
# fonts_showcased will be a random list containing these values :
#  ['3x5', '3d_diagonal', '3-d']



# Add the font names you want to showcase specifically 
# Note that they must be in the list art.FONT_NAMES
fonts_showcased = showcase( "Hellothere", fonts = ["fuzzy" , "os2"])

