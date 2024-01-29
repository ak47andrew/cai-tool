# Cai tools

> [!CAUTION]
> This project violates [Crush on AI ToS](https://crushon.ai/terms-of-service). Using it can lead it your account being banned! You have been warned and I am not responsible for this.

> [!WARNING]
> This project is not finished yet, so some things in the README may appear later

> [!NOTE]
> You can ignore "Requirements" and "Installation" blocks by downloading executables on the [Release tab](https://github.com/Tumpa-Prizrak/cai-tool/releases)

> [!NOTE]
> Installation guide is written for Linux users. Windows is pretty similar, but google steps that is outputting an error

Cai stands for [Crush on AI](https://crushon.ai/). This tool will help you with managing your Favorite characters in CRUD: create, read, update, and delete

> [!NOTE]
> `ChatGPT tl;dr` This project provides a tool to manage your favorite characters on Crush on the AI platform. However, using it violates Crush on AI's terms of service and can lead to account banning. The tool requires Python 3.9+. You can download executables from the Release tab to avoid installation steps. The tool allows CRUD operations on your favorite characters and is accessible via shell or terminal only. The README provides instructions on how to install and use the tool, including commands for parsing, removing, and randomly selecting a character.

## Requirements

- `Python 3.9+`

## Installation

- Copy the project and create a virtual environment

```sh
git clone https://github.com/Tumpa-Prizrak/cai-tool.git
cd cai-tool
python -m venv venv
```

- Install python packages

```sh
source venv/bin/activate
pip install -r requirements.txt
```

- Change the *root_folder* variable in `config.py` to your home folder or another directory that contains the `cai` directory - a place where the utility will save its OC database.
- Change directories at the `cai` file to place with the `src` folder in it.
- Allow execution of the `cai` file

```sh
chmod +x cai
```

- Run it!

```sh
./cai
```

> [!TIP]
> You can copy the `cai` file to any directory in your `$PATH` variable. For example to `/usr/bin`. This will make utility available from any directory. Use the cp command for this: `sudo cp cai /usr/bin/cai`.

## Usage

See `cai --help` for brief usage. All interactions will be available only using a shell or other type of terminal. You can't use this via UI

> [!NOTE]
> This utility doesn't manage your real data on the CAI platform - it's on your local PC only. Util there's no public API available - it's almost impossible to implement

### First using

Create a `plaintext.txt` file in your `cai` directory. Go to your [Favorite characters page](https://crushon.ai/account) (Profile -> Interactions -> Favorite characters). Press `Ctrl + A` to highlight the text of the webpage and `Ctrl + C` to copy all highlighted text. Then paste it to `plaintext.txt`. Run `cai parse`

### Parse

#### Syntax

```sh
cai parse
```

#### Description

The parse command parses your `plaintext.txt` for characters and saves them to `ocs.json` for later use. You should run this command every time you change your `plaintext.txt` file. Match the number of characters parsed with your Favorite character amount. If it doesn't match - create an issue at [Github Issues page](https://github.com/Tumpa-Prizrak/cai-tool/issues) with your "plaintext.txt" file attached, probably something wrong with the script

#### Errors

- **plaintext.txt is not found! Did you create it?** - make sure you created `plaintext.txt` and changed the directory in a `config.py` file. The directory must always contain `plaintext.txt`
- **No characters found! Did you fill up plaintext.txt?** - make sure you filled up `plaintext.txt` with data you copied from "Favorite characters". Otherwise - create an issue at [Github Issues page](https://github.com/Tumpa-Prizrak/cai-tool/issues) with your "plaintext.txt" file attached, probably something wrong with the script

### Random

#### Syntax

```sh
cai random
```

#### Description

Random command choose a random character from your library and output all the info about it:

- id - position of the character in the list
- messages - the approximate amount of total messages. Example: *\~ 2000 msg*
- memories - the amount of memories with this character
- name - the name of this character
- by {author} - author of this character
- description - brief description of the character
- tags - list of the tags of the character, categorizing it. Example: *NSFW, Elf, Submissive, Kinky, Seductive, Female*

#### Errors

- `No OCs found! Did you fill plaintext.txt?` - make sure you filled up `plaintext.txt` with data you copied from "Favorite characters" and then used "cai parse"
- `No parsed OCs found! use cai parse` - File `ocs.json` is not found. Run the `cai parse` command before using this command

### Remove

#### Syntax

> [!IMPORTANT]
> You must specify either id or name. If you specify both - **id** will be used

```sh
cai remove --id <integer> --name <string>
```

#### Description

Removes character based on its id or name.

- Character id - position of the character in the list. Usually, you get it by using the `cai random` command. Press **Enter** to confirm deletion or **N** and then **Enter** to cancel it
- Name - name of the character. utility is using indirect comparison so you'll be able to find your character even without one in one match. Press **Enter** to see the next character, press **Y**, and then **Enter** to delete a character.

#### Errors

- `No OCs found! Did you fill plaintext.txt?` - make sure you filled up `plaintext.txt` with data you copied from "Favorite characters" and then used "cai parse"
- `No parsed OCs found! use cai parse` - File `ocs.json` is not found. Run the `cai parse` command before using this command
