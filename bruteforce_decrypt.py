{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyM+yj8W2BosfQ24z7aT1E+1",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/anvithalolla/Bypassing-Ransomware/blob/main/bruteforce_decrypt.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "tykbrjOfuZkF"
      },
      "outputs": [],
      "source": [
        "from zipfile import ZipFile\n",
        "import sys\n",
        "\n",
        "def attempt_extract(zf_handle, password):\n",
        "    try:\n",
        "        # Attempt to extract the zip file using the given password\n",
        "        zf_handle.extractall(pwd=password.strip())\n",
        "        print(f\"[+] Password found: {password.decode().strip()}\")\n",
        "        return True\n",
        "    except RuntimeError as e:\n",
        "        # Handle incorrect password attempts\n",
        "        if 'Bad password' in str(e):\n",
        "            return False\n",
        "        else:\n",
        "            print(f\"[-] An error occurred: {e}\")\n",
        "            sys.exit(1)\n",
        "    except Exception as e:\n",
        "        print(f\"[-] An unexpected error occurred: {e}\")\n",
        "        sys.exit(1)\n",
        "\n",
        "def main():\n",
        "    print(\"[+] Beginning bruteforce\")\n",
        "\n",
        "    with ZipFile('enc.zip') as zf:\n",
        "        with open('rockyou.txt', 'rb') as f:\n",
        "            for line in f:\n",
        "                password = line.strip()\n",
        "                if attempt_extract(zf, password):\n",
        "                    break\n",
        "            else:\n",
        "                print(\"[+] Password not found in list\")\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    main()\n"
      ]
    }
  ]
}