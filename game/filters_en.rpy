# Copyright (C) 2024, MrDaseMan/KiTsa
# https://github.com/MrDaseMan/
#==================================

#==================================
init 999:   # Initialize in the last queue
    python: # For work with Python

        #====================================
        # Imports
        import copy # Import library for copying dictionaries

        class simple_filter:
            def __init__(self): # Constructor
                pass
            
            def define(self): # Define
                # Apply filter "grayscale" to all images
                self.__apply_filter__("grayscale", im.Grayscale) 

                # Apply filter "sepia" to all images
                self.__apply_filter__("sepia", im.Sepia) 
            #====================================

            #====================================
            # Initialization of filter images
            # Automatically applies the specified filter to all images in the project
            # Creates a new tag with the filtered image with the addition of the filter_name
            #====================================
            # Sample initialization of filter
            # filter.__apply_filter__("grayscale", im.Grayscale) - apply filter "grayscale" to all images
            # or
            # filter.__apply_filter__("sepia", im.Sepia, ["image_tag"]) - apply filter "sepia" only to "image_tag"
            #====================================
            # ARGUMENTS:
            # filter_name - name of the filter
            # filter_funcion - function of filtering
            # paths - list of paths of images (can be left blank to apply the filter to all images)
            #====================================
            def __apply_filter__(self, filter_name, filter_funcion, paths=None):
                images_array = renpy.display.image.images # List of images
                filtered_im_array = {}                    # Dictionary of images with filter

                if paths:                                                  # If the list of image paths is specified
                    images_array = [i for i in images_array if i in paths] # Create a list of images with the specified paths

                for i in images_array: # Iterate through the list of images
                    try:               # Trying to apply the filter
                        filtered_im_name = i + (filter_name,)                                               # Name of the image with the filter
                        filtered_im_array[filtered_im_name] = filter_funcion(renpy.display.image.images[i]) # Apply the filter
                    except:     # If it fails
                        pass    # Skip

                for i in filtered_im_array:              # Iterate through the dictionary of images
                    renpy.image(i, filtered_im_array[i]) # Define the image
            #==================================

            #================================
            # Apply the filter to the current scene
            # To add a new filter, add it above and use the same keyword
            # Add new conditions with another code / add the name of the filter inside conditions (e.g. grayscale)
            #! If you add a new filter, you must add it above and use the same keyword
            #================================
            # Sample usage
            # filter.enable("grayscale", Dissolve(1), ["image_tag"])
            #================================
            # ARGUMENTS:
            # filter_name - name of the filter
            # filter_transition - transition of the filter
            # u can learn more about renpy transitions: https://www.renpy.org/doc/html/transitions.html#transition-classes
            # ignore - list of tags to ignore
            #================================
            def enable(self, filter_name=None, filter_transition=None, ignore=[]):
                if filter_name == "grayscale" or filter_name == "sepia": # If the filter is "grayscale" or "sepia"

                    img_list = []                   # Result list of images with the filter
                    tags = renpy.get_showing_tags() # Get all tags

                    for i in list(tags):               # Iterate through the list of tags
                        tag_name = i                   # Name of the tag
                        full_name = tag_name           # Full name of the tag
                        atrb = renpy.get_attributes(i) # Attributes of the tag

                        for a in atrb:           # Iterate through the list of attributes
                            full_name += ' ' + a # Add the attribute to the full name

                        # =================================
                        # Add the object to the list of images with the filter where: 
                        # tag - tag
                        # name - full name
                        # obj - object of the image
                        img_obj = {
                            "tag": tag_name,
                            "name": full_name,
                            "obj": copy.deepcopy(renpy.display.core.displayable_by_tag("master", tag_name)) # Копируем объект
                        }
                        img_list.append(img_obj) # Add the object to the list
                        # =================================

                    renpy.transition(filter_transition) # Apply the transition
                    renpy.scene()                       # Reset the scene
                    
                    for i in img_list[::-1]:    # Iterate through the list of images
                        if i["tag"] in ignore:  # If the tag is in the list of ignored tags
                            continue            # Skip

                        placement = i["obj"].get_placement()                         # Get the placement of the image
                        renpy.show(i["name"] + " " + filter_name, at_list=[i["obj"]])

                    for i in img_list:              # Iterate through the list of ignored images
                        if i["tag"] not in ignore:  # If the tag is not in the list of ignored tags
                            continue                # Skip
                        
                        placement = i["obj"].get_placement()      # Get the placement of the image
                        renpy.show(i["name"], at_list=[i["obj"]]) # Show the image
            #================================



            #================================
            # Disable the filter
            # To add a new filter, add it above and use the same keyword
            # Add new conditions with another code / add the name of the filter inside conditions (e.g. grayscale)
            #! If you add a new filter, you must add it above and use the same keyword
            #! The filters inside filter.enable() and filter.disable() functions must be the same
            #================================
            # Sample usage:
            # filter.disable("grayscale", Dissolve(1), ["image_tag"])
            #================================
            # ARGUMENTS:
            # filter_name - name of the filter
            # filter_transition - transition of the filter
            # u can learn more about renpy transitions: https://www.renpy.org/doc/html/transitions.html#transition-classes
            # ignore - list of tags to ignore
            #================================            
            def disable(self, filter_name=None, filter_transition=None, ignore=[]):
                if filter_name == "grayscale" or filter_name == "sepia": # If the filter is "grayscale" or "sepia"

                    img_list = []                   # The list of images with the filter
                    tags = renpy.get_showing_tags() # Get all tags                
                    
                    for i in list(tags):                # Iterate through the list of tags
                        tag_name = i                    # Name of the tag
                        full_name = tag_name            # Full name of the tag
                        atrb = renpy.get_attributes(i)  # Attributes of the tag
                        
                        for a in atrb:                  # Iterate through the list of attributes
                            if a != filter_name:        # If the attribute is not the filter
                                full_name += ' ' + a    # Add the attribute to the full name

                        # =================================
                        # Add the object to the list of images with the filter where:
                        # tag - tag
                        # name - full name
                        # obj - object of the image
                        img_obj = {
                            "tag": tag_name, 
                            "name": full_name,
                            "obj": copy.deepcopy(renpy.display.core.displayable_by_tag("master", tag_name)) # Copy the object
                        }
                        img_list.append(img_obj) # Add the object to the list
                        # =================================

                    renpy.transition(filter_transition) # Apply the transition
                    renpy.scene()                       # Reset the scene

                    for i in img_list:            # Iterate through the list of images in reverse
                        if i["tag"] in ignore:          # If the tag is in the list of ignored tags
                            continue                    # Skip

                        placement = i["obj"].get_placement()      # Get the placement of the image
                        renpy.show(i["name"], at_list=[i["obj"]]) # Show the image

                    for i in img_list:                  # Iterate through the list of ignored images
                        if i["tag"] not in ignore:      # If the tag is not in the list of ignored tags
                            continue                    # Skip

                        placement = i["obj"].get_placement()      # Get the placement of the image
                        renpy.show(i["name"], at_list=[i["obj"]]) # Show the image
            #================================

        # Инициализируем
        filter = simple_filter() 
        filter.define()



#================================