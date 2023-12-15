The processing pattern is quite obscure, with the github action configured by action.yml. When you run the action integration.yml, it looks at action.yml (github does this w/o any asking-- you just have to know it happens). 
-- action.yml triggers the dockerfile 
-- dockerfile builds a Docker container, copying the source ttl files directory,  the tools folder with vocab.py and vocab2md.py, github actions main github_action_main.py, and a Makefile 
github_action_main.py is set as the entrypoint for the container Its input arguments are passed as environmental variables: 'command' (values are 'doc' or 'uijson') and 'path' environmental variables (which are defined in action.yml, and assigned values in integration.yml )

-- when the workflow is run, the docker container gets spun up, and the entrypoint script github_action_main.py is executed.  This python executes the Makefile inside the container using subprocess.run call. Its hard to tell what actually gets run in the makefile, but it look mostly like it sets up a cache directory and runs vocab.py to load the turtle into an sqlAlchemy datastore that is accessed using SPARQL queries.   calls to vocab.py are made in github_action_main.py and in the Makefile [TBD figure out if this is necessary]

