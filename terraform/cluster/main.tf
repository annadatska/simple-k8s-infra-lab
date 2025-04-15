provider "kubernetes" {
  config_path = "~/.kube/config"
}

resource "null_resource" "create_kind_cluster" {
  provisioner "local-exec" {
    command = "kind create cluster --name demo-cluster"
  }
}
