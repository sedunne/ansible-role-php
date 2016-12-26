# Ansible Role: Nexcess SCL PHP

Installs Necxess' SCL PHP Version(s).  Note that this only installs the CLI version of PHP.

## Requirements

- https://github.com/nexcess/ansible-role-repo-nexcess-scl

## Role Variables

See `defaults/main.yml`.

## Dependencies

None.

## Add to Requirements

    - src: https://github.com/nexcess/ansible-role-php.git
      name: nexcess.php

## Example Playbook

    - hosts: php_hosts
      roles:
        - nexcess.php

## License

MIT / BSD
