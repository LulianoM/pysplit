# Instalando o PySPLIT

O PySPLIT é compatível com Python 2.7, 3.6 e 3.7. Ele depende dos seguintes pacotes:

    NumPy >= 1.6
    matplotlib >= 1.2
    Basemap >= 1.0
    GeoPandas >= 0.1
    Cartopy >= 0.15

e está disponível no PyPi. Você pode instalar a versão estável mais recente executando o seguinte comando:

```
$ pip install pysplit
```

Para instalar a partir do código-fonte ou criar uma instalação de desenvolvimento, clone e faça um fork do PySPLIT e, em seguida, instale executando:

```
$ python setup.py install
```

ou desenvolva localmente executando:

```
$ python setup.py develop
```

Instalando em um ambiente virtual conda:

As dificuldades de instalação com o PySPLIT geralmente estão relacionadas às dependências do GeoPandas. Uma solução simples é instalar o PySPLIT em um novo ambiente virtual conda. Este é o método de instalação recomendado. Primeiro, adicione o canal conda-forge:

```
$ conda config --add channels conda-forge
```


Em seguida, crie o ambiente conda. Para um ambiente Python 3.6 chamado pysplitenv, execute o seguinte comando:

```
$ conda create --name pysplitenv python=3.6 numpy matplotlib pandas basemap six fiona shapely geopandas cartopy
```

Da mesma forma, para um ambiente Python 3.7 chamado pysplitenv, execute o seguinte comando:

```
$ conda create --name pysplitenv python=3.7 numpy matplotlib pandas basemap six fiona shapely geopandas cartopy
```

Ou, para criar um ambiente Python 2.7 chamado pysplitenv, execute o seguinte comando:

```
$ conda create --name pysplitenv python=2.7 numpy matplotlib pandas basemap six fiona=1.5.1 shapely geopandas cartopy
```

Ative o pysplitenv executando o seguinte no Windows:

```
$ activate pysplitenv
```

Se você estiver no Linux ou OSX, execute o seguinte comando em vez disso:

```
$ source activate pysplitenv
```

Dentro do seu ambiente virtual, instale o PySPLIT como descrito acima.