import os
import testinfra.utils.ansible_runner

inventory = os.environ.get("MOLECULE_INVENTORY_FILE", "example/inventory/hosts")
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(inventory).get_hosts(
    "all"
)


def test_service_running_and_enabled(host):
    svc = host.service("atop")
    assert svc.is_enabled
    assert svc.is_running


def test_service_restart_after_config(host):
    config = host.file("/etc/default/atop")
    svc = host.service("atop")
    assert config.exists
    assert svc.is_running
    # Sanity: service is running and the managed config is present
    assert config.size > 0
