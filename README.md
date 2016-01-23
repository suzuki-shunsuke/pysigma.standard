# sigma.standard

sigma.standard is a python validation framework.  
sigma.standard is based on [sigma.core](https://github.com/pysigma/core).  
sigma.standard supports the following validation logics.

* Type(type)
* White List(white_list)
* Black List(black_list)
* Not None(noneable)
* String Length(length)
* Size(size)
* Regular Expression(match, search)

## Example

```python
from sigma.core import Model
from sigma.standard import Field


class User(Model):
    id = Field(type=int, size=(5, 10))
    password = Field(type=str, length=(8, 15))

user = User()
```

```python
user.id = 20  # raise OverMaxError
```

```python
user.password = 10  # raise InvalidTypeError
```

## Install

```
$ pip install sigma.standard
```

## Dependencies

* [sigma.core](https://pypi.python.org/pypi/sigma.core/)

## License

sigma is available under the [MIT License](http://opensource.org/licenses/mit-license.php).
