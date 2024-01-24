# Copyright (C) 2024, MrDaseMan/KiTsa
# https://github.com/MrDaseMan/
#==================================

#==================================
init 999:   # Инициализируется в самую последнюю очередь
    python: # Для работы с Python

        #====================================
        # Импорты
        import copy # Импортируем библиотеку для копирования словарей

        class simple_filter:
            def __init__(self): # Конструктор
                pass
            
            def define(self): # Определение
                # Применяем фильтр "grayscale" ко всем изображениям
                self.__apply_filter__("grayscale", im.Grayscale) 

                # Применяем фильтр "sepia" ко всем изображениям
                self.__apply_filter__("sepia", im.Sepia) 
            #====================================

            #====================================
            # Инициализация фильтров изображений
            # Автоматически накладывает заданный фильтр на заданные или все (по умолчанию) изображения в проекте
            # Создаёт новый тэг с фильтрованным изображением с добавлением filter_name
            #====================================
            # Пример инициализации фильтра
            # filter.__apply_filter__("grayscale", im.Grayscale) - применить фильтр "grayscale" ко всем изображениям
            # или
            # filter.__apply_filter__("sepia", im.Sepia, ["image_tag"]) - применить фильтр "sepia" только к "image_tag"
            # на выходе получим изображения с тэгом "image-name grayscale", "image-name sepia"
            #====================================
            # АРГУМЕНТЫ:
            # filter_name - название фильтра
            # filter_funcion - функция фильтрации
            # paths - список путей изображений (можно не задавать, чтобы применить фильтр ко всем изображениям)
            #====================================
            def __apply_filter__(self, filter_name, filter_funcion, paths=None):
                images_array = renpy.display.image.images # Список изображений
                filtered_im_array = {}                    # Словарь изображений с фильтром

                if paths:                                                  # Если список путей изображений задан
                    images_array = [i for i in images_array if i in paths] # Создаем список изображений с заданными путями

                for i in images_array: # Перебираем список изображений
                    try:               # Пытаемся применить фильтр
                        filtered_im_name = i + (filter_name,)                                               # Имя изображения с фильтром
                        filtered_im_array[filtered_im_name] = filter_funcion(renpy.display.image.images[i]) # Применяем фильтр
                    except:     # Если не получилось
                        pass    # Пропускаем

                for i in filtered_im_array:              # Перебираем словарь
                    renpy.image(i, filtered_im_array[i]) # Объявляем изображение
            #==================================

            #================================
            # Применяем фильтр к текущей сцене
            # Чтобы добавить новый фильтр в игре, необходимо следующее:
            # Добавить новое условие с другой механикой / добавить название фильтра в условие (например: grayscale)
            #! Если вы добавляете новый фильтр, то необходимо добавить его выше и использовать аналогичный keyword.
            #================================
            # Пример применения фильтра:
            # filter.enable("grayscale", Dissolve(1), ["image_tag"])
            #================================
            # АРГУМЕНТЫ: 
            # filter_name - название фильтра
            # filter_transition - переход во время применения фильтра
            # ознакомиться с существующими переходами можно на странице https://www.renpy.org/doc/html/transitions.html#transition-classes
            # ignore - игнорируемые картинки (не применяем фильтр к ним)
            def enable(self, filter_name=None, filter_transition=None, ignore=[]):
                if filter_name == "grayscale" or filter_name == "sepia": # Если фильтр "grayscale" или "sepia"

                    img_list = []                   # Итоговый список всех изображений на экране
                    tags = renpy.get_showing_tags() # Получаем теги текущих изображений на экране

                    for i in list(tags):               # Перебираем все теги
                        tag_name = i                   # Тег
                        full_name = tag_name           # Полное имя изображения с атрибутами
                        atrb = renpy.get_attributes(i) # Получаем атрибуты изображения 

                        for a in atrb:           # Перебираем атрибуты
                            full_name += ' ' + a # Добавляем атрибуты в полное имя

                        # =================================
                        # Добавляем в список картинки с атрибутами, где:
                        # tag - тег
                        # name - полное имя
                        # obj - объект картинки
                        img_obj = {
                            "tag": tag_name,
                            "name": full_name,
                            "obj": copy.deepcopy(renpy.display.core.displayable_by_tag("master", tag_name)) # Копируем объект
                        }
                        img_list.append(img_obj) # Добавляем в список
                        # =================================

                    renpy.transition(filter_transition) # Применяем переход
                    renpy.scene()                       # Сбрасываем сцену
                    
                    for i in img_list[::-1]:    # Перебираем инвертированный список
                        if i["tag"] in ignore:  # Если тег в списке игнорируемых
                            continue            # Пропускаем

                        placement = i["obj"].get_placement()                         # Получаем позицию текущего изображения
                        renpy.show(i["name"] + " " + filter_name, at_list=[i["obj"]])

                    for i in img_list:              # Перебираем список игнорируемых изображений
                        if i["tag"] not in ignore:  # Если тег не в списке игнорируемых
                            continue                # Пропускаем
                        
                        placement = i["obj"].get_placement()     # Получаем позицию текущего изображения
                        renpy.show(i["name"], at_list=[i["obj"]])
            #================================



            #================================
            # Убирает фильтр с текущей сцены
            # Чтобы добавить новый фильтр в игре, необходимо следующее:
            # Добавить новое условие с другой механикой / добавить название фильтра в условие (например: grayscale)
            #! Если вы добавляете новый фильтр, то необходимо добавить его выше и использовать аналогичный keyword.
            #! Фильтры внутри функции filter.enable() и filter.disable() должны совпадать.
            #================================
            # Пример применения функции:
            # filter.disable("grayscale", Dissolve(1), ["image_tag"])
            #================================
            # АРГУМЕНТЫ: 
            # filter_name - название фильтра
            # filter_transition - переход во время применения фильтра
            # ознакомиться с существующими переходами можно на странице https://www.renpy.org/doc/html/transitions.html#transition-classes
            # ignore - игнорируемые картинки (не применяем фильтр к ним)
            def disable(self, filter_name=None, filter_transition=None, ignore=[]):
                if filter_name == "grayscale" or filter_name == "sepia": # Если фильтр "grayscale" или "sepia"

                    img_list = []                   # Список изображений
                    tags = renpy.get_showing_tags() # Теги текущих изображений                   
                    
                    for i in list(tags):                # Перебираем теги
                        tag_name = i                    # Тег
                        full_name = tag_name            # Полное имя изображения с атрибутами
                        atrb = renpy.get_attributes(i)  # Получаем атрибуты изображения
                        
                        for a in atrb:                  # Перебираем атрибуты
                            if a != filter_name:        # Если атрибут не равен фильтру
                                full_name += ' ' + a    # Добавляем атрибуты в полное имя

                        # =================================
                        # Добавляем в список картинки с атрибутами, где:
                        # tag - тег
                        # name - полное имя
                        # obj - изображение
                        img_obj = {
                            "tag": tag_name, 
                            "name": full_name,
                            "obj": copy.deepcopy(renpy.display.core.displayable_by_tag("master", tag_name)) # Копируем объект
                        }
                        img_list.append(img_obj) # Добавляем в список
                        # =================================

                    renpy.transition(filter_transition) # Применяем переход
                    renpy.scene()                       # Сбрасываем сцену

                    for i in img_list[::-1]:            # Перебираем инвертированный список
                        if i["tag"] in ignore:          # Если тег в списке игнорируемых
                            continue                    # Пропускаем

                        placement = i["obj"].get_placement()      # Получаем позицию текущего изображения
                        renpy.show(i["name"], at_list=[i["obj"]]) # Отображаем изображение

                    for i in img_list:                  # Перебираем список игнорируемых изображений
                        if i["tag"] not in ignore:      # Если тег не в списке игнорируемых
                            continue                    # Пропускаем

                        placement = i["obj"].get_placement()      # Получаем позицию текущего изображения
                        renpy.show(i["name"], at_list=[i["obj"]]) # Отображаем изображение
            #================================

        # Инициализируем
        filter = simple_filter() 
        filter.define()



#================================