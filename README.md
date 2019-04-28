
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/Stefanitsky)  [![PyPI version](https://badge.fury.io/py/rephunt.svg)](https://badge.fury.io/py/rephunt) [![GitHub version](https://badge.fury.io/gh/stefanitsky%2Frephunt.svg)](https://badge.fury.io/gh/stefanitsky%2Frephunt)
# RepHunt

RepHunt - is a simple console app for those, who want to increase their
reputation on any of the sites, that are included in the Stack Exchange.

![Stack Overflow](https://cdn.sstatic.net/Sites/stackoverflow/img/apple-touch-icon.png)| ![Server Fault](https://cdn.sstatic.net/Sites/serverfault/img/apple-touch-icon.png) | ![Super User](https://cdn.sstatic.net/Sites/superuser/img/apple-touch-icon.png)
:---: | :---: | :---:
[Stack Overflow](https://stackoverflow.com/)| [Server Fault](https://serverfault.com/) | [Super User](https://superuser.com/)
![Meta Stack Exchange](https://meta.stackexchange.com/content/Sites/stackexchangemeta/img/apple-touch-icon.png)| ![Web Applications](https://cdn.sstatic.net/Sites/webapps/img/apple-touch-icon.png) | ![Arqade](https://cdn.sstatic.net/Sites/gaming/img/apple-touch-icon.png)
[Meta Stack Exchange](https://meta.stackexchange.com/) | [Web Applications](https://webapps.stackexchange.com) | [Arqade](https://gaming.stackexchange.com)
![Webmasters](https://cdn.sstatic.net/Sites/webmasters/img/apple-touch-icon.png) | ![Seasoned Advice](https://cdn.sstatic.net/Sites/cooking/img/apple-touch-icon.png) | ![Game Development](https://cdn.sstatic.net/Sites/gamedev/img/apple-touch-icon.png)
[Webmasters](https://webmasters.stackexchange.com) | [Seasoned Advice](https://cooking.stackexchange.com) | [Game Development](https://gamedev.stackexchange.com)
![Photography](https://cdn.sstatic.net/Sites/photo/img/apple-touch-icon.png) | ![Cross Validated](https://cdn.sstatic.net/Sites/stats/img/apple-touch-icon.png) | ![Mathematics](https://cdn.sstatic.net/Sites/math/img/apple-touch-icon.png)
[Photography](https://photo.stackexchange.com) | [Cross Validated](https://stats.stackexchange.com) | [Mathematics](https://math.stackexchange.com)
![Home Improvement](https://cdn.sstatic.net/Sites/diy/img/apple-touch-icon.png) | ![Geographic Information Systems](https://cdn.sstatic.net/Sites/gis/img/apple-touch-icon.png) | ![TeX - LaTeX](https://cdn.sstatic.net/Sites/tex/img/apple-touch-icon.png)
[Home Improvement](https://diy.stackexchange.com) | [Geographic Information Systems](https://gis.stackexchange.com) | [TeX - LaTeX](https://tex.stackexchange.com)
| ![Ask Ubuntu](https://cdn.sstatic.net/Sites/askubuntu/img/apple-touch-icon.png) | | |
| [Ask Ubuntu](https://askubuntu.com) |

## Installation & Documentation & Usage with [pip](https://pip.pypa.io/en/stable/)

```bash
pip install rephunt
python -m rephunt -h
python -m rephunt --tag python --count 5

...
Title: Using transform together with nth
Asked: 4 minutes ago
Stats: 0 votes | 1 answers | 6 views | answered: no
Tags: python, pandas, pandas-groupby
Link: https://stackoverflow.com/questions/55891019/using-transform-together-with-nth
...
```

## Documentation & Usage:

#### Default documentation:
```bash
pip -m rephunt -h
```

#### Usage
```bash
Optional arguments:
  -h, --help
            show this help message and exit
  
  -s {stackoverflow,serverfault,superuser,meta,webapps,gaming,webmasters,cooking,gamedev,photo,stats,math,diy,gis,tex,askubuntu}, --site {stackoverflow,serverfault,superuser,meta,webapps,gaming,webmasters,cooking,gamedev,photo,stats,math,diy,gis,tex,askubuntu}
            select the needed site (default: stackoverflow)
                        
  -c COUNT, --count COUNT
            select the number of questions to display (default:10)
                        
  -o {desc,asc}, --order {desc,asc}
            select order type (default: desc)
                        
  --sort {activity,votes,creation,hot,week,month}
            select sort type (default: creation)
                        
  -t TAG, --tag TAG
            select tag for filtering questions (default: None)

```

## License
[MIT](https://github.com/Stefanitsky/rephunt/blob/master/LICENSE.md)