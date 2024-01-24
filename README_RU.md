# Ren'Py simple screen filtering demo

[RU](./README_RU.md) | [EN](./README.md)

Библиотека для Ren'Py, позволяющая быстро применять простые фильтры к текущему экрану.

## Определения функций и класса
Все функции определены в [filters.rpy](./game/filters.rpy).

### Класс `simple_filter`
```py
class simple_filter:
    def define(self):
        ## ... ##
    
    def __apply_filter__(self, filter_name, filter_funcion, paths=None):
        ## ... ##

    def enable(self, filter_name=None, filter_transition=None, ignore=[]):
        ## ... ##
    
    def disable(self, filter_name=None, filter_transition=None, ignore=[]):
        ## ... ##
```

Вы можете посмотреть дополнительные комментарии в [этом файле](./game/filters.rpy), чтобы узнать, как они работают.

По умолчанию `simple_filter` применяется `"sepia"` и `"grayscale"` фильтры к всем изображениям.

### Использование
В качестве примера использования, вы можете посмотреть скрипт [script.rpy](./game/script.rpy).

`filter` это предобъявленная переменная в [filters.rpy](./game/filters.rpy), являющаяся объектом класса `simple_filter`.

```py
filter = simple_filter()
```

После этого вы можете использовать `filter` в вашем скрипте.

```py
# применяет фильтр "sepia" с переходом Fade(0.5, 1.0, 0.5, color="#ffffff")
$ filter.enable("sepia", Fade(0.5, 1.0, 0.5, color="#ffffff"))

## ... ##

# отключает фильтр "sepia" с переходом Fade(0.5, 1.0, 0.5, color="#000000")
$ filter.disable("sepia", Fade(0.5, 1.0, 0.5, color="#000000"))
```

Спасибо [этим людям](./CREDITS.md) за визуальную часть новеллы-примера.