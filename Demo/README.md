## Azure ML Functions Example

1. Generate model:
```
pyhon abs.py
```

2. Install Azure ML Cli and Preview Extension:
TODO insert.
```
```

3. Create workspace and set as default
```
az ml workspace create -w <NAME> -g <RG>
```

Note the name of the container registry (in containerRegistry, after registries). This will be used later for logging in.

3. Register Model:
```
az ml model register -n abs -p saved_model -t registered_model.json -w <NAME> -g <RG>
```

4. Package for Functions:
```
az ml model package-functions -f registered_model.json --pof package-options.json --ic inference-config.json -w <Name> -g <RG>
```
The output of that command will include the location of your functions image.

5. Get storage accounts for functions deployment.
```
az storage account create --name {fnStorage} --sku Standard_LRS
export storageConnectionString=`az storage account show-connection-string --name {fnStorage} --query connectionString --output tsv`
```


6. Get credentials for functions:
The ACR name is was either gotten at the time of creation, or is the part prior to azurecr.io in the package location.
```
az acr credential show -n <ACR NAME>
```

7. Create functionapp:
```
az functionapp create --name $app_name --storage-account coverstediag --plan coverste --deployment-container-image-name <image_name>
```

8. Configure functionapp:
```
az functionapp config appsettings set --name $app_name --settings DOCKER_REGISTRY_SERVER_USERNAME=$dockername DOCKER_REGISTRY_SERVER_PASSWORD=$dockerpwd 
```