# leads-djangon-rest

Need seralized to convert model data to JSON in order to serve to react front end

set up serilaizer by passing it in the inline class
of the model that is to be serliazed
after that pick which fields are the be used for this serializer

in the api file import viewsets, the model and the model serializer

then set up a queryset for example model.objects.all()

set up permissions using permissions_classes

and finally specify the serializer that is to be used

nesxt create urls.py

and import routers from restfw and viewset that was created

set up the router using default router method and register the end point using router.register
router.register required the api end point url, the view set , and a name

finally set up the url patterns

### work flow

    create model
    set up serializer to serliaze model
    create api file and set up viewset with serliazer and model
    create urls.py and import the view set
    register to the viewset with the router and the desired endpoint
    in project.urls.py in the url patterns include the app.urls and that will connect the route
    if permissions were set to any you can get/put/post/delete records

    now when a record exists you can access the record by /api/route_name/:id

    and the routes are preconfigured for you

    the / route would return all records
    by id returns by id
