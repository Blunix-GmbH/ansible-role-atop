# Atop Ansible Role (ansible-role-atop) from Blunix GmbH

This Ansible role installs and configures the `atop` performance monitoring tool on Debian systems, matching how we deploy it in production baselines.

The Ansible Role is written and actively maintained by <a href="https://www.blunix.com" target="_blank">Blunix GmbH</a>.
It is used in the Blunix <a href="https://www.blunix.com/linux-managed-hosting.html" target="_blank">Linux Managed Hosting</a> Stack.
Its usage is documented at our <a href="https://www.blunix.com/manual" target="_blank">Linux Managed Hosting Documentation</a>.


## Features

- Installs the `atop` package on Debian.
- Manages `/etc/default/atop` via a template to control logging behaviour.
- Configures log directory, log retention and sampling interval via role variables.


## Requirements

- Ansible: **>= 2.20.0**
- Managed operating systems:
  - Debian **trixie**



## Role variables, inventory and example playbook

Production playbooks include the role without overrides. The example is split into files under `example/`:

- <a href="https://github.com/Blunix-GmbH/ansible-role-atop/blob/main/example/inventory/group_vars/all/atop.yml" target="_blank">`example/inventory/group_vars/all/atop.yml`</a> — sampling interval, log retention, and log dir.
- <a href="https://github.com/Blunix-GmbH/ansible-role-atop/blob/main/example/play.yml" target="_blank">`example/play.yml`</a> — minimal play applying the role to all hosts.


## Managed files and templates

- <a href="https://github.com/Blunix-GmbH/ansible-role-atop/blob/main/templates/etc/default/atop.j2" target="_blank"><code>/etc/default/atop</code></a> (controls interval, log dir, log file name)


### Tests

### Infrastructure As Code Tests

- Provision: use <a href="https://github.com/Blunix-GmbH/ansible-roles/blob/main/dev-tools/main.tf" target="_blank"><code>dev-tools/main.tf</code></a> with the atop role enabled to create a test host.
- Playbook: <a href="https://github.com/Blunix-GmbH/ansible-role-atop/blob/main/example/play.yml" target="_blank"><code>example/play.yml</code></a> applies the role and configures atop/log rotation defaults.
- Tests in `example/tests/`:
  - <a href="https://github.com/Blunix-GmbH/ansible-role-atop/blob/main/example/tests/cus-dev-prod-web-1/test_default.py" target="_blank"><code>cus-dev-prod-web-1/test_default.py</code></a>: checks atop is installed, service is active, and basic defaults are in place.

## Author Information

Blunix GmbH Berlin  

`root@Linux:~# Support | Consulting | Hosting | Training`

Blunix GmbH provides 24/7/365 Linux emergency support and consulting, Service Level Agreements for Debian Linux managed hosting using Ansible Configuration Management as well as Linux trainings and workshops.

Learn more at <a href="https://www.blunix.com" target="_blank">https://www.blunix.com</a>.

## Contact Information

Click here to see our <a href="https://www.blunix.com/#contact" target="_blank">Contact Information</a>.

For bug reports and feature requests, please open an issue in this repository’s GitHub issue tracker.


## License

Apache-2.0

Please refer to the `LICENSE` file in the root of this repository.
