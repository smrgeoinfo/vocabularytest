# iSamples Vocabularies 

## Vocabulary github action

The vocabulary respository may be run as a GitHub action.  The `action.yml` (which is required to be located at the root of the repository) defines the action inputs and outputs.  

The action is run as a Docker image, and the image is built according to the instructions in the `Dockerfile` (which is also in the root of the repository, due to Docker's requirement that all things built into the image be located in the same directory).

The code in this repository is designed to read a vocabulary serialized using SKOS RDF/Turtle. The source turtle files, with file extension '.ttl', are expected to reside in the vocabulary directory in the repository.

The processing pattern: 
1.  with the github action configured by action.yml. When you run the action integration.yml, it looks at action.yml (github does this w/o any asking-- you just have to know it happens). 
-- action.yml triggers deploying a Docker container defined by Dockerfile 
-- Dockerfile builds a Docker container, copying these files from the host repository:
  1) the source ttl files directory from /vocabulary,  
  2) the /tools folder with vocab.py and vocab2md.py,
  3) .github/actions/github_action_main.py, and 
  4) /Makefile. The make file has rules that can be used on invocation, including 


github_action_main.py is set as the entrypoint for the container Its input arguments are passed as environmental variables:
  1) 'command' (values are 'doc' or 'uijson') and
  2) 'path' environmental variables (which are defined in action.yml, and assigned values in integration.yml )

-- when the workflow is run, the docker container gets spun up, and the entrypoint script github_action_main.py is executed.  This python executes the Makefile inside the container using subprocess.run call. Its hard to tell what actually gets run in the makefile, but it look mostly like it sets up a cache directory and runs vocab.py to load the turtle into an sqlAlchemy datastore that is accessed using SPARQL queries.   calls to vocab.py are made in github_action_main.py and in the Makefile [TBD figure out if this is necessary]



### Testing
There is a test file at `.github/workflows/integration.yml`, which can be run manually using the workflow dispatch option.  It contains the necessary instruction to check out the repository and run it as a GitHub action.

### Implementation
The Docker entrypoint of the action is the python file located at `.github/actions/vocabularies/github_action_main.py`.  GitHub is responsible for converting the action parameters into environment variables that the script interprets.
