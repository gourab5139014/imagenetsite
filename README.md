We will be scraping, transforming, storing, transforming, and displaying some data.

### 1. First, we'll need data

ImageNet (http://imagenet.stanford.edu/) is a commonly used dataset in machine learning research. We'll be using its taxonomy system.

When you go to http://imagenet.stanford.edu/synset?wnid=n02486410, you'll see a tree on the left. Your job is to scrape this tree and transform it into a linear form, like this:

```
[
    {name: 'ImageNet 2011 Fall Release', size: 32326},
    {name: 'ImageNet 2011 Fall Release > plant, flora, plant life', size: 4486},
    {name: 'ImageNet 2011 Fall Release > plant, flora, plant life > phytoplankton', size: 2},
    {name: 'ImageNet 2011 Fall Release > plant, flora, plant life > phytoplankton > planktonic algae', size: 0},
    {name: 'ImageNet 2011 Fall Release > plant, flora, plant life > phytoplankton > diatom', size: 0},
    {name: 'ImageNet 2011 Fall Release > plant, flora, plant life > microflora', size: 0},
    ...
]
```

We'll use `>` as a separator of categories/subcategories.

It's completely up to you how you download this data, everything is allowed.

### 2. Second, we'll need to store it somewhere

Create a database (use any database system you like or want to try) to store these tuples `(string, number)` and fill it with the data you obtained in the first step.

### 3. Making sense of it

Next, we'll convert it back to a tree. Why not. Like this:

```
{
    name: 'ImageNet 2011 Fall Release',
    size: 32326,
    children: [
        {
            name: 'plant, flora, plant life',
            size: 4486,
            children: [
                {
                    name: 'phytoplankton',
                    size: 2,
                    children: [
                        ...
                    ]
                },
                ...
            ]
        },
        ...
    ]
}
```

* Can you write an algrorithm that will output such a tree? No cheating here, you have to read this data in a linear form from the database.
* What is the complexity of your algorithm (in big O notation)?

### 3. Now it's time to show the data again

* Can you design and build an interface to show this data?
* Can you implement search in this UI?

<hr>

Feel free to use any tools, frameworks or libraries. Whatever you are most comfortable with or something new that you wanted to try for a long time. Just let me know what you chose, why, and what was your previous experience with it.

## Template

     ,-----.,--.                  ,--. ,---.   ,--.,------.  ,------.
    '  .--./|  | ,---. ,--.,--. ,-|  || o   \  |  ||  .-.  \ |  .---'
    |  |    |  || .-. ||  ||  |' .-. |`..'  |  |  ||  |  \  :|  `--, 
    '  '--'\|  |' '-' ''  ''  '\ `-' | .'  /   |  ||  '--'  /|  `---.
     `-----'`--' `---'  `----'  `---'  `--'    `--'`-------' `------'
    ----------------------------------------------------------------- 


Welcome to your Django project on Cloud9 IDE!

Your Django project is already fully setup. Just click the "Run" button to start
the application. On first run you will be asked to create an admin user. You can
access your application from 'https://imagenetsite-gourab5139104.c9users.io/' and the admin page from 
'https://imagenetsite-gourab5139104.c9users.io/admin'.

## Starting from the Terminal

In case you want to run your Django application from the terminal just run:

1) Run syncdb command to sync models to database and create Django's default superuser and auth system

    $ python manage.py migrate

2) Run Django

    $ python manage.py runserver $IP:$PORT
    
## Configuration

You can configure your Python version and `PYTHONPATH` used in
Cloud9 > Preferences > Project Settings > Language Support.

## Support & Documentation

Django docs can be found at https://www.djangoproject.com/

You may also want to follow the Django tutorial to create your first application:
https://docs.djangoproject.com/en/1.9/intro/tutorial01/

Visit http://docs.c9.io for support, or to learn more about using Cloud9 IDE.
To watch some training videos, visit http://www.youtube.com/user/c9ide