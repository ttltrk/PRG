
---

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [most used manuals](https://github.com/ttltrk/PRG/blob/master/MUM.MD)

###### [改善](https://github.com/ttltrk/0C/blob/master/README.MD) - [.co.](https://github.com/ttltrk/PRG/blob/master/CODING.MD) - [manuals](https://github.com/ttltrk/PRG/blob/master/MAN.MD) - [basic manuals](https://github.com/ttltrk/PRG/blob/master/MANUALS.MD) - [Scripts](https://github.com/ttltrk/PRG/blob/master/PY/DOC/SC/SC.MD) - [Python](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/PY.MD) - [own manuals](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PY/MAN/MAN.MD) - [PYF](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/PYF.MD) - [DS](https://github.com/ttltrk/PRG/blob/master/PY/DOC/PYF/DataStruct/DS.MD)

###### [SQL](https://github.com/ttltrk/DB/blob/master/SQL/DOC/OSM/OSQLM/SQLM/SQLM.MD#^) - [SS](https://github.com/ttltrk/ELSE/blob/master/SHELL/OSSM/SSCR/SSCR.MD)

---

<h3 id='^'>Python - Front End - Django</h3>

---

```
-----------------------------------------------
#shortcommands

#how to create a project in django
django-admin startproject <project_name>

#first app folder in working dir
python manage.py startapp first_app

conda info --envs
activate MyDjangoEnv
cd C:\Users\AttilaTorok\Desktop\ADM\MM\PY\MYDJANGO\first_project
python manage.py runserver

-----------------------------------------------

1. install anaconda

https://docs.anaconda.com/anaconda/install/windows/

-----------------------------------------------

2.confing anaconda

-----------------------------------------------

3. create a virtual environment

anaconda prompt

conda create --name myDjangoEnv python=3.6

-----------------------------------------------

# To activate this environment, use
#
#     $ conda activate MyDjangoEnv
#
# To deactivate an active environment, use
#
#     $ conda deactivate


(base) C:\Users\AttilaTorok>conda activate MyDjangoEnv

(MyDjangoEnv) C:\Users\AttilaTorok>conda info --envs
# conda environments:
#
base                     C:\Users\AttilaTorok\Anaconda3
MyDjangoEnv           *  C:\Users\AttilaTorok\Anaconda3\envs\MyDjangoEnv


(MyDjangoEnv) C:\Users\AttilaTorok>

-----------------------------------------------

4. install django on virtual env

(MyDjangoEnv) C:\Users\AttilaTorok>conda install django
Solving environment: done

## Package Plan ##

  environment location: C:\Users\AttilaTorok\Anaconda3\envs\MyDjangoEnv

  added / updated specs:
    - django


The following packages will be downloaded:

    package                    |            build
    ---------------------------|-----------------
    pytz-2018.7                |           py36_0         260 KB
    django-2.1.5               |           py36_0         4.4 MB
    ------------------------------------------------------------
                                           Total:         4.7 MB

The following NEW packages will be INSTALLED:

    django: 2.1.5-py36_0
    pytz:   2018.7-py36_0

Proceed ([y]/n)? y


Downloading and Extracting Packages
pytz-2018.7          | 260 KB    | ############################################################################ | 100%
django-2.1.5         | 4.4 MB    | ############################################################################ | 100%
Preparing transaction: done
Verifying transaction: done
Executing transaction: done

(MyDjangoEnv) C:\Users\AttilaTorok>

-----------------------------------------------

5. check the python version

(MyDjangoEnv) C:\Users\AttilaTorok>python
Python 3.6.8 |Anaconda, Inc.| (default, Dec 30 2018, 18:50:55) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

-----------------------------------------------

6. check the actual version on your comp (not on virtual env)

(MyDjangoEnv) C:\Users\AttilaTorok>deactivate

(base) C:\Users\AttilaTorok>
(base) C:\Users\AttilaTorok>
(base) C:\Users\AttilaTorok>python
Python 3.7.1 (default, Dec 10 2018, 22:54:23) [MSC v.1915 64 bit (AMD64)] :: Anaconda, Inc. on win32
Type "help", "copyright", "credits" or "license" for more information.
>>>

-----------------------------------------------

7. how to activate django env

(base) C:\Users\AttilaTorok\Desktop\ADM\MM\PY\MYDJANGO>activate MyDjangoEnv

(MyDjangoEnv) C:\Users\AttilaTorok\Desktop\ADM\MM\PY\MYDJANGO>

-----------------------------------------------

8. create project

(MyDjangoEnv) C:\Users\AttilaTorok\Desktop\ADM\MM\PY\MYDJANGO>django-admin startproject first_project

(MyDjangoEnv) C:\Users\AttilaTorok\Desktop\ADM\MM\PY\MYDJANGO>


#how to create a project in django
django-admin startproject <project_name>

-----------------------------------------------

9. start the django server - you can logoff with ctrl+c

(MyDjangoEnv) C:\Users\AttilaTorok\Desktop\ADM\MM\PY\MYDJANGO>cd first_project

(MyDjangoEnv) C:\Users\AttilaTorok\Desktop\ADM\MM\PY\MYDJANGO\first_project>python manage.py runserver

and copy paste the IP to the browser

-----------------------------------------------

10. how to start an app

(MyDjangoEnv) C:\Users\AttilaTorok\Desktop\ADM\MM\PY\MYDJANGO\first_project>python manage.py startapp first_app

(MyDjangoEnv) C:\Users\AttilaTorok\Desktop\ADM\MM\PY\MYDJANGO\first_project>

-----------------------------------------------

check out the udemy course for hello world
```

---
