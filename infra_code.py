from azure.identity import DefaultAzureCredential
from azure.mgmt.containerregistry import ContainerRegistryManagementClient

subscription_id = "417670b6-8f2d-425a-b28c-df0470dd3b6a"
resource_group_name = "Our_Future_Health_Resource_group"
registry_name = "OurFutureHealthContainerRegistry"

def get_count_of_cache_container_images():
    credential = DefaultAzureCredential()
    client = ContainerRegistryManagementClient(credential, subscription_id)
    cache_rules = client.cache_rules.list(resource_group_name, registry_name)
    print(f"Cache rules '{registry_name}':")
    container_image_names = []
    for rule in cache_rules:
        print(f"{rule.source_repository}")
        container_image_names.append(rule.source_repository)
    return container_image_names