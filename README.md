# Container MLOps Template repository

Learn how to create a container and package it with GitHub Actions. This repository template gives you a good starting point for a Dockerfile, GitHub Actions workflow, and Python code.

Depending on the type of model you need, you will need different workflow steps and most definitely a different `main.py` file. The default uses FastApi

# Learn objectives

*
*
*
*
*

## Deploy your API to the Azure Cloud

This deployment can be done at no cost, using free resources with an Azure subscription. Use one of these to deploy this:

- [Sign in to your account]()
- [Create a (no Credit Card required) Azure For Students account]()
- [Create a new Azure account]()


## Create an Azure App Service

1. Open an [Azure Cloud Shell](https://shell.azure.com/?WT.mc_id=academic-0000-alfredodeza) to use the `az` cli
1. Create a *Resource Group*:
```
az group create --name demo-huggingface --location "East US"
```
1. Create the **FREE** App Service Plan:
```
az appservice plan create --name "demo-huggingface" --resource-group demo-huggingface --is-linux --sku FREE
```
1. Create the web app with a placeholder container
```
az webapp create --name "demo-huggingface" --resource-group demo-huggingface --plan demo-huggingface --deployment-container-image mcr.microsoft.com/appsvc/staticsite:latest
```
1. Head to the [App Service](https://portal.azure.com/#view/HubsExtension/BrowseResource/resourceType/Microsoft.Web%2Fsites)
