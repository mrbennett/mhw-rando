resource "azurerm_resource_group" "mhwrando" {
  name     = "mhwrando"
  location = "West Europe"
}

resource "azurerm_app_service_plan" "mhwrando" {
  name                = "mhwrando-appserviceplan"
  location            = azurerm_resource_group.mhwrando.location
  resource_group_name = azurerm_resource_group.mhwrando.name

  sku {
    tier = "Free"
    size = "F1"
  }
}

resource "azurerm_app_service" "mhwrando" {
  name                = "mhwrando-app-service"
  location            = azurerm_resource_group.mhwrando.location
  resource_group_name = azurerm_resource_group.mhwrando.name
  app_service_plan_id = azurerm_app_service_plan.mhwrando.id

  site_config {
    python_version = "3.4"
    scm_type       = "None"
  }
}