output "resource_group_name" {
  value = azurerm_resource_group.region.name
}

output "container_registry_name" {
  value = azurerm_container_registry.our_future_health.name
}

output "container_registry_login_server" {
  value = azurerm_container_registry.our_future_health.login_server
}