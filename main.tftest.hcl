# valid_string_concat.tftest.hcl

run "region_validation_resource_group" {

  command = plan

  assert {
    condition     = azurerm_resource_group.region.location == "eastus"
    error_message = "Location does not match to eastus"
  }

}

run "test_Public_registry_access_Docker" {

    command = plan

    assert {
        condition     = strcontains(azurerm_container_registry_cache_rule.defaultImage.source_repo, "docker.io")

        error_message = "only docker.io is permissive public registry access permistted"
    }
}

run "test_Public_registry_access_Github" {

    command = plan

    assert {
        condition     = !strcontains(azurerm_container_registry_cache_rule.defaultImage.source_repo, "ghcr.io")

        error_message = "only docker.io is permissive public registry access permistted"
    }
}

run "test_Public_registry_access_quay" {

    command = plan

    assert {
        condition     = !strcontains(azurerm_container_registry_cache_rule.defaultImage.source_repo, "quay.io")

        error_message = "only docker.io is permissive public registry access permistted"
    }
}