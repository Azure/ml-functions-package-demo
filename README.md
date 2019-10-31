# Package Azure Machine Learning Models for 

<!-- 
Guidelines on README format: https://review.docs.microsoft.com/help/onboard/admin/samples/concepts/readme-template?branch=master

Guidance on onboarding samples to docs.microsoft.com/samples: https://review.docs.microsoft.com/help/onboard/admin/samples/process/onboarding?branch=master

Taxonomies for products and languages: https://review.docs.microsoft.com/new-hope/information-architecture/metadata/taxonomies?branch=master
-->

Give a short description for your sample here. What does it do and why is it important?

## Contents

Outline the file contents of the repository. It helps users navigate the codebase, build configuration and any related assets.

| File/folder       | Description                                |
|-------------------|--------------------------------------------|
| `Demo`            | Sample demo from ignite.                        |
| `azure_cli_ml_preview-1.0.72-py2.py3-none-any.whl` | wheel file containg preview CLI |
| `.gitignore`      | Define what to ignore at commit time.      |
| `CHANGELOG.md`    | List of changes to the sample.             |
| `CONTRIBUTING.md` | Guidelines for contributing to the sample. |
| `README.md`       | This README file.                          |
| `LICENSE`         | The license for the sample.                |

## Prerequisites

Python, Azure CLI, Azure ML CLI Extension

## Setup

Add the preview CLI to your Azure CLI

```
az extension add --source azure_cli_ml_preview-1.0.72-py2.py3-none-any.whl
```

You can also use the URL of the 'raw' CLI in github to install it.

## Runnning the sample

See Demo/readme.md

## Key concepts

As a preview, you can now package Azure ML Models for use with Azure functions. 
You can either use `azureml-contrib-functions` from PyPi, or the CLI preview features included in this repo.

### Package Options File
When you package your model, you can package it for functions by providing a 'Package Options File', which is a JSON file that tells Azure ML how to packge your model.

#### Example for HTTP
```
{
    {"flavor": "functionsApp", 
    "trigger": "Http", 
    "authLevel": "anonymous"}
}
```
Auth level is as described in the [Azure Functions Documentation](https://docs.microsoft.com/azure/azure-functions/functions-bindings-http-webhook?tabs=csharp#trigger---configuration)

Auth level is an optional parameter which defaults to function.

#### Example for Blob
```
{   "flavor": "functionsApp", 
    "trigger": "Blob", 
    "inPath": "input/{blobname}.{blobextension}",
    "outPath": "output/{blobname}.out"}
```
Input path and output path are as described in documentation [here](https://docs.microsoft.com/azure/azure-functions/functions-bindings-storage-blob?tabs=csharp#trigger---blob-name-patterns)

They are optional parameters which default to the above values.

Make sure to see [Connection Strings](#Connection-Strings) for configuring your storage account.

#### Example for Service Bus Queue
```
"flavor": "functionsApp", 
    "trigger": "ServiceBusQueue", 
    "inQueueName": "inqueue",
    "outQueueName": "outqueue"}
```
They are optional parameters which default to the above values.

Make sure to see [Connection Strings](#Connection-Strings) for configuring your Service Bus account.


### Connection Strings

Blob and Service Bus Queues require a connection string to know which storage account or Service bus to connect to.

You should pass these connections strings as the aplication setting `TriggerConnectionString` when you deploy  or if you choose to write the docker context to your local disk, you could add it as an environment variable in the dockerfile with the same name.  

[More info on application settings](https://docs.microsoft.com/azure/azure-functions/functions-how-to-use-azure-function-app-settings).

## Feedback

This capability is in public preview and needs your feedback. If you face challenges or are interested in additional triggers, please open an issue in this repo.

## Contributing

This project welcomes contributions and suggestions.  Most contributions require you to agree to a
Contributor License Agreement (CLA) declaring that you have the right to, and actually do, grant us
the rights to use your contribution. For details, visit https://cla.opensource.microsoft.com.

When you submit a pull request, a CLA bot will automatically determine whether you need to provide
a CLA and decorate the PR appropriately (e.g., status check, comment). Simply follow the instructions
provided by the bot. You will only need to do this once across all repos using our CLA.

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/).
For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or
contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
