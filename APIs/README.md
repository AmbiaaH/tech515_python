# API Fundamentals

## What are APIs? How are they used and why are they so popular?
What is an API?
* Application programming interface
* provides a service that ...
  * give access to resources (images, data, webpags, videos)
  * allow you to take a certain action 
* API is built to represent certain resources

From APi provider perspective
*provide a service which is easy to implement, maintain, extend and scale 

Why might devOps/support engineers need to use APIs
* Automate interactions with cloud servics, esp for configuration/administration
* simulate user actions or workflows to try and repreoduce + test  issues
* Access data to help troubleshooting/diagnosis
* Retrieve and manipulate data frome external systems and services



## Create a diagram to showcase the data transfer process in API communication.

*Often uses JSON
*   ````JSON
{
    Key:Value
    Key:Value
    Key:Value
    Key:Value
     
}

* or XML

## What is a REST API? What makes an API RESTful? What are the REST guidelines?
* REST: 
  * representational state transfer
  * Type of architecture use for the API
  * Primarily used to build web services that are lightweight, maintainable, scaleable 
  * Also called RESTful srrvice 
  * uses HTTP as its protocol 
*If RESTful must have these properties:
  * Representations and data flow
  * Messages
  * URI / naming resources
  * stateless
  * caching 

    


## What is HTTP? (what does it stand for and what is it used for? What is HTTPS?)

* HTTP = HYPERTEXT TRANSFER PROTOCOL 
* HTTPS = as above with SECURE

## Explain HTTP request structure using the diagrams provided, or your own.
> see diagram
## Explain HTTP response structure using the diagram provided, or your own.
> see diagram
## What are the 5 HTTP verbs and what do they do?

GET → read
POST → create
PUT → update (replacement)
PATCH → update (changing partial)
DELETE → ? (delete)


## URIs and naming of resources

* searching for different types od data 


## What is statelessness? Show examples of “stateless” and stateful http requests.

* keeps track of request if stateful 
* doesnt keep track of requsted data 

## What is caching?

* storing results of previous requests to speed up similar or identical requests in the future
* can be stored on the client, server or any other component between them (such as proxy server)
* 