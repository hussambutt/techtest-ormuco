# techtest

Both the ansible playbook and the app are part of this repository.

The user needs to export his AWS keys from where the playbook will be run if he needs to run the playbook on his AWS
environment plus have his key pair already available on AWS. I also assume that the user has a hosted zone on AWS.

The playbook will bring up a t2.micro instance on AWS and deploy the django application on it.

Currently in the ec2.yml and under env_var/base.yml there are variables at the start of the file which should be changed
to match the users's preference.

Min changes required to run:

Under playbooks/ec2.yml:
      keypair: # Keypair name
      zone: # Zone name
      record: # Record name under zone

Under env_vars/base.yml:
    cert_bot_hostname: # something.com

The following from inside the repo will bring up and instance with the app:

cd test-ansibleaws
ansible-playbook -i inventory/hosts playbooks/ec2.yml

The app once deployed can be reached on the url specified as the variable "record" under the ec2.yml file. The variable
cert_bot_hostname under env_var/base.yml would also need to be changed to allow for the correct ssl certs to be
generated as well.

The creation of the ec2 instance is NOT idempotent and will result in a new instance created every time the playbook is
run. If you just want to run the roles only for the webserver you can execute the following command:

ansible-playbook -i inventory/hosts -l webserver  playbooks/ec2.yml

The site brought up by me using this repo is:

[test.hussambutt.com
]()
