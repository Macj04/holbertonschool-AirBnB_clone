#!/bin/bash
echo ""

black='\033[1m'
green='\033[0;32m'
red='\033[0;31m'
reset='\033[0m'

echo -e "${green}${black}Starting...${reset}"
echo ""
echo -e  "${red}${black}Trying to delete file.json${reset}"
rm file.json
echo""
echo -e "${green}${black}Creating TXT file.${reset}"
read -p "File name: " output_file
echo ""
echo -e  "${green}${black}${black}STARTED${reset}"
echo ""

exec > >(tee "$output_file")

echo "╭══════ .✧. ══════╮"
echo "guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py" ; ./test_save_reload_base_model.py
echo ""
echo "───────────────────────"
echo ""
echo "guillaume@ubuntu:~/AirBnB$ cat file.json ; echo " ; cat file.json ; echo ""
echo ""
echo "───────────────────────"
echo ""
echo "guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py" ; ./test_save_reload_base_model.py
echo ""
echo "───────────────────────"
echo ""
echo "guillaume@ubuntu:~/AirBnB$ ./test_save_reload_base_model.py" ; ./test_save_reload_base_model.py
echo ""
echo "───────────────────────"
echo ""
echo "guillaume@ubuntu:~/AirBnB$ cat file.json ; echo " ; cat file.json ; echo ""
echo ""
echo "───────────────────────"
echo ""
echo "╰══════ .✧. ══════╯"

exec >&2
echo ""
echo -e "${green}${black}Saving to TXT file.${reset}"
echo -e "${red}${black}Finished.${reset}"
echo ""