# Ren'Py simple screen filtering demo

[RU](./README_RU.md) | [EN](./README.md)

Ren'Py library for simple screen filtering 

Here u can see an example project which demonstrates how to use simple screen filtering in Ren'Py.

## Definitions
All functions are defined in [filters.rpy](./game/filters.rpy) file.

### Structure of `simple_filter` **class**

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

U can check additional comments inside [that file](./game/filters.rpy) to see how it works step by step.

By default, `simple_filter` class is applied `"sepia"` and `"grayscale"` filters to all images.

### Usage
To see an example of usage, you can see [that script](./game/script.rpy).

`filter` is predefined variable in [filters.rpy](./game/filters.rpy). It is an object of `simple_filter` class.

```py
filter = simple_filter()
```

After that, you can use `filter` in your script.

```py
# enable the "sepia" filter with Fade(0.5, 1.0, 0.5, color="#ffffff") transition
$ filter.enable("sepia", Fade(0.5, 1.0, 0.5, color="#ffffff"))

## ... ##

# disable the "sepia" filter with Fade(0.5, 1.0, 0.5, color="#000000") transition
$ filter.disable("sepia", Fade(0.5, 1.0, 0.5, color="#000000"))
```

Thanks for [this guys](./CREDITS.md) for visual part of example novel.