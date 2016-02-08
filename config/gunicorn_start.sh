#!/bin/sh

#NAME="ronak_blog"
#DJANGODIR=/home/django_blog
#SOCKFILE=/tmp/foofish.sock
#USER=root
#GROUP=root
#NUM_WORKERS=3
#DJANGO_SETTINGS_MODULE=settings.prod
#DJANGO_WSGI_MODULE=wsgi

#echo "Starting $NAME as `whoami`"

#cd $DJANGODIR
#source /root/envs/django_blog/bin/activate
#export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
#export PYTHONPATH=$DJANGODIR:$PYTHONPATH

#RUNDIR=$(dirname $SOCKFILE)
#test -d $RUNDIR || mkdir -p $RUNDIR

#exec /root/envs/django_blog/bin/gunicorn ${DJANGO_WSGI_MODULE}:application \
#--name $NAME \
#--workers $NUM_WORKERS \
#--user=$USER --group=$GROUP \
#--log-level=error \
#--bind=unix:$SOCKFILE

NAME="ronak_blog"
DJANGODIR=/home/ubuntu/websites/simplecode.in
SOCKFILE=/home/ubuntu/dblog.sock
USER=ubuntu
GROUP=ubuntu
NUM_WORKERS=3
DJANGO_SETTINGS_MODULE=django_blog.settings.dev
DJANGO_WSGI_MODULE=django_blog.wsgi

echo "Starting $NAME as `whoami`"

cd $DJANGODIR
source /home/ubuntu/virtenvs/simplecode/bin/activate
export DJANGO_SETTINGS_MODULE=$DJANGO_SETTINGS_MODULE
export PYTHONPATH=$DJANGODIR:$PYTHONPATH

RUNDIR=$(dirname $SOCKFILE)
test -d $RUNDIR || mkdir -p $RUNDIR

exec gunicorn ${DJANGO_WSGI_MODULE}:application \
--name $NAME \
--workers $NUM_WORKERS \
--user=$USER --group=$GROUP \
--log-level=error \
--bind=unix:$SOCKFILE
