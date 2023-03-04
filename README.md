# Overview
PythonicGardening is a set of tools built to allow a user to create and publish content to their Quartz repository. It was designed to incorporate [CI/CD](https://www.redhat.com/en/topics/devops/what-is-ci-cd) concepts into a users workflow with Quartz. 

It is used in [GeorgeOnTheWeb](https://github.com/Vignettes/GeorgeOnTheWeb) to allow me to create and push journal entries and quick notes directly to [my digital garden](https://www.georgewolf.net) without leaving the terminal.

## Why use the terminal when other tools are available?
Because the terminal is a distraction-free environment. You can jot down your note and have it online in under 2 minutes. 

# Features
PythonicGardening will allow you to:
- Create a MarkDown file from template
	- Move created template to content folder--assumes you are using [Quartz](https://quartz.jzhao.xyz)
- Edit a MarkDown file
	- Both from template and as a new file
- Push created files to your GitHub repository
 
# Roadmap
## Committed
- Allow user to create custom frontmatter templates to format content
- Update title in frontmatter based on user input
- Allow users to customize config.py for:
	- Content directory (contentDir)  to place created MarkDown files
	- Git commit message (COMMIT_MESSAGE) to change standard commit verbiage
	- Git repo path (PATH_OF_GIT_REPO) to change local repo targed for push

## Uncomitted
- Graphical interface 
	- Ruins the "all in terminal" value, would be an optional feature
- Image upload

## Requests
Feature requests will be added here.

# Interested in contributing?
You can contact me with questions or just fork this repo. 
