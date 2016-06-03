# content-publisher

content-publisher is a project for selling out video content. All videos we sell are hosted on an external servers(wistia.com) and their links are embedded to a website as a iframe code. If we mark video as a premium then we can sell it out for money by using braintree and payu payment systems.

  - Heroku deyployment with AWS S3: [Link](http://contentpub-pro.herokuapp.com)
  - AWS Elastic Beanstalk deployment with AWS S3: [Link](http://content-publisher-prod.mrcd6tpmj3.eu-central-1.elasticbeanstalk.com/)

### Project features
  - selling out premium accounts via Braintree and PayU systems
  - full user authentication system
  - posibility to register/login with facebook
  - full REST API for category, video and comment models
  - transaction history for braintree and payu systems
  - posibility to embed vimeo and youtube, wistia iframes
  - videos can be commented by users
  - notification when action happens(e.g. comments is made in a thread)
  - analytic systems are implemented

### Technical features
  - django 1.9.5
  - PostgreSQL 9.3 configuration database for production
  - static and media files are hosted in AWS S3 (for both AWS Elastic Beanstalk and Heroku)
  - Redis is used as a Celery broker for Heroku
  - Amazon SQS is used as a Celery broker for AWS Elastic Beanstalk
  - AWS ElastiCache(Redis) is used for session caching in AWS Elastic Beanstalk
  - Redis is used for session caching in Heroku
  - OAuth2 is implemented with Facebook authentication
  - Rest api is expoed vbia django Rest Framework with JWT token
  - email service is provied via Google Gmail account
  - django-debug-toolbar is implemented

### Local deployment tutorial

[---> Link <---](https://github.com/paveu/content-publisher/blob/master/docs/deployment_to_local.md)

### Heroku deployment tutorial

[---> Link <---](https://github.com/paveu/content-publisher/blob/master/docs/deployment_to_heroku.md)

### AWS Elastic Beanstalk deployment tutorial

[---> Link <---](https://github.com/paveu/content-publisher/blob/master/docs/deployment_to_aws_elastic_beanstalk.md)

### Version
* version: 1.4.0
* project started in 08/may/2015. 
* code taken from my old repo: [https://github.com/paveu/srvup](https://github.com/paveu/srvup)

### Todos
  - add Flower for monitor Celery tasks
  - fixing comment thread with angular.js - top priority
  - add fabric deployment script with filling in site id=1 for facebook socialapp
  - add celery for getting exchange rate from usd->pln. do it periodicaly and save a result to database
  - add Sentry for monitoring exepctions happen within the project
  - improving user account panel with angular.js
  - deploying project with fabric script for local/stage and production
  - braintree and payu tutorials for those who wants to run it in production mode
  - add tox, coverage, pytest
  - covering all models along with payment systems with unit and functional tests
  - exposing transaction model with REST API only for thoe users who has permision
  - add automatic resize and compress images with PIL

License
----

MIT

**Free Software, Hell Yeah!**

