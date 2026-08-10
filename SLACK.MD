https://api.slack.com/apps
Create new workspace: Enterprise AI Lab

Created APP: Blank,
App Name: Product Approval Bot
Workspace: Enterprise AI Lab

Configure OAuth scopes:
OAuth & Permissions -> Under Bot Token Scopes, click Add an OAuth Scope and add these scopes:
chat:write
chat:write.public
channels:read
groups:read
im:write
users:read
Click Install to Workspace, it will be in the top -> Allow

Enable Interactivity
Disable Socket Mode in SOcket Mode section
Add the come to interactivity -> Select ON
and add the url: https://ca-product-api-dev.wittypebble-b04395ef.southindia.azurecontainerapps.io/slack/actions

Install the app to the workspace

Configure FastAPI to receive Slack events

Need to install SSL certificate in local
open "/Applications/Python 3.14/Install Certificates.command"
