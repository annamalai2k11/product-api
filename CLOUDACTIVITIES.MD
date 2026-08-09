Created Azure Free Account with free subscription

=> Created Resource Group: rg-product-api-dev
| Setting | Value |
| -------------- | -------------------- |
| Subscription | Azure subscription 1 |
| Resource Group | `rg-product-api-dev` |
| Region | South India |

Tags:
| Key | Value |
| ----------- | -------------- |
| environment | development |
| project | product-api |
| managed-by | github-actions |
| owner | annamalai |

=> Created Container Apps
| Setting | Value |
| ---------------------------- | -------------------- |
| Name | `ca-product-api-dev` |
| Region | South India |
| Deployment Source | Container Image |
| Optimize for Azure Functions | No |

| Setting                 | Value                                    |
| ----------------------- | ---------------------------------------- |
| Environment             | Auto-created by Azure                    |
| Name                    | `managedEnvironment-rgproductapidev-...` |
| Log Analytics Workspace | Auto-created by Azure                    |
| Workspace Name          | `workspacergproductapidev...`            |

| Setting      | Value                          |
| ------------ | ------------------------------ |
| Image Source | Docker Hub or other registries |
| Registry     | `ghcr.io`                      |
| Image        | `annamalai2k11/product-api`    |
| Tag          | `latest`                       |

| Setting           | Value       |
| ----------------- | ----------- |
| Development Stack | Unspecified |
| Workload Profile  | Consumption |
| CPU               | 0.5         |
| Memory            | 1 Gi        |
| GPU               | Disabled    |

| Setting                    | Value                        |
| -------------------------- | ---------------------------- |
| Ingress                    | Enabled                      |
| Ingress Traffic            | Accept traffic from anywhere |
| Ingress Type               | HTTP                         |
| Transport                  | HTTP/1                       |
| Target Port                | 8000                         |
| Allow Insecure Connections | No                           |
| Session Affinity           | None                         |

App Registration / Service Principal

1. Open App registrations: Azure Portal → Microsoft Entra ID → App registrations → New registration
   Give name: github-product-api

2. Copy the important IDs
   After creating we will get Application (client) ID

   Goto Microsoft Entra ID → Overview
   Tenant ID

   Azure Portal → Subscriptions → your subscription
   Subscription ID

   Now we have: CLIENT_ID, TENANT_ID, SUBSCRIPTION_ID

3. Create a client secret
   Microsoft Entra ID → App registrations → github-product-api → Certificates & secrets

   Click New client secret
   Give below details:
   Description: GitHub Actions
   Expires: 6 months / 12 months

   Now we will get: Value and Secret ID, copy the Value

   We have CLIENT_ID,CLIENT_SECRET,TENANT_ID,SUBSCRIPTION_ID

4. Give GitHub Actions access to your Resource Group
   Azure Portal → Resource groups → your resource group -> Access control (IAM)
   Add → Add role assignment -> Contributor -> Next
   Assign access to: User, group, or service principal
   Click Select members -> Search for github-product-api
   Review + assign

5. Create the GitHub secret
   GitHub → Your repository → Settings → Secrets and variables → Actions -> Repository Secrets -> New Repository Secrets
   AZURE_CREDENTIALS
   {
   "clientId": "YOUR_APPLICATION_CLIENT_ID",
   "clientSecret": "YOUR_CLIENT_SECRET_VALUE",
   "subscriptionId": "YOUR_AZURE_SUBSCRIPTION_ID",
   "tenantId": "YOUR_AZURE_TENANT_ID"
   }
   AZURE_CONTAINER_APP_NAME: Azure Portal → Container Apps → your Product API app → Overview
   AZURE_RESOURCE_GROUP : RG NAme
