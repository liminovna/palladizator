# palladizator
![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/liminovna/palladizator/blob/colab_version/palladizator.ipynb

Эта программа транскрибирует китайский язык на русский.

Пригодится, например, когда нужно оформить список литературы в работе, где использовались китайские источники.
Или при переводе текстов, в которых называются объекты/явления, которым нет соответствий в русском языке.
<sub><sub>(или когда вы с подругой полиной щянё цунго напэньё)<sub><sub>

```
>>> python palladius.py "国家语委现代汉语平衡语料库" 
>>> гоцзя юй вэй сяньдай ханьюй пинхэн юйляоку
```

Можно поставить флажок -c -- тогда все слова будут писаться с большой буквы.

  
```
>>> python palladius.py -c "国家语委现代汉语平衡语料库" 
>>> Гоцзя Юй Вэй Сяньдай Ханьюй Пинхэн Юйляоку
```

Основывается на [g2pc](https://github.com/Kyubyong/g2pC), который предусматривает снятие омографии
  
Буду править и оптимизировать, а пока это -- просто рабочий код.

 
# palladizator
  
At this point it just works. Later on i'm planning on revising the code and maybe switching to some api instead of using g2pc on the local machine.

This programm is supposed to transcribe Chinese into Russian and is powered by G2pC library.

```
>>> python palladius.py "国家语委现代汉语平衡语料库" 
>>> гоцзя юй вэй сяньдай ханьюй пинхэн юйляоку
```

At this point it just works. Later on i'm planning on revising the code and maybe switching to some api instead of using g2pc on the local machine.
