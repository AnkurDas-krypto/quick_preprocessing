#APIreference

##text preprocessing using lemmatization

```python 
from quick_preprocessing import lemmatize_preprocessing
```

??? note "EXAMPLE" 
    ### Short Example 
    ```
    EXAMPLE: sent = "hello my name is Ankur. I lives in canada. I am goods. I studies at concordia. I studies software engineering"
    lst= sent.split(".")
    preprocess = lemmatize_preprocessing(lst)
    
    OUTPUT: ['hello name ankur',
     'life canada',
     'good',
     'study concordia',
     'study software engineering']
    ```

##text preprocessing using stemming
```python
from quick_preprocessing import stemming_preprocessing
```

##NOTE 
Input has to be in list