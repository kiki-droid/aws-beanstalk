# aws-beanstalk

Python code to host a dynamic website on Amazon Web Services (AWS) Beanstalk using boto library.

For using this you need to sign up with AWS. You need to create and use security access key for your personal use, then create a Simple Storage Service (S3) bucket and upload zip file of the web application. Then put the name of bucket and access key in the codes launch_1.py and launch_2.py. 

The application used here is a To-do List made using flask library of python and html. If you are using any other programming language than python to make the application do change it to that language in the 'PlatformArn' in the launch_2.py.

Finally to run the program launch_1.py first then followed by launch_2.py.
