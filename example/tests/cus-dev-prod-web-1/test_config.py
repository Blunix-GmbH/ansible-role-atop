import os

import testinfra.utils.ansible_runner

inventory = os.environ.get("MOLECULE_INVENTORY_FILE", "example/inventory/hosts")
testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(inventory).get_hosts(
    "all"
)


def test_atop_config_file(host):
    vars = host.ansible.get_variables()
    interval = vars.get("atop_log_interval")
    log_dir = vars.get("atop_log_dir")

    cfg = host.file("/etc/default/atop")
    assert cfg.exists
    assert cfg.user == "root"
    assert cfg.group == "root"
    assert cfg.mode == 0o640

    content = cfg.content_string
    assert f'INTERVAL="{interval}"' in content
    assert f'LOGPATH="{log_dir}"' in content
    assert f'OUTFILE="$LOGPATH/daily.log"' in content


def test_log_directory(host):
    vars = host.ansible.get_variables()
    log_dir = vars.get("atop_log_dir")
    log = host.file(log_dir)
    assert log.exists
    assert log.is_directory
    assert log.user == "root"
    assert log.group == "root"
