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
