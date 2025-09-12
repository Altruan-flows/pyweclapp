# pyweclapp - Methods, classes and class builders for interacting with the weclapp api

This Package contains methods to acess weclapp objects via the api.

## Setup 
#### Step1
Set up your weclapp domain and provide weclapp API token.
```{python}
    import os
    os.environ["WECLAPP_API_TOKEN"] = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx"
    os.environ["WECLAPP_DOMAIN"] = "yourCompany.weclapp.com
```


# weclapp
### Provides basic function for quering the Weclapp API (GET, PUT, POST and DELETE)
You can specify with asType the desired datatype of the response, so that for
example the "result" attribte gets removed when asking for e.g. all orders
in these functions will throw a specialized weclappError if they fail.
PUT function uses the query Parmateter "justUsedProperties" by default to allow
for updates with only changes.


# weclappClasses
### Provides a nested pydantic dataModel for the most used classes with update tracking and metaData handling
To initialise use .fromWeclapp -> e.g. weclappClasses.SalesOrder.fromWeclapp("salesOrderId")
to retrieve the dictionary again use .getUpdateDict("used+") with updateType
To directly Update use .updateWeclapp(), .updateEntity() functions


### Creating Neu class Instances in weclapp
the class also provides you with a template to create an emptyClass. In this case
use the fromBlank() classmethod.
after that all attributes will be set to None, lists or empyt subclasses, that
you can modify or append to.
after compleetion call the postNewEntity() method to post it to weclapp. Please
do not set "id" or "verion"
#### Example
    salesOrder = weclappClasses.SalesOrder.fromBlank()
    salesOrder.customerId = "1234"  
    salesOrder.invoiceAddress.firstName = "Max"
    salesOrder.qmd("1234", addToMetaData=True).booleanValue = True  # Adds a custom Attribute
    orderItem = weclappClasses.OrderItems.fromBlank()
    orderItem.articleId = "1234"
    salesOrder.orderItems.append(orderItem)
    salesOrder.postNewEntity()

### Createing a new class Template
Sometimes you may want to create a new weclappClass that does not exist yet or
update an old one.

#### Setup Example
    from pyweclapp.weclappClasses.weclappClassBlueprint import weclappClassCreator
    weclappClassCreator.WeclappClassCreator(entityName="ticket",
    expamleEntityId="74344116", targetDirectory="util/weclappClasses").createPythonFile()

offers a convenient way to do this.
just specify a  entityName -> "salesOrder", "shipment", "contract", "article", "etc."
                expamleEntityId -> to estimate the types
                targetDirectory -> where the generaed files should be placed
                entity -> overwirtes the starting dictionary (Optional)

This will create the templates for the weclappclass as well as a init file.
if you need supproperties make sure the example entity contains example of this.
Oherwhise it will only be an enpty list without model
#### CATION may overwrite existing files -> choose an empty directory


# CustomAttributes
when working with customAttribes a way of nameing them is important. However the
ids vary form system to system
the CAT classes (CustomATtributes) will generate the a classtemplate like in examples.
ater that the attributes will be accessable with their weclappSystemNames with
suggesions
selectableElements will also be parsed. use bracets in description to choose a
different system Name e.g.: "this is a selectable - Option (MySelectableOption)"
-> Name will be "MySelectableOption"
otherhwise invalid characters will be removed and a "X" will be added if the
startincharacter is invalid

#### CAUTION this may overwrite changes you made in your module. 
#### Setup Example
    from pyweclapp.customAttributes import CAT_Generator
    # specify your wish directory. 
    CAT_Generator(entityName="ticket", entityId="74344116",
    targetDirectory="util/customAttributes")

#### if you only need attribtes for specific entity please use the more specific and lightweight subclasses like cat_SalesOrder

# weclappDoc
### allows you to upload, download or modify documents
it autosets a description (DocDescription class) in json format to make documents
identifiable via code.

### DocManager(entityName, entityId) 
    -> get all documents of a entity: .getDocuments()
    -> Upload a file -> .uploadFile()
    -> download a file -> .getDocumentFiles()

### Document
behaives like a weclapp class -> Document.fromWeclapp()
Allows to:
    -> update -> .updateFile()
    -> download -> .downloadDoc()
    -> set Description -> .setDescription() 
    -> update Description -> .updateDescription()

#### Example
    docManger = pyweclapp.weclappDoc.DocManager("shipment", "74433425")
    availableDocs = docManger.getDocuments()

# timeFunctions
### higher level functions for working with dates in different formats
optimised for woring with weclapp


create wheel with comand >python3 setup.py bdist_wheel sdist