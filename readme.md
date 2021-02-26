# Setup Ubuntu

## Install powerline

Run in terminal:

```bash
git clone https://github.com/b-ryan/powerline-shell && cd powerline-shell && sudo python3 setup.py install
```

Copy the code block below and paste to end of *~/.bashrc*:

```bash
function _update_ps1() {
    PS1=$(powerline-shell $?)
}

if [[ $TERM != linux && ! $PROMPT_COMMAND =~ _update_ps1 ]]; then
    PROMPT_COMMAND="_update_ps1; $PROMPT_COMMAND"
fi
```

Run in terminal:

```bash
mkdir -p ~/.config/powerline-shell && \powerline-shell --generate-config > ~/.config/powerline-shell/config.json
```

Copy folder **powerline-shell** and paste to **~/.config**

![This is my terminal](./terminal.jpg)

> Config segments in *./powerline-shell/config.json*
>
> Config theme in *./powerline-shell/themes/default.py*

## Install apache2 mysql php8.0

Copy *InstallPHP8.0MariaDB.sh* to current working older

Run in terminal:

```bash
sudo chmod +x ./InstallPHP8.0MariaDB.sh && sudo ./InstallPHP8.0MariaDB.sh
```

> Notice announcements in terminal

## Install JDK 15

Run in terminal:

```bash
sudo add-apt-repository ppa:linuxuprising/java && sudo apt update && sudo apt install oracle-java15-installer
```
