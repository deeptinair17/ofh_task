
resource "azurerm_resource_group" "region" {
  location = var.resource_group_location
  name     = "Our_Future_Health_Resource_group"
}

resource "azurerm_container_registry" "our_future_health" {
  name                = "OurFutureHealthContainerRegistry"
  resource_group_name = azurerm_resource_group.region.name
  location            = azurerm_resource_group.region.location
  sku                 = "Standard"
}

resource "azurerm_container_registry_cache_rule" "defaultImage" {
  name                  = "defaultImage"
  container_registry_id = azurerm_container_registry.our_future_health.id
  target_repo           = "target2"
  source_repo           = "docker.io/ubuntu"
  credential_set_id     = "${azurerm_container_registry.our_future_health.id}/credentialSets/DockerCredentialsSet"
}