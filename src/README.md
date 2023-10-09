# pyWeclapp - Methods, classes and class builders for interacting with the weclapp aoi

This Package contains methods to acess weclapp objects via the api.

## Setup 
#### Spep1
set the weclappDomain to call to to environment variables:
os.environ["weclappDomain"] = "yourCompany.weclapp.com"

#### Spep2
set the authenticationToken obtainable from weclapp via:
your Account -> my settings -> API-Token
the token should have the format xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
set the default token as "Weclapp_AuthenticationToken0" via os.environ["Weclapp_AuthenticationToken0"] = yourToken

#### Spep3
For some applications it is usefull to set multiple tokens from different users. Please index them e.g. "Weclapp_AuthenticationToken1", "Weclapp_AuthenticationToken2"
the Api Key can be referenced in selected functions via it's short name key0 or key1  or ...; key0=default

