# Configure Service-Account
## AWS IAM (Groups, Users, Roles, Policies) + AWS S3

Although scripting is great, scripting everything is not advisable if you do not have a full understanding of what is getting scripted. If this is the case, troubleshooting issues will be pointless sicne you wouldn't understand how things works. My advise, please do not hide the behavior and logic of a process for the sake of efficiency.

I have always focused in supporting one key factor in automation:
### [Readability](https://en.wikipedia.org/wiki/Computer_programming#Readability_of_source_code)

---

Take the time to review this documents:

[Endpoints available for GitHub Apps](https://docs.github.com/en/rest/overview/endpoints-available-for-github-apps)

<a href="https://docs.github.com/en/rest/reference/actions#list-repository-secrets">List repository secrets</a><br>
<a href="https://docs.github.com/en/rest/reference/actions#get-a-repository-public-key">Get a repository public key</a><br>
<a href="https://docs.github.com/en/rest/reference/actions#get-a-repository-secret">Get a repository secret</a><br>
<a href="https://docs.github.com/en/rest/reference/actions#create-or-update-a-repository-secret">Create or update a repository secret</a><br>
<a href="https://docs.github.com/en/rest/reference/actions#delete-a-repository-secret">Delete a repository secret</a>

---

#### These are the steps you need to follow: <br>

**<span style="color:red">A</span>** -) Create your own GitHub Repository and include this GitHub Action - Pipeline into your own GitHub Repository. <br>
e.g.: [Deploy-Terraform](https://github.com/emvaldes/terraform-awscloud/blob/master/.github/workflows/terraform-awscloud.yaml)

Be aware that this single GitHub Action-Pipeline uses several other GitHub Actions.

[emvaldes/system-requirements@master](https://github.com/emvaldes/system-requirements/blob/master/action.yaml)<br>
[emvaldes/generate-credentials@master](https://github.com/emvaldes/generate-credentials/blob/master/action.yaml)<br>
[emvaldes/configure-access@master](https://github.com/emvaldes/configure-access/blob/master/action.yaml)<br>
[emvaldes/terraform-controller@master](https://github.com/emvaldes/terraform-controller/blob/master/action.yaml)<br>
[emvaldes/monitor-loadbalancer@master](https://github.com/emvaldes/monitor-loadbalancer/blob/master/action.yaml)<br>

---

**<span style="color:red">B</span>** -) Create a [GitHub Personal Token](https://github.com/settings/tokens):<br>
https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token <br>

**<span style="color:red">C</span>** -) Then create two environment variables to enable the interaction with the GitHub REST API to manage secrets: <br>

```shell
export github_personal_token="***";
export github_restapi_application="application/vnd.github.v3+json";
```

**Note**: The GitHub Personal Token will not be visible from within the deployment script so it must be passed as a parameter.

```shell
...
github_personal_token="${1}";
if [[ ${#github_personal_token} == '' ]]; then
  echo -e; read -p "GitHub Personal Token: " response;
  if [[ ${#response} -eq 0 ]]; then
          echo -e "\nWarning: Invalid GitHub Personal Token! \n";
          exit 1;
    else  export github_personal_token=${response};
  fi;
fi;
...
```

**<span style="color:red">D</span>** -) Execute these steps to setup your environment.

```shell
wget --quiet --output-document=\${HOME}/bin/manage-profiles.shell ${github_usercontent}/devops-tools/master/manage-profiles.shell
chmod 0754 \${HOME}/bin/manage-profiles.shell
```

**<span style="color:red">E</span>** -) Please, follow these instructions after:

```shell
mkdir -p ${HOME}/bin ;

export PATH="${PATH}:${HOME}/bin" ;
export github_secrets="github-secrets.py" ;

wget --quiet --output-document="${HOME}/bin/github-secrets.py" \
     https://raw.githubusercontent.com/emvaldes/manage-profiles/master/github-secrets.py ;
chmod 0754 \${HOME}/bin/github-secrets.py ;
ls -al ${HOME}/bin/github-secrets.py ;

alias python='python3' ;
python --version ;
pip --version ;

pip install virtualenv ;
```

```console
# DEPRECATION: Python 2.7 reached the end of its life on January 1st, 2020. Please upgrade your Python as Python 2.7 is no longer maintained. A future version of pip will drop support for Python 2.7. More details about Python 2 support in pip, can be found at https://pip.pypa.io/en/latest/development/release-process/#python-2-support
# Defaulting to user installation because normal site-packages is not writeable
# Collecting virtualenv
#   Downloading virtualenv-20.0.31-py2.py3-none-any.whl (4.9 MB)
#      |████████████████████████████████| 4.9 MB 3.2 MB/s
# Requirement already satisfied: importlib-metadata<2,>=0.12; python_version < "3.8" in /Library/Python/2.7/site-packages (from virtualenv) (1.7.0)
# Requirement already satisfied: importlib-resources>=1.0; python_version < "3.7" in /Library/Python/2.7/site-packages (from virtualenv) (3.0.0)
# Requirement already satisfied: distlib<1,>=0.3.1 in /Library/Python/2.7/site-packages (from virtualenv) (0.3.1)
# Requirement already satisfied: filelock<4,>=3.0.0 in /Library/Python/2.7/site-packages (from virtualenv) (3.0.12)
# Requirement already satisfied: appdirs<2,>=1.4.3 in /Library/Python/2.7/site-packages (from virtualenv) (1.4.4)
# Requirement already satisfied: pathlib2<3,>=2.3.3; python_version < "3.4" and sys_platform != "win32" in /Library/Python/2.7/site-packages (from virtualenv) (2.3.5)
# Requirement already satisfied: six<2,>=1.9.0 in /System/Library/Frameworks/Python.framework/Versions/2.7/Extras/lib/python (from virtualenv) (1.12.0)
# Requirement already satisfied: configparser>=3.5; python_version < "3" in /Library/Python/2.7/site-packages (from importlib-metadata<2,>=0.12; python_version < "3.8"->virtualenv) (4.0.2)
# Requirement already satisfied: zipp>=0.5 in /Library/Python/2.7/site-packages (from importlib-metadata<2,>=0.12; python_version < "3.8"->virtualenv) (1.2.0)
# Requirement already satisfied: contextlib2; python_version < "3" in /Library/Python/2.7/site-packages (from importlib-metadata<2,>=0.12; python_version < "3.8"->virtualenv) (0.6.0.post1)
# Requirement already satisfied: typing; python_version < "3.5" in /Library/Python/2.7/site-packages (from importlib-resources>=1.0; python_version < "3.7"->virtualenv) (3.7.4.3)
# Requirement already satisfied: singledispatch; python_version < "3.4" in /Library/Python/2.7/site-packages (from importlib-resources>=1.0; python_version < "3.7"->virtualenv) (3.4.0.3)
# Requirement already satisfied: scandir; python_version < "3.5" in /Library/Python/2.7/site-packages (from pathlib2<3,>=2.3.3; python_version < "3.4" and sys_platform != "win32"->virtualenv) (1.10.0)
# Installing collected packages: virtualenv
#   WARNING: The script virtualenv is installed in '/Users/emvaldes/Library/Python/2.7/bin' which is not on PATH.
#   Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
# Successfully installed virtualenv-20.0.31
```

**<span style="color:red">F</span>** -) Include the Python 2.7 bin-folder into then PATH:

```shell
export PATH="${PATH}:${HOME}/Library/Python/2.7/bin" ;

mkdir -p /tmp/.virtualenv ;
virtualenv /tmp/.virtualenv/python3 ;
```

```console
# created virtual environment CPython2.7.16.final.0-64 in 392ms
#   creator CPython2macOsFramework(dest=/Users/emvaldes/.virtualenv/python3, clear=False, global=False)
#   seeder FromAppData(download=False, pip=bundle, wheel=bundle, setuptools=bundle, via=copy, app_data_dir=/Users/emvaldes/Library/Application Support/virtualenv)
#     added seed packages: pip==20.2.2, setuptools==44.1.1, wheel==0.35.1
#   activators PythonActivator,CShellActivator,FishActivator,PowerShellActivator,BashActivator
```

**<span style="color:red">G</span>** -) Activated the Python VirtualEnv.

```shell
source /tmp/.virtualenv/python3/bin/activate ;
```

**<span style="color:red">H</span>** -) Installing PyNacl in Python VirtualEnv:

```console
# (python3) emvaldes-macbookpro:python3 emvaldes$ python -m pip install pynacl ;
# Requirement already satisfied: pynacl in /Library/Frameworks/Python.framework/Versions/3.8/lib/python3.8/site-packages (1.4.0)
# Requirement already satisfied: cffi>=1.4.1 in /Users/emvaldes/Library/Python/3.8/lib/python/site-packages (from pynacl) (1.13.2)
# Requirement already satisfied: six in /Users/emvaldes/Library/Python/3.8/lib/python/site-packages (from pynacl) (1.14.0)
# Requirement already satisfied: pycparser in /Users/emvaldes/Library/Python/3.8/lib/python/site-packages (from cffi>=1.4.1->pynacl) (2.19)
```

**<span style="color:red">I</span>** -) Installing PyNacl in your Operating System: <br>
**Note**: Encrypt your secret using [pynacl](https://pynacl.readthedocs.io/en/stable/public/#nacl-public-sealedbox) with Python 3.

```shell
python -m pip install pynacl ;

Collecting pynacl
  Downloading PyNaCl-1.4.0-cp35-abi3-macosx_10_10_x86_64.whl (380 kB)
     |████████████████████████████████| 380 kB 1.1 MB/s
Requirement already satisfied: six in /Users/emvaldes/Library/Python/3.8/lib/python/site-packages (from pynacl) (1.14.0)
Requirement already satisfied: cffi>=1.4.1 in /Users/emvaldes/Library/Python/3.8/lib/python/site-packages (from pynacl) (1.13.2)
Requirement already satisfied: pycparser in /Users/emvaldes/Library/Python/3.8/lib/python/site-packages (from cffi>=1.4.1->pynacl) (2.19)
Installing collected packages: pynacl
Successfully installed pynacl-1.4.0

WARNING: You are using pip version 20.0.2; however, version 20.2.2 is available.
You should consider upgrading via the '/Library/Frameworks/Python.framework/Versions/3.8/bin/python -m pip install --upgrade pip' command.
python -m pip install --upgrade pip ;
Collecting pip
  Downloading pip-20.2.2-py2.py3-none-any.whl (1.5 MB)
     |████████████████████████████████| 1.5 MB 1.2 MB/s
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 20.0.2
    Uninstalling pip-20.0.2:
      Successfully uninstalled pip-20.0.2
Successfully installed pip-20.2.2
```

**<span style="color:red">J</span>** -) Confirm that Python 3.x and Python PyNacl are setup.

```shell
python --version ;
python -m pip install pynacl ;
...
```

**<span style="color:red">K</span>** -) This script block will pull down all the devops-modules that are used by this deploymentand get them sourced ini the environment so you do not need to install anything.

```shell
...
export devops_tools='emvaldes/devops-tools';

declare -a functions=(
    devops-assumerole
    devops-awscli
    devops-tools
  );

container="/tmp/import--$(LC_CTYPE=C tr -dc 'a-zA-Z0-9' < /dev/urandom | head -c32)";
mkdir -p ${container};

source_tools="https://raw.githubusercontent.com/${devops_tools}/master";
echo -e;
for xfile in ${functions[@]}; do
  random_index="$(LC_CTYPE=C tr -dc 'a-zA-Z0-9' < /dev/urandom | head -c32)";
  for xitem in functions variables; do
    master_file="${source_tools}/${xitem}/${xfile}.${xitem}";
    source_file="${container}/source--${random_index}.${xitem}";
    wget --quiet --output-document=${source_file} ${master_file};
    echo -e "Source: ${source_file}";
    source ${source_file};
  done;
done;
rm -rf ${container};
...
```

**<span style="color:red">L</span>** -) These are the basic/core set of variables that are needed for the script to work. <br>
**Note**: Make sure you modify or make available the access-keys files.

```shell
...
## AWS IAM admin-level account and company name-id
export master_user='masteruser';
export company_name='anonymous';

## AWS IAM Group/User credentials-set
export group_name='devops';
export user_name='devops';

## Target GitHub Account/Repository
export github_user='emvaldes';
export github_repo='manage-profiles';

## SSH Access (Private & Public Keys)
export private_sshkey=${HOME}/.ssh/domains/${company_name}/private/${company_name} ;
export public_sshkey=${HOME}/.ssh/domains/${company_name}/public/${company_name}.pub ;

## These are the AWS IAM Roles/Policies
export access_policy='DevOps--Custom-Access.Policy';
export access_role='DevOps--Custom-Access.Role';
export assume_policy='DevOps--Assume-Role.Policy';
export custom_boundary='Devops--Permission-Boundaries.Policy';

export DEVOPS_ACCESS_ROLE='DevOps--Custom-Access.Role';

## Basic (skeleton) Shell-command to execute:
configure_account --master-user=${master_user} \
                  --account-name=${user_name} \
                  --company-name=${company_name} \
                  --github-user=${github_user} \
                  --github-repo=${github_repo} \
                  --create-secrets=true \
                  --deploy-keypair=true \
                  --private-sshkey=${private_sshkey} \
                  --public-sshkey=${public_sshkey} \
;
...
```

**<span style="color:red">M</span>** -) Exporting ***${github_public_key}***, ***${github_public_key_id}*** <br>
[Fetching GitHub Public Encryption Key](https://github.com/emvaldes/devops-tools/blob/7800086abac75e6c558140e789d73249ceb90e02/functions/devops-assumerole.functions#L68)

```shell
...
if [[ ${create_secrets} == true ]]; then
  ## Then create two environment variables to enable the interaction with the GitHub REST API to manage secrets:
  export github_restapi_application="application/vnd.github.v3+json";
  ## Exporting ${github_public_key}, ${github_public_key_id}
  if [[ ${#github_personal_token} -eq 0 ]]; then
          echo -e "\nWarning: GitHub Personal Token is null! \n";
          return 1;
    else  echo -e "\nGitHub Personal Token is: ${github_personal_token}";
  fi;
  target_location="https://api.github.com/repos/${github_user}/${github_repo}/actions/secrets/public-key";
  message="$(
      curl --location \
           --silent \
           --header "Authorization: token ${github_personal_token}" \
           --header "Accept: ${github_restapi_application}" \
      ${target_location}
    )";
  if [[ $(echo -e ${message} | jq '.message' --raw-output) =~ 'Must have admin' ]]; then
    echo -e "\nWarning: ${message}! \n";
    return 2;
  fi;
  ## {
  ##   "message": "Moved Permanently",
  ##   "url": "https://api.github.com/repositories/***/actions/secrets/public-key",
  ##   "documentation_url": "https://docs.github.com/v3/#http-redirects"
  ## }
  custom_message="$(echo -e ${message} | jq '.message' --raw-output)";
  if [[ ${custom_message} =~ 'Moved Permanently' ]]; then
    target_location="$(echo -e ${message} | jq '.url' --raw-output)";
    echo -e "\nWarning: Secrets Public-Key Location is invalid ['${custom_message}'] ! ";
  fi;
  eval $(
      curl --location \
           --silent \
           --header "Authorization: token ${github_personal_token}" \
           --header "Accept: ${github_restapi_application}" \
      ${target_location} \
      | jq -r "to_entries|map(\"export github_public_\(.key)=\(.value|tostring)\")|.[]"
    ) ;
  ## Fetched: {"key_id":"?","key": "?"} -> github_public_key, github_public_key_id
  echo -e "\nExported: ['${github_public_key}'] & ['${github_public_key_id}'] ...\n";
...
```

**<span style="color:red">N</span>** -) This Python function is the only portion of this automation that does not work. So the encrypted content is properly submitted but it's not accepted. As a result to that, the secrets are empty.<br>
[GitHub Secrets Script (Python)](https://github.com/emvaldes/terraform-awscloud/blob/24f588c7bbd3b75c9f2a914f03c3bdcb073d3308/scripts/github-secrets.py#L1)

**Note**: This python script must be stored and executed within a Python3 VirtualEnv for multiple-platforms support.

```python
#!/usr/local/bin/python3

import sys, argparse, json

from base64 import b64encode
from nacl import encoding, public

def encrypt( encrypt_key: str, secret_value: str ) -> str:
    #private_key = public.PrivateKey.generate()
    public_key = public.PublicKey( encrypt_key.encode( "utf-8" ), encoding.Base64Encoder() )
    sealed_box = public.SealedBox( public_key )
    encrypted = sealed_box.encrypt( secret_value.encode( "utf-8" ) )
    ### print(encrypted)
    return b64encode( encrypted ).decode( "utf-8" )

def main():
    ## print ( 'Total Arguments?:', format( len( sys.argv ) ) )
    ## print ( '   Argument List:', str( sys.argv ) )
    parser = argparse.ArgumentParser()
    parser.add_argument( '--public-key', dest='public_key',  type=str, help='Encryption Public-Key' )
    parser.add_argument( '--content', dest='content',  type=str, help='Source Content' )
    options = parser.parse_args()
    ## print( json.dumps( { "encrypted_value" : encrypt( options.public_key, options.content ), "key_id" : encrypt_key } ) )
    print( encrypt( options.public_key, options.content ) )

if __name__ == '__main__':
    main()
```

**<span style="color:red">O</span>** -)  Define a function for creating the GitHub Secrets:<br>
[Create GitHub Secret (REST API)](https://github.com/emvaldes/devops-tools/blob/7800086abac75e6c558140e789d73249ceb90e02/functions/devops-tools.functions#L139)

```shell
function create_github_secret () {
    ## tracking_process ${FUNCNAME} "${@}";
    oIFS="${IFS}";
    for xitem in "${@}"; do
      IFS='='; set `echo -e "${xitem}" | sed -e '1s|^\(-\)\{1,\}||'`
      [[ ${1#*\--} = "github-repo" ]] && export github_repo="${2}";
      [[ ${1#*\--} = "github-token" ]] && export github_token="${2}";
      [[ ${1#*\--} = "github-user" ]] && export github_user="${2}";
      [[ ${1#*\--} = "secret-name" ]] && export secret_name="${2}";
      [[ ${1#*\--} = "secret-value" ]] && export secret_value="${2}";
      [[ ${1#*\--} = "interactive" ]] && export interactive_mode='true';
      ## [[ ${1#*\--} = "dry-run" ]] && export dry_run="${2}";
      [[ ${1#*\--} = "verbose" ]] && export verbose='true';
      [[ ${1#*\--} = "help" ]] && export display_help='true';
    done; IFS="${oIFS}";
    export github_restapi="application/vnd.github.v3+json";
    eval $(
        curl --silent \
             --header "Authorization: token ${github_token}" \
             --header "Accept: ${github_restapi}" \
             https://api.github.com/repos/${github_user}/${github_repo}/actions/secrets/public-key \
        | jq -r "to_entries|map(\"export github_public_\(.key)=\(.value|tostring)\")|.[]") ;
    if [[ ${#github_public_key} -gt 0 ]]; then
            [[ ${verbose} == true ]] && echo -e "\nGitHub Public-Key:   ${github_public_key}";
      else  echo -e "\nWarning: Unable to fetch GitHub Public Encryption-Key! \n";
            return 1;
    fi;
    encrypted=$(
        github-secrets.py --public-key ${github_public_key} \
                          --content "${secret_value}"
      );
    if [[ ${verbose} == true ]]; then
      echo -e;
      echo -e "DevOps GitHub User:  ${github_user}";
      echo -e "DevOps GitHub Repo:  ${github_repo}";
      echo -e "GitHub Repos Token:  ${github_token}";
      echo -e "GitHub RESTAPI App:  ${github_restapi}";
      echo -e "GitHub Public Key:   ${github_public_key}";
      echo -e "GitHub Secret Name:  ${secret_name}";
      echo -e "GitHub Secret Value: ${secret_value}";
      echo -e "GitHub Secret (encrypted): ${encrypted}";
      echo -e "\nCreating GitHub Secret: ...";
      echo curl --verbose --silent --request PUT \
           --header "Authorization: token ${github_token}" \
           --header "Accept: ${github_restapi}" \
           https://api.github.com/repos/${github_user}/${github_repo}/actions/secrets/${secret_name} \
           -d '{"encrypted_value":"'${encrypted}'","key_id":"'${github_public_key_id}'"}' ;
    fi;
    curl --verbose --silent --request PUT \
         --header "Authorization: token ${github_token}" \
         --header "Accept: ${github_restapi}" \
         https://api.github.com/repos/${github_user}/${github_repo}/actions/secrets/${secret_name} \
         -d '{"encrypted_value":"'${encrypted}'","key_id":"'${github_public_key_id}'"}' ;
         ## 2>&1>/dev/null ;
    return 0;
  }; alias create-github-secret='create_github_secret';
  ## create-github-secret --secret-name=AWS_ACCESS_KEYPAIR \
  ##                      --secret-value="$(IFS=$'\n'; cat ~/.ssh/private/default-terraform)" \
  ##                      --github-token=${github_personal_token} \
  ##                      --github-user=emvaldes \
  ##                      --github-repo=terraform-awscloud \
  ##                      --verbose ;
```

**<span style="color:red">P</span>** -) Injecting all the required secrets into the target GitHub Repository.
[Encrypting GitHub Secrets](https://github.com/emvaldes/devops-tools/blob/7800086abac75e6c558140e789d73249ceb90e02/functions/devops-assumerole.functions#L98)

```shell
AWS_ACCESS_KEY_ID           Terraform AWS Access Key-Id (e.g.: AKIA2...VT7DU).
AWS_DEFAULT_ACCOUNT         The AWS Account number (e.g.: 123456789012).
AWS_DEFAULT_PROFILE         The AWS Credentials Default User (e.g.: default).
AWS_DEFAULT_REGION          The AWS Default Region (e.g.: us-east-1)
AWS_SECRET_ACCESS_KEY       Terraform AWS Secret Access Key (e.g.: zBqDUNyQ0G...IbVyamSCpe)
BACKUP_TERRAFORM            Enable|Disable (true|false) backing-up terraform plan/state
DEPLOY_TERRAFORM            Enable|Disable (true|false) deploying terraform infrastructure
DESTROY_TERRAFORM           Enable|Disable (true|false) destroying terraform infrastructure
DEVOPS_ASSUMEROLE_POLICY    Defines the AWS IAM 'DevOps--Assume-Role.Policy'
DEVOPS_BOUNDARIES_POLICY.   Defines the AWS IAM 'DevOps--Permission-Boundaries.Policy'
DEVOPS_ACCESS_POLICY        Defines the AWS IAM 'DevOps--Custom-Access.Policy'
DEVOPS_ACCESS_ROLE          Defines the AWS IAM 'DevOps--Custom-Access.Role'
DEVOPS_ACCOUNT_NAME         A placeholder for the Deployment Service Account's name (devops).
INSPECT_DEPLOYMENT          Control-Process to enable auditing infrastructure state.
PRIVATE_KEYPAIR_FILE        Terraform AWS KeyPair (location: ~/.ssh/id_rsa).
PRIVATE_KEYPAIR_NAME        Terraform AWS KeyPair (e.g.: devops).
PRIVATE_KEYPAIR_SECRET      Terraform AWS KeyPair (PEM, Private file)
PROVISION_TERRAFORM         Enable|Disable (true|false) the provisioning of the terraform-toolset
TARGET_WORKSPACE            Identifies which is your default (current) environment
UPDATE_PYTHON_LATEST        Enforce the upgrade from the default 2.7 to symlink to the 3.6
UPDATE_SYSTEM_LATEST        Enforce the upgrade of the Operating System.
```

```shell
...
unset AWS_SESSION_TOKEN AWS_TOKEN_EXPIRES;
declare -a default_secrets=(
    AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID}
    AWS_DEFAULT_ACCOUNT=${AWS_ACCOUNT}
    AWS_DEFAULT_PROFILE=default
    AWS_DEFAULT_REGION=${DEFAULT_REGION}
    AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY}
    DEPLOY_TERRAFORM=true
    DESTROY_TERRAFORM=true
    DEVOPS_ACCESS_POLICY=${access_policy}
    DEVOPS_ACCESS_ROLE=${access_role}
    DEVOPS_ACCOUNT_NAME=${user_name}
    INSPECT_DEPLOYMENT=true
    PRIVATE_KEYPAIR_FILE=.ssh/id_rsa
    PRIVATE_KEYPAIR_NAME=${user_name}
    PRIVATE_KEYPAIR_SECRET=?
    PROVISION_TERRAFORM=true
    UPDATE_PYTHON_LATEST=true
    UPDATE_SYSTEM_LATEST=true
  );
for xsecret in ${default_secrets[@]}; do
  export secret_name="${xsecret%%\=*}";
  export secret_value="${xsecret##*\=}";
  create_github_secret --github-repo="${github_repo}" \
                       --github-token="${github_personal_token}" \
                       --github-user="${github_user}" \
                       --secret-name="${secret_name}" \
                       --secret-value="${secret_value}" \
  ;
done;
...
```

**<span style="color:red">Q</span>** -) Populating the AWS Access Key-Pair:
**Note**: It's imperative that you create a Private/Public SSH-Keys. The Private-Key will be encrypted and stored in a GitHub Secret while the Public-Key will be published to all AWS Regions automatically (if requested).

[Encrypting Private SSH-Key](https://github.com/emvaldes/devops-tools/blob/6b17375df1fb450d24a6c9fde945b9a2019101b6/functions/devops-assumerole.functions#L130)

```shell
...
create-github-secret --github-repo="${github_repo}" \
                     --github-token="${github_personal_token}" \
                     --github-user="${github_user}" \
                     --secret-name=PRIVATE_KEYPAIR_SECRET" \
                     --secret-value="$(IFS=$'\n'; cat ${private_sshkey})" \
;
...
```

**<span style="color:red">R</span>** -) How to query the GitHub Secrets to confirm that a particular secret was created (testing):

```shell
$ curl --silent \
       --header "Authorization: token ${github_personal_token}" \
       --header "Accept: ${github_restapi_application}" \
       https://api.github.com/repos/${github_user}/${github_repo}/actions/secrets/${PRIVATE_KEYPAIR_SECRET} ;
```

```json
{
  "name": "PRIVATE_KEYPAIR_SECRET",
  "created_at": "2020-08-22T18:50:43Z",
  "updated_at": "2020-08-22T18:50:43Z"
}
```

**<span style="color:red">S</span>** -) How to query the GitHub Secrets to delete a particular secret:

```shell
$ curl --silent \
       --request DELETE \
       --header "Authorization: token ${github_personal_token}" \
       --header "Accept: ${github_restapi_application}" \
       https://api.github.com/repos/${github_user}/${github_repo}/actions/secrets/PRIVATE_KEYPAIR_SECRET ;
```

**Note**: If you query a non-existing GitHub Secret, the result will be an empty JSON object.

This is the process I would want to use so GitHub Secrets can be recycled and the application is not aware of these updates.<br>
Since the process is leveraging the AWS STS Assume Role capabilities, both GitHub Secrets and Service Accounts are fully decoupled.

**<span style="color:red">T</span>** -) This is how the automation deals with positionless parameters:

```shell
...
oIFS="${IFS}";
for xitem in "${@}"; do
  IFS='='; set `echo -e "${xitem}" | sed -e '1s|^\(-\)\{1,\}||'`
  [[ ${1#*\--} = "access-policy" ]] && export access_policy="${2}";
  [[ ${1#*\--} = "access-role" ]] && export access_role="${2}";
  [[ ${1#*\--} = "assume-policy" ]] && export assume_policy="${2}";
  [[ ${1#*\--} = "company-name" ]] && export company_name="${2}";
  [[ ${1#*\--} = "create-secrets" ]] && export create_secrets=true;
  [[ ${1#*\--} = "custom-boundary" ]] && export custom_boundary="${2}";
  [[ ${1#*\--} = "default-region" ]] && export DEFAULT_REGION="${2}";
  [[ ${1#*\--} = "deploy-keypair" ]] && export deploy_keypair=true;
  [[ ${1#*\--} = "github-repo" ]] && export github_repo="${2}";
  [[ ${1#*\--} = "github-user" ]] && export github_user="${2}";
  [[ ${1#*\--} = "group-name" ]] && export group_name="${2}";
  [[ ${1#*\--} = "master-user" ]] && export master_user="${2}";
  [[ ${1#*\--} = "private-sshkey" ]] && export private_sshkey="${2}";
  [[ ${1#*\--} = "public-sshkey" ]] && export public_sshkey="${2}";
  [[ ${1#*\--} = "role-duration" ]] && export default_roleduration="${2}";
  [[ ${1#*\--} = "user-name" ]] && export user_name="${2}";
  [[ ${1#*\--} = "interactive" ]] && export interactive_mode='true';
  ## [[ ${1#*\--} = "dry-run" ]] && export dry_run="${2}";
  [[ ${1#*\--} = "verbose" ]] && export verbose='true';
  [[ ${1#*\--} = "help" ]] && export display_help='true';
done; IFS="${oIFS}";
...
```

**<span style="color:red">U</span>** -) This is how default parameters are constructed:

```shell
...
## Define custom-parameter(s):
[[ ${#access_policy} -eq 0 ]] && export access_policy='DevOps--Custom-Access.Policy';
[[ ${#access_role} -eq 0 ]] && export access_role='DevOps--Custom-Access.Role';
[[ ${#group_name} -eq 0 ]] && export group_name='devops';
[[ ${#user_name} -eq 0 ]] && export user_name='deployment';
[[ ${#assume_policy} -eq 0 ]] && export assume_policy='DevOps--Assume-Role.Policy';
[[ ${#company_name} -eq 0 ]] && export company_name='anonymous';
[[ ${#create_secrets} -eq 0 ]] && export create_secrets=false;
[[ ${#custom_boundary} -eq 0 ]] && export custom_boundary='Devops--Permission-Boundaries.Policy';
[[ ${#DEFAULT_REGION} -eq 0 ]] && export DEFAULT_REGION='us-east-1';
[[ ${#deploy_keypair} -eq 0 ]] && export deploy_keypair=false;
[[ ${#github_user} -eq 0 ]] && export github_user='emvaldes';
[[ ${#github_repo} -eq 0 ]] && export github_repo='configure-account';
[[ ${#master_user} -eq 0 ]] && export master_user='default';
[[ ${#default_roleduration} -eq 0 ]] && export default_roleduration=3600;
[[ ${#private_sshkey} -eq 0 ]] && export private_sshkey="${HOME}/.ssh/domains/${company_name}/private/${company_name}";
[[ ${#public_sshkey} -eq 0 ]] && export public_sshkey="${HOME}/.ssh/domains/${company_name}/public/${company_name}.pub";
[[ ${#interactive_mode} -eq 0 ]] && export interactive_mode='false';
## [[ ${#dry_run} -eq 0 ]] && export dry_run='false';
[[ ${#verbose} -eq 0 ]] && export verbose='false';
...
```

**<span style="color:red">V</span>** -) Processing Encryption/Publishing of Secrets into GitHub Secrets:

```shell
GitHub Personal Token is: ***
Fetching GitHub Public-Key ...

...

* Uses proxy env variable no_proxy == 'localhost,127.0.0.1'
*   Trying 140.82.114.5...
* TCP_NODELAY set
* Connected to api.github.com (140.82.114.5) port 443 (#0)
* ALPN, offering h2
* ALPN, offering http/1.1
* successfully set certificate verify locations:
*   CAfile: /etc/ssl/cert.pem
  CApath: none
* TLSv1.2 (OUT), TLS handshake, Client hello (1):
* TLSv1.2 (IN), TLS handshake, Server hello (2):
* TLSv1.2 (IN), TLS handshake, Certificate (11):
* TLSv1.2 (IN), TLS handshake, Server key exchange (12):
* TLSv1.2 (IN), TLS handshake, Server finished (14):
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES128-GCM-SHA256
* ALPN, server accepted to use http/1.1
* Server certificate:
*  subject: C=US; ST=California; L=San Francisco; O=GitHub, Inc.; CN=*.github.com
*  start date: Jun 22 00:00:00 2020 GMT
*  expire date: Aug 17 12:00:00 2022 GMT
*  subjectAltName: host "api.github.com" matched cert's "*.github.com"
*  issuer: C=US; O=DigiCert Inc; OU=www.digicert.com; CN=DigiCert SHA2 High Assurance Server CA
*  SSL certificate verify ok.
> PUT /repos/emvaldes/configure-account/actions/secrets/PRIVATE_KEYPAIR_SECRET HTTP/1.1
> Host: api.github.com
> User-Agent: curl/7.64.1
> Authorization: token ***
> Accept: application/vnd.github.v3+json
> Content-Length: 4636
> Content-Type: application/x-www-form-urlencoded
> Expect: 100-continue
>
< HTTP/1.1 100 Continue
* We are completely uploaded and fine
< HTTP/1.1 204 No Content
< Server: GitHub.com
< Date: Mon, 07 Sep 2020 01:15:56 GMT
< Status: 204 No Content
< X-OAuth-Scopes: admin:enterprise, admin:gpg_key, admin:org, admin:org_hook, admin:public_key, admin:repo_hook, delete:packages, delete_repo, gist, notifications, read:packages, repo, user, workflow, write:discussion, write:packages
< X-Accepted-OAuth-Scopes:
< X-GitHub-Media-Type: github.v3; format=json
< X-RateLimit-Limit: 5000
< X-RateLimit-Remaining: 4888
< X-RateLimit-Reset: 1599443591
< X-RateLimit-Used: 112
< Access-Control-Expose-Headers: ETag, Link, Location, Retry-After, X-GitHub-OTP, X-RateLimit-Limit, X-RateLimit-Remaining, X-RateLimit-Used, X-RateLimit-Reset, X-OAuth-Scopes, X-Accepted-OAuth-Scopes, X-Poll-Interval, X-GitHub-Media-Type, Deprecation, Sunset
< Access-Control-Allow-Origin: *
< Strict-Transport-Security: max-age=31536000; includeSubdomains; preload
< X-Frame-Options: deny
< X-Content-Type-Options: nosniff
< X-XSS-Protection: 1; mode=block
< Referrer-Policy: origin-when-cross-origin, strict-origin-when-cross-origin
< Content-Security-Policy: default-src 'none'
< Vary: Accept-Encoding, Accept, X-Requested-With
< X-GitHub-Request-Id: D4D4:4B2B:135FE8B:2A8224B:5F5589CC
<
* Connection #0 to host api.github.com left intact
* Closing connection 0
```

---

**<span style="color:red">01</span>** -) Creating IAM Policy ['DevOps--Custom-Access.Policy']

```json
{
    "Policy": {
        "PolicyName": "DevOps--Custom-Access.Policy",
        "PolicyId": "ANPA2N4P2YIKAG36C5GX2",
        "Arn": "arn:aws:iam::123456789012:policy/DevOps--Custom-Access.Policy",
        "Path": "/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 0,
        "PermissionsBoundaryUsageCount": 0,
        "IsAttachable": true,
        "CreateDate": "2020-09-07T23:17:47+00:00",
        "UpdateDate": "2020-09-07T23:17:47+00:00"
    }
}
```

**<span style="color:red">02</span>** -) Creating IAM Boundary Policy ['Devops--Permission-Boundaries.Policy']

```json
{
    "Policy": {
        "PolicyName": "Devops--Permission-Boundaries.Policy",
        "PolicyId": "ANPA2N4P2YIKJXWXEDACY",
        "Arn": "arn:aws:iam::123456789012:policy/Devops--Permission-Boundaries.Policy",
        "Path": "/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 0,
        "PermissionsBoundaryUsageCount": 0,
        "IsAttachable": true,
        "CreateDate": "2020-09-07T23:17:51+00:00",
        "UpdateDate": "2020-09-07T23:17:51+00:00"
    }
}
```

**<span style="color:red">03</span>** -) Creating IAM Group ['devops']

```json

{
    "Group": {
        "Path": "/",
        "GroupName": "devops",
        "GroupId": "AGPA2N4P2YIKIPXP4UURH",
        "Arn": "arn:aws:iam::123456789012:group/devops",
        "CreateDate": "2020-09-07T23:17:53+00:00"
    }
}
```

**<span style="color:red">04</span>** -) Creating IAM Service-Account ['devops']

```json
{
    "User": {
        "Path": "/",
        "UserName": "devops",
        "UserId": "AIDA2N4P2YIKJACYLZ6DI",
        "Arn": "arn:aws:iam::123456789012:user/devops",
        "CreateDate": "2020-09-07T23:17:55+00:00"
    }
}
```

**<span style="color:red">05</span>** -) Creating IAM Access-Keys: ['devops']

```shell
AWS Credential :: AWS_ACCESS_KEY_ID = ***AWS**ACCESS***KEY***ID***
AWS Credential :: AWS_SECRET_ACCESS_KEY = ***AWS**SECRET***ACCESS***KEY***

Displaying auto-generated credentials:

[anonymous-devops]
aws_access_key_id = ***AWS**ACCESS***KEY***ID***
aws_secret_access_key = ***AWS**SECRET***ACCESS***KEY***
aws_session_token =
x_principal_arn = arn:aws:iam::123456789012:user/devops
x_security_token_expires =

```

**<span style="color:red">06</span>** -) Attaching/Listing IAM Service-Account ['devops'] into IAM Group ['devops']

```json
{
  "Users": [
    {
      "Path": "/",
      "UserName": "devops",
      "UserId": "AIDA2N4P2YIKJACYLZ6DI",
      "Arn": "arn:aws:iam::123456789012:user/devops",
      "CreateDate": "2020-09-07T23:17:55+00:00"
    }
  ],
  "Group": {
    "Path": "/",
    "GroupName": "devops",
    "GroupId": "AGPA2N4P2YIKIPXP4UURH",
    "Arn": "arn:aws:iam::123456789012:group/devops",
    "CreateDate": "2020-09-07T23:17:53+00:00"
  }
}
```

**<span style="color:red">07</span>** -) Creating IAM Role ['DevOps--Custom-Access.Role']

```json
{
    "Role": {
        "Path": "/",
        "RoleName": "DevOps--Custom-Access.Role",
        "RoleId": "AROA2N4P2YIKBTX2LAK6V",
        "Arn": "arn:aws:iam::123456789012:role/DevOps--Custom-Access.Role",
        "CreateDate": "2020-09-07T23:18:03+00:00",
        "AssumeRolePolicyDocument": {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Principal": {
                        "AWS": [
                            "arn:aws:iam::123456789012:user/devops"
                        ]
                    },
                    "Action": [
                        "sts:AssumeRole"
                    ]
                }
            ]
        }
    }
}
```

**<span style="color:red">08</span>** -) Attaching IAM Role ['DevOps--Custom-Access.Policy']

**<span style="color:red">09</span>** -) Listing IAM Role ['DevOps--Custom-Access.Role']:

```json
{
  "Role": {
    "Path": "/",
    "RoleName": "DevOps--Custom-Access.Role",
    "RoleId": "AROA2N4P2YIKBTX2LAK6V",
    "Arn": "arn:aws:iam::123456789012:role/DevOps--Custom-Access.Role",
    "CreateDate": "2020-09-07T23:18:03+00:00",
    "AssumeRolePolicyDocument": {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "AWS": "arn:aws:iam::123456789012:user/devops"
          },
          "Action": "sts:AssumeRole"
        }
      ]
    },
    "Description": "DevOps Infrastructure Deployment - Automation Services.",
    "MaxSessionDuration": 3600,
    "RoleLastUsed": {}
  }
}
```

**<span style="color:red">10</span>** -) Attached IAM Role Policy ['DevOps--Custom-Access.Role']:

```json
{
  "AttachedPolicies": [
    {
      "PolicyName": "DevOps--Custom-Access.Policy",
      "PolicyArn": "arn:aws:iam::123456789012:policy/DevOps--Custom-Access.Policy"
    }
  ]
}
```

**<span style="color:red">11</span>** -) Assigning IAM Permission Boundary ['DevOps--Custom-Access.Role'] ...

**<span style="color:red">12</span>** -) Creating IAM Policy ['DevOps--Assume-Role.Policy']

```json
{
    "Policy": {
        "PolicyName": "DevOps--Assume-Role.Policy",
        "PolicyId": "ANPA2N4P2YIKGEFKJRRWD",
        "Arn": "arn:aws:iam::123456789012:policy/DevOps--Assume-Role.Policy",
        "Path": "/",
        "DefaultVersionId": "v1",
        "AttachmentCount": 0,
        "PermissionsBoundaryUsageCount": 0,
        "IsAttachable": true,
        "CreateDate": "2020-09-07T23:18:12+00:00",
        "UpdateDate": "2020-09-07T23:18:12+00:00"
    }
}
```

**<span style="color:red">13</span>** -) Creating IAM Policy ['DevOps--Assume-Role.Policy']

```json
{
  "AttachedPolicies": [
    {
      "PolicyName": "DevOps--Assume-Role.Policy",
      "PolicyArn": "arn:aws:iam::123456789012:policy/DevOps--Assume-Role.Policy"
    }
  ]
}
```

```shell
-rw-r--r--  1 emvaldes  staff  230 Sep  7 16:18 /Users/emvaldes/.aws/access/123456789012/anonymous-devops.credentials

[anonymous-devops]
aws_access_key_id = ASIA2N4P2YIKONYL63U3
aws_secret_access_key = SlG2c0hVMW20RQt1qjGABe+XmdgwGdYzDWLbjcyf
aws_session_token = IQoJb3JpZ2luX2VjEBgaCXVzLWVhc3QtMSJIMEYCIQD2R0+5sBPuL2sdzBbrAI73T4wdeC9msEMo8/8OPFmVkgIhAMioLy8bRsgLsM+I8mSv6M6S8BBsU+DI4vPj+FgVfetEKq0CCCAQARoMNzE3MDI0MzEzODc2IgyrWejVfctJ0z2P1SIqigKBaHYv7lviliRPVH0+U1Tax5wCG7gdPR+PrMbCbabmeNgSzGXJMbK4qBXKfIL2YS1EUP5rTYclnw+Bn8NuVsWGjns8zHpYev2HM0wf9Fqb7W5CXx3y6dZpWSRLAv39mNMZ0ffAwFMXPeV8IQT+T9+Xy+1gspkEAd+wWeLC5x7YAPysnu1nr9BuidCAtgDxqGiku74g1bVVK09QLPlnaE+yLfrqd6TTGorG4R1YYEpgdYB1iKJA3TnMsova7mKdIWkUudFLKizDtJC1FRQPODR6ynWBqPtheOqy9Jz5VEkR1KKZdM+xMok0X7bsBZvIzrsjC1N4FWYvkELijrxoLrFjLlF3qCnE9g3QHDC7/9r6BTqcAV658MxL0f2MzCCgUzdH1kxokedgFSfFG1wh8weUjAamzOzbnUB2FwyaE8CScXI4MUSDs5wO4lTCyNYa+SvFgA35JSy6QuSgxTTjeFz3Zb2mh+tb8w9nuzNY9Dx4cwmSHrkCSxyly4dqjSUY93iOYJetfzadgW6yJxWBXyLVEULGzQl+sBE6dtuIRwtKnuTe2lDlWzn7wUIAecww2Q==
x_principal_arn = arn:aws:iam::123456789012:user/devops
x_security_token_expires = 2020-09-08T00:18:19+00:00

{
    "UserId": "AROA2N4P2YIKBTX2LAK6V:TerraformPipeline-20200907161818",
    "Account": "123456789012",
    "Arn": "arn:aws:sts::123456789012:assumed-role/DevOps--Custom-Access.Role/TerraformPipeline-20200907161818"
}

Token Expires: 2020-09-08 00:18:19 [1599524299]
 Current Date: 2020-09-07 23:18:20 [1599520700]

The Assumed-Role Session has 59 minutes remaining until it expires.
```

```shell
Deploying Key-Pair [devops]: /Users/emvaldes/.ssh/domains/anonymous/public/anonymous.pub -> us-east-1
Deploying Key-Pair [devops]: /Users/emvaldes/.ssh/domains/anonymous/public/anonymous.pub -> us-east-2
Deploying Key-Pair [devops]: /Users/emvaldes/.ssh/domains/anonymous/public/anonymous.pub -> us-west-1
Deploying Key-Pair [devops]: /Users/emvaldes/.ssh/domains/anonymous/public/anonymous.pub -> us-west-2
```

**<span style="color:red">14</span>** -) Creating AWS S3 Bucket ['terraform--states--123456789012']

**<span style="color:red">15</span>** -) Configuring/Fetching AWS S3 Bucket ['terraform--states--123456789012'] Access Control List (ACL)

```json
{
  "Owner": {
    "DisplayName": "dating.cherryblossoms",
    "ID": "c7704c0502cb4ffae2240fd22526ac4430f3bf6097b92248f4e9e79b76242cc1"
  },
  "Grants": [
    {
      "Grantee": {
        "DisplayName": "dating.cherryblossoms",
        "ID": "c7704c0502cb4ffae2240fd22526ac4430f3bf6097b92248f4e9e79b76242cc1",
        "Type": "CanonicalUser"
      },
      "Permission": "FULL_CONTROL"
    }
  ]
}
```

**<span style="color:red">16</span>** -) Configuring/Fetching AWS S3 Bucket ['terraform--states--123456789012'] Log-Delivery

```json
{
  "Owner": {
    "DisplayName": "dating.cherryblossoms",
    "ID": "c7704c0502cb4ffae2240fd22526ac4430f3bf6097b92248f4e9e79b76242cc1"
  },
  "Grants": [
    {
      "Grantee": {
        "Type": "Group",
        "URI": "http://acs.amazonaws.com/groups/s3/LogDelivery"
      },
      "Permission": "WRITE"
    },
    {
      "Grantee": {
        "Type": "Group",
        "URI": "http://acs.amazonaws.com/groups/s3/LogDelivery"
      },
      "Permission": "READ_ACP"
    }
  ]
}
```

**<span style="color:red">17</span>** -) Configuring IAM Policy ['DevOps--S3Bucket-Logging.Policy']

```json
{
  "TargetPrefix": "logs/",
  "TargetBucket": "terraform--states--123456789012"
}
```

**<span style="color:red">18</span>** -) Configuring/Fetching AWS S3 Bucket ['terraform--states--123456789012'] Versioning

```json
{
  "Status": "Enabled"
}
```

**<span style="color:red">19</span>** -) Creating IAM Policy ['DevOps--S3Bucket-Principal.Policy']

```json
{
  "Version": "2012-10-17",
  "Id": "PolicyS3Bucket",
  "Statement": [
    {
      "Sid": "StmtS3Bucket",
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::123456789012:user/devops"
      },
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::terraform--states--123456789012/*"
    }
  ]
}
```

## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/emvaldes/configure-account/edit/master/README.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

## Configure Service-Account Script

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/emvaldes/configure-account/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
